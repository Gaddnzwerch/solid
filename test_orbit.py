import unittest
import orbit
import planet

class TestOrbit(unittest.TestCase):
    def setUp(self):
        self.__center = planet.Planet()
        self.__orbiter = planet.Planet()
        self.__orbit = orbit.Orbit(self.__center, self.__orbiter, 1)

    def test_center(self):
        self.assertIsNotNone(self.__orbit.center) 
    
    def test_orbiter(self):
        self.assertIsNotNone(self.__orbit.orbiter)

    def test_distance(self):
        self.assertEqual(self.__orbit.distance,1)

if __name__ == '__main__': 
    unittest.main()
            
