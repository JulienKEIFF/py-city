import pygame as pg
from .utils import draw_text
from .settings import HUD_COLOR
from .resources import Resources
class Hud:
  
  def __init__(self, resources, width, height):
    self.width = width
    self.height = height
    self.resources = resources

    self.hud_color = HUD_COLOR

    # ressources HUD
    self.ressources_surface = pg.Surface((width, height * 0.04), pg.SRCALPHA)
    self.resources_rect = self.ressources_surface.get_rect(topleft=(0, 0))
    self.ressources_surface.fill(self.hud_color)

    # Building HUD
    self.building_surface = pg.Surface((width * 1, height * 0.25), pg.SRCALPHA)
    self.build_rect = self.building_surface.get_rect(topleft=(self.width * 0.84, self.height * 0.74))
    self.building_surface.fill(self.hud_color)

    self.images = self.load_image()
    self.tiles = self.create_build_hud()

    self.selected_building = None



  def create_build_hud(self):
    render_pos = [self.width * 0.85 + 10, self.height * 0.75 + 10]
    object_width = (self.building_surface.get_width())/ 35 

    tiles = []

    for image_name, image in self.images.items():
      pos = render_pos.copy()
      image_tmp = image.copy()
      image_scale = self.scale_image(image_tmp, w=object_width)
      rect = image_scale.get_rect(topleft=pos)
      tiles.append(
        {
          "name": image_name,
          "icon": image_scale,
          "image": self.images[image_name],
          "rect": rect
        }
      )

      render_pos[0] += image_scale.get_width() + 10

    return tiles



  def update(self):
    mouse_pos = pg.mouse.get_pos()
    mouse_action = pg.mouse.get_pressed()

    if mouse_action[2]:
      self.selected_building = None

    for tile in self.tiles:
      if tile["rect"].collidepoint(mouse_pos):
        if mouse_action[0]:
          self.selected_building = tile



  def draw(self, screen):

    if self.selected_building is not None:
      img = self.selected_building["image"].copy()
      img.set_alpha(100)
      screen.blit(img, pg.mouse.get_pos())

    screen.blit(self.ressources_surface, (0, 0))
    screen.blit(self.building_surface, (self.width * 0.85, self.height * 0.75))

    for tile in self.tiles:
      screen.blit(tile["icon"], tile["rect"].topleft)

    # resssources
    pos = self.width - 650
    for ressource in self.resources.get_resources().items():
      draw_text(screen, ressource[1]["name"] + ": " + ressource[1]["total"].__str__(), 30, (255, 255, 255), (pos, 10))
      pos += 150



  def load_image(self):
    sawmill = pg.image.load("assets/building/sawmill.png")
    mine = pg.image.load("assets/building/mine.png")
    church = pg.image.load("assets/building/church.png")
    house = pg.image.load("assets/building/house.png")

    images = {
      "mine": mine,
      "sawmill": sawmill,
      "church": church,
      "house": house,
    }

    return images



  def scale_image(self, image, w=None, h=None):
    if (w == None) and (h == None):
      pass
    elif h == None:
      scale = w / image.get_width()
      h = scale * image.get_height()
      image = pg.transform.scale(image, (int(w), int(h)))
    elif w == None:
      scale = h / image.get_height()
      w = scale * image.get_width()
      image = pg.transform.scale(image, (int(w), int(h)))
    else:
      image = pg.transform.scale(image, (int(w), int(h)))

    return image