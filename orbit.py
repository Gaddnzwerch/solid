from math import sqrt, pi

class Orbit():
	def __init__(self, a_center, a_orbiter, a_semi_major_axis):
		self.center = a_center
		self.orbiter = a_orbiter
		self.semiMajorAxis = a_semi_major_axis 
	
	@property
	def reducedMass(self):
		""" return the reduced mass calculated by the formula "reducedMass = (m1 * m2) / (m1 + m2) """
		return (self.center.mass * self.orbiter.mass) / (self.center.mass + self.orbiter.mass)	

	@property 
	def alpha(self):
		""" return the alpa value "alpha = G * m1 * m2" neccessary for various other calculations """
		m_gravitationConstant = 6.67384e-11        
		return m_gravitationConstant * self.center.mass * self.orbiter.mass	

	@property 
	def revolutionTime(self):
		""" return the revolutionTime in days "sqr((4pi**2*semimajoraxis**3)/alpha)" """		
		return sqrt(4* pi**2 * self.semiMajorAxis**3 / self.alpha)			

	def __str__(self):
		return _("%s is orbiting around %s in %s") % (format(self.orbiter), format(self.center), format(self.revolutionTime))
        
