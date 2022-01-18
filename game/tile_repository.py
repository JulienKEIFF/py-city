import pygame as pg

def load_images():
  mine = pg.image.load("assets/building/mine.png").convert_alpha()
  sawmill = pg.image.load("assets/building/sawmill.png").convert_alpha()
  church = pg.image.load("assets/building/church.png").convert_alpha()
  house = pg.image.load("assets/building/house.png").convert_alpha()
  grass = pg.image.load("assets/env/grass.png").convert_alpha()
  tree = pg.image.load("assets/env/tree.png").convert_alpha()
  rock = pg.image.load("assets/env/rock.png").convert_alpha()

  return {
    # Environement tiles
    "grass": grass, 
    "tree": tree, 
    "rock": rock,
    
    # Building tiles
    "mine": mine,
    "sawmill": sawmill,
    "church": church,
    "house": house,
  }