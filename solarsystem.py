import orbit

class SolarSystem():
    def __init__(self,aSun):
        self.__sun = aSun
        self.__orbiter = []
        self.__planets = []

    def get_sun(self):
        return self.__sun
    sun = property(get_sun)

    def get_orbiter(self):
        return self.__orbiter
    orbiter = property(get_orbiter)

    def add_orbiting_object(self, a_orbiter, a_distance):
        #all objects are orbiting around the sun in a solar system
        self.__orbiter.append(orbit.Orbit(self.__sun, a_orbiter, a_distance))


    def get_planets(self):
        return self.__planets

    planets = property(get_planets)

    def add_planet(self, a_planet, a_distance):
        self.__planets.append(a_planet)
        self.__orbiter.append(orbit.Orbit(self.__sun, a_planet, a_distance))

    
