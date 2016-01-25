import collections
from random import randint

class Planet:
    def __init__(self, a_diameter = 1275632, a_mass = 5.974e24):
        self.diameter = a_diameter
        self.mass = a_mass #in kg
        self.surfaceMap = None

class PlanetFactory:
    @staticmethod
    def create():
        m_diameter = randint(4000, 1.42984e8)
        m_mass = randint(3.301e23, 1.899e27)
        return Planet(m_diameter, m_mass)

    @staticmethod
    def create_earth():
        return Planet(12756.32,5.974e24)

    @staticmethod
    def create_mercury():
        return Planet(4879.400,3.301e23)

    @staticmethod
    def create_venus():
        return Planet(12103.600,4.869e24)

    @staticmethod
    def create_mars():
        return Planet(6792.400, 6.418e23)

    @staticmethod
    def create_jupiter():
        return Planet(1.42984e8, 1.899e27)

    @staticmethod
    def create_saturn():
        return Planet(120536, 5.685e24) 

    @staticmethod
    def create_neptun():
        return Planet(49528, 1.0243e26)

    @staticmethod
    def create_uranus():
        return Planet(51118, 8.683e25)
