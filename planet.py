import collections

class Planet:
    def __init__(self, a_diameter = 1275632, a_mass = 5.974e24):
        self.diameter = a_diameter
        self.mass = a_mass #in kg
        self.surfaceMap = None

class PlanetFactory:
    #3254473

    def create_earth():
        return Planet(12756.32,5.974e24)
    create_earth = staticmethod(create_earth)

    def create_mercury():
        return Planet(4879.400,3.301e23)
    create_mercury = staticmethod(create_mercury)        

    def create_venus():
        return Planet(12103.600,4.869e24)
    create_venus = staticmethod(create_venus)        

    def create_mars():
        return Planet(6792.400, 6.418e23)
    create_mars = staticmethod(create_mars)

    def create_jupiter():
        return Planet(1.42984e8, 1.899e27)
    create_jupiter = staticmethod(create_jupiter)

    def create_saturn():
        return Planet(120536, 5.685e24) 
    create_saturn = staticmethod(create_saturn)

    def create_neptun():
        return Planet(49528, 1.0243e26)
    create_neptun = staticmethod(create_neptun)

    def create_uranus():
        return Planet(51118, 8.683e25)
    create_uranus = staticmethod(create_uranus)
