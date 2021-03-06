import pygame as pg

class Camera:

  def __init__(self, width, height):
    self.width = width
    self.height = height

    self.scroll = pg.Vector2(-2500, -1000) # Center the view at launch
    self.direction_x = 0
    self.direction_y = 0
    self.speed = 25

    self.max_scroll_x = -5250
    self.min_scroll_x = 250
    self.max_scroll_y = -2500
    self.min_scroll_y = 250

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
    new_scroll_x = self.direction_x + self.scroll.x
    new_scroll_y = self.direction_y + self.scroll.y
    if self.min_scroll_x > new_scroll_x and self.max_scroll_x < new_scroll_x: 
      self.scroll.x += self.direction_x

    if self.min_scroll_y > new_scroll_y and self.max_scroll_y < new_scroll_y: 
      self.scroll.y += self.direction_y    