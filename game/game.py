import pygame as pg
import sys
from .world import World
from .settings import TILE_SIZE, DEBUG, FPS_COUNTER, WORLD_SIZE
from .utils import draw_text
from .camera import Camera

class Game:

  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock
    self.width, self.height = self.screen.get_size()

    # World
    self.world = World(WORLD_SIZE, WORLD_SIZE, self.width, self.height)

    # Camera
    self.camera = Camera(self.width, self.height)

  def run(self):
    self.playing = True
    while self.playing:
      self.clock.tick(FPS_COUNTER)
      self.events()
      self.update()
      self.draw()
  
  def events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.playing = False
        pg.quit()
        sys.exit()

  def update(self):
    self.camera.update()

  def draw(self):
    self.screen.fill((10, 10, 10))

    self.screen.blit(self.world.grass_tiles, (self.camera.scroll.x, self.camera.scroll.y))

    for x in range(self.world.grid_x):
      for y in range(self.world.grid_y):
        render_pos = self.world.world[x][y]["render_pos"]

        tile = self.world.world[x][y]["tile"]
        if tile != "":
          self.screen.blit(
            self.world.tiles[tile], 
            (
              render_pos[0] + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x, 
              render_pos[1] - (self.world.tiles[tile].get_height() - TILE_SIZE) + self.camera.scroll.y
            )
          )



        if DEBUG:
          rect = pg.Rect(cell[0][0], cell[0][1], TILE_SIZE, TILE_SIZE)
          cell = self.world.world[x][y]["cart_rect"]
          
          p = self.world.world[x][y]["iso_poly"]
          p = [(x + self.width/2, y + self.height/4) for x, y in p]
          pg.draw.polygon(self.screen, (0, 0, 0), p, 1)
          
          pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

    draw_text(
      self.screen,
      'fps={}'.format(round(self.clock.get_fps())),
      25,
      (255,255,255),
      (10,10)
    )

    pg.display.flip()