import orbit

class Sun():
  #defaul is diameter of our sun
  def __init__(self, a_diameter = 1392684):
    self.__diameter = a_diameter # km

  def get_diameter(self):
    return self.__diameter
  diameter = property(get_diameter)
