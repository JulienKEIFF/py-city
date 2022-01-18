import pygame as pg

class Resources:

  def __init__(self):
    self.resources = {
      "wood": {
        "name": "Bois",
        "total": 50
      },
      "rock":{
        "name": "Roche",
        "total": 50
      },
      "gold":{
        "name": "Or",
        "total": 50
      },
      "citizen": {
        "name": "Population",
        "total": 0
      }
    }

    self.costs = {
      "mine": {"wood": 10, "rock": 15, "citizen": 2},
      "sawmill": {"wood": 10, "rock": 5, "citizen": 2},
      "church": {"wood": 50, "rock": 75, "gold": 25, "citizen": 2},
      "house": {"wood": 10, "rock": 5, "gold": 5 },
      "road": {"wood": 1, "rock": 1},
    }

  def get_resources(self):
    return self.resources
  
  def get_cost(self, building):
    return self.costs[building]

  def get_all_cost(self):
    return self.costs

  def apply_cost_to_resource(self, building):
    for resource, cost in self.costs[building].items():
      self.resources[resource]["total"] -= cost

  def add_citizen(self, citizen_to_add):
    self.resources["citizen"]["total"] += citizen_to_add

  def is_affordable(self, building):
    affordable = True
    for resource, cost in self.costs[building].items():
      if cost > self.resources[resource]["total"]:
        affordable = False
    return affordable