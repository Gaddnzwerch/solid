import orbit
from stellarobject import StellarObject

from random import randint

class Sun(StellarObject):
	def __init__(self, a_diameter, a_mass):	
		super().__init__(a_diameter, a_mass)

	def __str__(self):
		return _("Sun") + ": " + super().__str__()