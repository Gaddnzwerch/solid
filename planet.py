import collections
from stellarobject import *

class Planet(StellarObject):
    def __init__(self, a_diameter, a_mass):
        super().__init__(a_diameter, a_mass)
        self.surfaceMap = None
    def __str__(self):
        return _("Planet") + ": " + super().__str__()

class PlanetarySystem(StellarSystem):

    @property
    def moons(self):
        return self.orbiting_objects
