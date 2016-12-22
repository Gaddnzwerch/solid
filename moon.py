from stellarobject import *

class Moon(StellarObject):

    def __init__(self, a_diameter, a_mass):
        super().__init__(a_diameter, a_mass)

    def __str__(self):
        return _("Moon") + ": " + super().__str__()
