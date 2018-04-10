import orbit 

class StellarObject():

	def __init__(self, a_diameter, a_mass):
		self.diameter = a_diameter #in km
		self.mass = a_mass #in t

	def __str__(self):
		return _('Mass: %s t, Diameter: %s km') % ("{:.2E}".format(self.mass), format(self.diameter))
		
	def __repr__(self):
		return str(self)
		

class StellarSystem():

	def __init__(self, a_center):
		self.center = a_center
		self.orbiter = []
		self.orbiting_objects = []

	def add_orbiting_object(self, a_orbiter, a_distance):
		#all objects are orbiting around the sun in a solar system
		self.orbiter.append(orbit.Orbit(self.center, a_orbiter, a_distance))
		self.orbiting_objects.append(a_orbiter)
		
	def __str__(self):
		l_descritption = _("This is a stellar system")
		l_descritption += "\n" 
		l_descritption += _("It's center is %s.") % (format(self.center))
		l_descritption += "\n" 
		l_descritption += _("There are %s planets revolving around the center:") % (format(len(self.orbiting_objects))) + "\n"
		
		for l_orbit in self.orbiter:
			l_descritption += " - " + str(l_orbit) + "\n"			
			
		return l_descritption