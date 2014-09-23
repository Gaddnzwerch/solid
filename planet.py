import collections

class Planet:
    def __init__(self, a_diameter = 1275632, a_mass = 5.974e24):
        self.__diameter = a_diameter
        self.__distance = 1 #in AU
        self.__mass = a_mass #in kg

    def get_diameter(self):
        return self.__diameter
    diameter = property(get_diameter)

    def get_distance(self):
        return self.__distance
    distance = property(get_distance)
        
    def get_mass(self):
        return self.__mass
    mass = property(get_mass)
