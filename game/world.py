import pygame as pg
import random

from .settings import TILE_SIZE, WORLD_SIZE

class World:

  def __init__(self, grid_x, grid_y, width, height):
    self.grid_x = grid_x
    self.grid_y = grid_y
    self.width = width
    self.height = height

    self.grass_tiles = pg.Surface((grid_x * TILE_SIZE * 2, grid_y * TILE_SIZE + 2 * TILE_SIZE))
    self.tiles = self.load_images()
    self.world = self.create_world()

  def create_world(self):
    world = []

    for grid_x in range(self.grid_x):
      world.append([])
      for grid_y in range(self.grid_y):
        world_tile = self.grid_to_world(grid_x, grid_y)
        world[grid_x].append(world_tile)

        render_pos = world_tile["render_pos"]
        self.grass_tiles.blit(self.tiles["grass"], (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1]))

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

    if r <= 5:
      tile = "tree"
    elif r<= 10:
      tile = "rock"
    else:
      tile = ""

    out = {
      "grid": [grid_x, grid_y],
      "cart_rect": rect,
      "iso_poly": iso_poly,
      "render_pos": [min_x, min_y],
      "tile": tile,
    }

    return out

  def cart_to_iso(self, x, y):
    iso_x = x - y
    iso_y = (x + y) / 2
    return (iso_x, iso_y)

  def load_images(self):
    grass = pg.image.load("assets/env/grass.png")
    block = pg.image.load("assets/env/block.png")
    tree = pg.image.load("assets/env/tree.png")
    rock = pg.image.load("assets/env/rock.png")

    return {"grass": grass, "block": block, "tree": tree, "rock": rock}