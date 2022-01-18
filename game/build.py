import pygame as pg

class Mine:
  def __init__(self, position, ressource):
    self.image  = pg.image.load("assets/building/mine.png")
    self.name = "mine"
    self.rect = self.image.get_rect(topleft=position)
    self.resource = ressource
    self.resource.apply_cost_to_resource(self.name)
    self.resource_cooldown = pg.time.get_ticks()

  def update(self):
    now = pg.time.get_ticks()
    if now - self.resource_cooldown > 2000:
      self.resource.resources["rock"]["total"] += 10
      self.resource_cooldown = now


class SawMill:
  def __init__(self, position, ressource):
    self.image  = pg.image.load("assets/building/sawmill.png")
    self.name = "sawmill"
    self.rect = self.image.get_rect(topleft=position)
    self.resource = ressource
    self.resource.apply_cost_to_resource(self.name)
    self.resource_cooldown = pg.time.get_ticks()

  def update(self):
    now = pg.time.get_ticks()
    if now - self.resource_cooldown > 2000:
      self.resource.resources["wood"]["total"] += 10
      self.resource_cooldown = now


class Chuch:
  def __init__(self, position, ressource):
    self.image  = pg.image.load("assets/building/sawmill.png")
    self.name = "church"
    self.rect = self.image.get_rect(topleft=position)
    self.resource = ressource
    self.resource.apply_cost_to_resource(self.name)
    self.resource_cooldown = pg.time.get_ticks()

  def update(self):
    now = pg.time.get_ticks()
    if now - self.resource_cooldown > 2000:
      self.resource.resources["gold"]["total"] += 10
      self.resource_cooldown = now