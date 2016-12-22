import unittest
import planet

class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.__planet = planet.Planet()

    def test_default_diameter(self):
        self.assertEqual(self.__planet.diameter,1275632)
    
    #TODO
    #def test_distance(self):
    #    self.assertEqual(self.__planet.distance, 1)

    def test_instance(self):
        self.assertIsInstance(self.__planet, planet.Planet)

if __name__ == "__main__":
    unittest.main()

