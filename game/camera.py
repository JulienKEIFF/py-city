import pygame as pg

class Camera:

  def __init__(self, width, height):
    self.width = width
    self.height = height

    self.scroll = pg.Vector2(0, 0)
    self.direction_x = 0
    self.direction_y = 0
    self.speed = 25

  def update(self):
    mouse_position = pg.mouse.get_pos()

    # x movement
    if mouse_position[0] > self.width * 0.97:
      self.direction_x = -self.speed
    elif mouse_position[0] < self.width * 0.03:
      self.direction_x = self.speed
    else:
      self.direction_x = 0

     # y movement
    if mouse_position[1] > self.height * 0.97:
      self.direction_y = -self.speed
    elif mouse_position[1] < self.height * 0.03:
      self.direction_y = self.speed
    else:
      self.direction_y = 0

    # update scroll
    self.scroll.x += self.direction_x
    self.scroll.y += self.direction_y    