import pygame as pg

class Resources:

  def __init__(self):
    self.resources = {
      "wood": {
        "name": "Bois",
        "total": 20
      },
      "rock":{
        "name": "Roche",
        "total": 20
      },
      "gold":{
        "name": "Or",
        "total": 20
      }
    }

    self.costs = {
      "sawmill": {"wood": 10, "rock": 5},
      "mine": {"wood": 10, "rock": 15}
    }

  def get_resources(self):
    return self.resources
  
  def get_cost(self, building):
    return self.costs[building]

  def apply_cost_to_resource(self, building):
    for resource, cost in self.costs[building].items():
      self.resources[resource]["total"] -= cost

  def is_affordable(self, building):
    affordable = True
    for resource, cost in self.costs[building].items():
      if cost > self.resources[resource]["total"]:
        affordable = False
    return affordable