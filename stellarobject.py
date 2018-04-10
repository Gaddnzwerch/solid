import orbit 
import units
import logging

class StellarObject():

	def __init__(self, a_diameter, a_mass):
		meter = units.unit('m')		
		tons = units.unit('tonne')
		self.diameter = meter(a_diameter)
		self.mass = tons(a_mass) #in t

	def __str__(self):
		return _('Mass: %s, Diameter: %s') % (format(self.mass), format(self.diameter))
		
	def __repr__(self):
		return str(self)
		

class StellarSystem():

	def __init__(self, a_center):	
		self.center = a_center
		self.orbiter = []
		self.orbiting_objects = []
		au = units.unit('AU')
		self.minimum_distance = au(a_center.diameter * 1.1)
		self.maximum_distance = au(a_center.diameter * 8e4)
		
	def add_orbiting_object(self, a_orbiter, a_distance):
		#all objects are orbiting around the sun in a solar system	
		logging.debug(a_distance)
		au = units.unit('AU')
		l_distance = au(a_distance)
		logging.debug(l_distance)
		self.orbiter.append(orbit.Orbit(self.center, a_orbiter, l_distance))
		self.orbiting_objects.append(a_orbiter)
		self.minimum_distance = int((l_distance + a_orbiter.diameter) * 1.1)
		
	def __str__(self):
		l_descritption = _("This is a stellar system")
		l_descritption += "\n" 
		l_descritption += _("It's center is %s.") % (format(self.center))
		l_descritption += "\n" 
		l_descritption += _("There are %s planets revolving around the center:") % (format(len(self.orbiting_objects))) + "\n"
		
		for l_orbit in self.orbiter:
			l_descritption += " - " + str(l_orbit) + "\n"			
			
		return l_descritption