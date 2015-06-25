import orbit

class Sun():
  #default is diameter of our sun
  def __init__(self, a_diameter = 1392684, a_mass = 1.989e30):
    self.__diameter = a_diameter # km
    self.__mass = a_mass # in kg

  def get_diameter(self):
    return self.__diameter
  diameter = property(get_diameter)
  
  def get_mass(self):
      return self.__mass
  mass = property(get_mass)
