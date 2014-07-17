import orbit

class Sun():
  #defaul is diameter of our sun
  def __init__(self, a_diameter = 1392684):
    self.__diameter = a_diameter # km
    self.__orbiter = []

  def get_diameter(self):
    return self.__diameter
  diameter = property(get_diameter)

  def add_orbiter(self, a_orbiter, a_distance):
    self.__orbiter.append(orbit.Orbit(self,a_orbiter, a_distance))

  def get_number_of_orbiters(self):
    return len(self.__orbiter)
