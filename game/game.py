import pygame as pg
import sys
from .world import World
from .settings import FPS_COUNTER, WORLD_SIZE
from .utils import draw_text
from .camera import Camera
from .hud import Hud
from .resources import Resources

class Game:

  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock
    self.width, self.height = self.screen.get_size()
    self.entities = []

    self.resources = Resources()

    # HUD
    self.hud = Hud(self.resources, self.width, self.height)

    # World
    self.world = World(self.resources, self.entities, self.hud, WORLD_SIZE, WORLD_SIZE, self.width, self.height)

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
    self.hud.update()
    self.world.update(self.camera)
    for e in self.entities: e.update()



  def draw(self):
    self.screen.fill((0,0,0))
    self.world.draw(self.screen, self.camera)
    draw_text(
      self.screen,
      'fps={}'.format(round(self.clock.get_fps())),
      25,
      (255,255,255),
      (10,10)
    )

    pg.display.flip()

