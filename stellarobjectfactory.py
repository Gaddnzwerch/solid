from sun import Sun
from planet import Planet 
from stellarobject import StellarSystem
from random import randint
import logging

class StellarSystemFactory():
	
	@staticmethod
	def create():
		# create center
		l_center = SunFactory.create()
		l_stellar_system = StellarSystem(l_center)
		
		# adding planets
		for i in range(randint(0,15)):
			l_stellar_system.add_orbiting_object(PlanetFactory.create(), i)
		
		logging.debug(_("Created") + " " + repr(l_stellar_system))
		logging.debug(str(l_stellar_system))		
		return l_stellar_system

class SunFactory():
  
	@staticmethod
	def create():
		return Sun(randint(1e6,10e8), randint(1e24, 1e34))
	
	@staticmethod
	def create_sol():
		return Sun(1392684, 1.989e30)		
		
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