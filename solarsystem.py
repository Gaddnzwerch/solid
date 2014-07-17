import orbit

class SolarSystem():
    def __init__(self,aSun):
        self.__sun = aSun
        self.__orbiter = []

    def get_sun(self):
        return self.__sun
    sun = property(get_sun)

    def get_orbiter(self):
        return self.__orbiter
    orbiter = property(get_orbiter)

    def add_orbiting_object(self, a_orbiter, a_distance):
        #all objects are orbiting around the sun in a solar system
        self.__orbiter.append(orbit.Orbit(self.__sun, a_orbiter, a_distance))
