import pygame as pg
import random
import noise

from .settings import TILE_SIZE
from .tile_repository import load_images
from .build import *
class World:

  def __init__(self, resources, entities, hud, grid_x, grid_y, width, height):
    self.resources = resources
    self.entities = entities
    self.hud = hud
    self.grid_x = grid_x
    self.grid_y = grid_y
    self.width = width
    self.height = height

    self.perlin_scale = grid_x/2
    self.buildings = [[None for x in range(self.grid_x)] for y in range(self.grid_y)]

    self.grass_tiles = pg.Surface((grid_x * TILE_SIZE * 2, grid_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
    self.tiles = load_images()
    self.world = self.create_world()

    self.temp_tile = None



  def update(self, camera):
    mouse_pos = pg.mouse.get_pos()
    mouse_action = pg.mouse.get_pressed()

    self.temp_tile = None
    if self.hud.selected_building is not None:

      if self.resources.is_affordable(self.hud.selected_building["name"]):
        grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera.scroll)

        if self.can_place_tile(grid_pos):
          img = self.hud.selected_building["image"].copy()
          img.set_alpha(100)

          try:
            render_pos = self.world[grid_pos[0]][grid_pos[1]]["render_pos"]
            iso_poly = self.world[grid_pos[0]][grid_pos[1]]["iso_poly"]
            collision = self.world[grid_pos[0]][grid_pos[1]]["collision"]

            self.temp_tile = {
              "image": img,
              "render_pos": render_pos,
              "iso_poly": iso_poly,
              "collision": collision
            }

            if mouse_action[0] and not collision:
              if self.hud.selected_building["name"] == "mine":
                entity = Mine(grid_pos, self.resources)
                self.entities.append(entity)
                self.buildings[grid_pos[0]][grid_pos[1]] = entity
              
              if self.hud.selected_building["name"] == "sawmill":
                entity = SawMill(grid_pos, self.resources)
                self.entities.append(entity)
                self.buildings[grid_pos[0]][grid_pos[1]] = entity

              if self.hud.selected_building["name"] == "church":
                entity = Chuch(grid_pos, self.resources)
                self.entities.append(entity)
                self.buildings[grid_pos[0]][grid_pos[1]] = entity

              if self.hud.selected_building["name"] == "house":
                entity = House(grid_pos, self.resources)
                self.entities.append(entity)
                self.buildings[grid_pos[0]][grid_pos[1]] = entity

              self.world[grid_pos[0]][grid_pos[1]]["tile"] = self.hud.selected_building["name"]
              self.world[grid_pos[0]][grid_pos[1]]["collision"] = True
              self.hud.selected_building = None
              pg.mixer.Sound("assets/sound/sfx/build.wav").play().set_volume(0.05)
              
          except:
            pass




  def draw(self, screen, camera):
    screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

    for x in range(self.grid_x):
      for y in range(self.grid_y):
        render_pos = self.world[x][y]["render_pos"]

        tile = self.world[x][y]["tile"]
        if tile != "":
          screen.blit(
            self.tiles[tile], 
            (
              render_pos[0] + self.grass_tiles.get_width() / 2 + camera.scroll.x, 
              render_pos[1] - (self.tiles[tile].get_height() - TILE_SIZE) + camera.scroll.y
            )
          )

    if self.temp_tile is not None:
      iso_poly = self.temp_tile["iso_poly"]
      iso_poly = [(x + self.grass_tiles.get_width()/2 + camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
      if self.temp_tile["collision"]:
        pg.draw.polygon(screen, (255, 0, 0), iso_poly, 3)
      else:
        pg.draw.polygon(screen, (255, 255, 255), iso_poly, 3)
      render_pos = self.temp_tile["render_pos"]
      screen.blit(
        self.temp_tile["image"],
        (
          render_pos[0] + self.grass_tiles.get_width() / 2 + camera.scroll.x,
          render_pos[1] - (self.temp_tile["image"].get_height() - TILE_SIZE) + camera.scroll.y
        )
      )

    self.hud.draw(screen)



  def create_world(self):
    world = []

    for grid_x in range(self.grid_x):
      world.append([])
      for grid_y in range(self.grid_y):
        world_tile = self.grid_to_world(grid_x, grid_y)
        world[grid_x].append(world_tile)

        render_pos = world_tile["render_pos"]
        self.grass_tiles.blit(self.tiles["grass"], (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))

    return world



  def grid_to_world(self, grid_x, grid_y):
    rect = [
      (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
      (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
      (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
      (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
    ]

    iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

    min_x = min([x for x, y in iso_poly])
    min_y = min([y for x, y in iso_poly])
    
    r = random.randint(0, 100)
    perlin = 100 * noise.pnoise2(
      grid_x/self.perlin_scale, 
      grid_y/self.perlin_scale, 
    )

    if(perlin >= 15) or (perlin <= -35):
      tile = "tree"
    else:
      if r == 1:
        tile = "tree"
      elif r == 2:
        tile = "rock"
      else:
        tile = ""

    out = {
      "grid": [grid_x, grid_y],
      "cart_rect": rect,
      "iso_poly": iso_poly,
      "render_pos": [min_x, min_y],
      "tile": tile,
      "collision": False if tile == "" else True
    }

    return out



  def cart_to_iso(self, x, y):
    iso_x = x - y
    iso_y = (x + y) / 2
    return (iso_x, iso_y)



  def mouse_to_grid(self, x, y, scroll):
    world_x = x - scroll.x - self.grass_tiles.get_width() / 2
    world_y = y - scroll.y

    cart_y = (2 * world_y - world_x) / 2
    cart_x = cart_y + world_x

    grid_x = int(cart_x // TILE_SIZE)
    grid_y = int(cart_y // TILE_SIZE)

    return grid_x, grid_y



  def can_place_tile(self, grid_pos):
    mouse_on_panel = False
    for rect in [self.hud.resources_rect, self.hud.build_rect]:
      if rect.collidepoint(pg.mouse.get_pos()):
        mouse_on_panel = True
    world_bounds = (0 <= grid_pos[0] <= self.grid_x) and (0 <= grid_pos[1] <= self.grid_x)

    if world_bounds and not mouse_on_panel:
      return True
    else:
      return False