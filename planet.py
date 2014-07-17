import collections

class Planet:
    def __init__(self, a_diameter = 1275632):
        self.__diameter = a_diameter
        self.__distance = 1 #in AU

    def get_diameter(self):
        return self.__diameter
    diameter = property(get_diameter)

    def get_distance(self):
        return self.__distance
    distance = property(get_distance)
        
