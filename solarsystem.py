import orbit
from stellarobject import StellarSystem

class SolarSystem(StellarSystem):

    @property
    def sun(self):
        return self.center

    @property
    def planets(self):
        return self.orbiting_objects

    def add_planet(self, a_planet, a_distance):
        super().add_orbiting_object(a_planet, a_distance) 
