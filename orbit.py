from math import sqrt, pi

class Orbit():
    def __init__(self, a_center, a_orbiter, a_semi_major_axis):
        self.__center = a_center
        self.__orbiter = a_orbiter
        self.semiMajorAxis = a_semi_major_axis
    
    def get_center(self):
        return self.__center
    center = property(get_center)            
    
    def get_orbiter(self):
        return self.__orbiter
    orbiter = property(get_orbiter)

    def get_reduced_mass(self):
        #reducedMass = (m1 * m2) / (m1 + m2)
        return (self.__center.mass * self.__orbiter.mass) / (self.__center.mass + self.__orbiter.mass)
    reducedMass = property(get_reduced_mass)
    
    def get_alpha(self):
        #alpha = G * m1 * m2
        m_gravitationConstant = 6.67384e-11        
        return m_gravitationConstant * self.__center.mass * self.__orbiter.mass
    alpha = property(get_alpha)

    def get_revolution_time(self):
        #time = sqr((4pi**2*semimajoraxis**3)/alpha)
        return sqrt(4* pi**2 * self.semiMajorAxis**3 / (6.67384e-11 * self.__center.mass))
    revolutionTime = property(get_revolution_time)
        
