import orbit
from stellarobject import StellarObject

from random import randint

class Sun(StellarObject):
  #default is diameter of our sun
  def __init__(self, a_diameter = 1392684, a_mass = 1.989e30):
    super().__init__(a_diameter, a_mass)

  def __str__(self):
      return _("Sun") + ": " + super().__str__()

class SunFactory():
  
  @staticmethod
  def create():
      return Sun(randint(1e6,10e8), randint(1e24, 1e34))
