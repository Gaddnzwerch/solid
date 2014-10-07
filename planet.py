import collections

class Planet:
    def __init__(self, a_diameter = 1275632, a_mass = 5.974e24):
        self.__diameter = a_diameter
        self.__mass = a_mass #in kg

    def get_diameter(self):
        return self.__diameter
    diameter = property(get_diameter)

    def get_mass(self):
        return self.__mass
    mass = property(get_mass)

class PlanetFactory:

    def create_earth():
        return Planet(1275632,5.974e24)
    create_earth = staticmethod(create_earth)

    def create_mercury():
        return Planet(4879400,3.301e23)
    create_mercury = staticmethod(create_mercury)        

    def create_venus():
        return Planet(12103600,4.869e24)
    create_venus = staticmethod(create_venus)        

    def create_mars():
        return Planet(6792400, 6.418e23)
    create_mars = staticmethod(create_mars)

    def create_jupiter():
        return Planet(1.42984e8, 1.899e27)
    create_jupiter = staticmethod(create_jupiter)

    def create_saturn():
        return Planet(120536, 5.685e24) 
    create_saturn = staticmethod(create_saturn)
