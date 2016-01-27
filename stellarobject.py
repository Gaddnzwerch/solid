import orbit 

class StellarObject():

    def __init__(self, a_diameter, a_mass):
        self.diameter = a_diameter
        self.mass = a_mass 

    def __str__(self):
        return "Mass: " + format(self.mass) + " Diameter: " + format(self.diameter)

class StellarSystem():

    def __init__(self, a_center):
        self.center = a_center
        self.orbiter = []
        self.orbiting_objects = []


    def add_orbiting_object(self, a_orbiter, a_distance):
        #all objects are orbiting around the sun in a solar system
        self.orbiter.append(orbit.Orbit(self.center, a_orbiter, a_distance))
        self.orbiting_objects.append(a_orbiter)

