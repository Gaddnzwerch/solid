import unittest
import orbit
import planet
import sun

class TestOrbit(unittest.TestCase):
    def setUp(self):
        self.__center = sun.Sun()
        self.__orbiter = planet.Planet()
        self.__orbit = orbit.Orbit(self.__center, self.__orbiter, 1.496e11)
        self.__orbit.eccentricity = 0.0167
        self.__orbit.epoch = 1 # in ticks

    def test_center(self):
        self.assertIsNotNone(self.__orbit.center) 
    
    def test_orbiter(self):
        self.assertIsNotNone(self.__orbit.orbiter)

    #necessary?
    def test_reduced_mass(self):
        self.assertEqual(self.__orbit.reducedMass, 5.973982057029257e24)

    def test_revolution_time(self):
        self.__orbit.semiMajorAxis = 1.496e11
        self.assertLessEqual(self.__orbit.revolutionTime, 31556000)
        self.assertGreaterEqual(self.__orbit.revolutionTime, 31555000)
        self.__orbit.semiMajorAxis = 1.0816e11
        self.assertLessEqual(self.__orbit.revolutionTime, 19399000)
        self.assertGreaterEqual(self.__orbit.revolutionTime, 19398000) 

if __name__ == '__main__': 
    unittest.main()
            
