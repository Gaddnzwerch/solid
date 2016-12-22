import unittest
import solarsystem
import sun
import orbit

class TestSolarSystem(unittest.TestCase):
    def setUp(self):
        self.__sun = (sun.Sun())
        self.__solarSystem = solarsystem.SolarSystem(self.__sun)

    def test_solarSystem_init(self):
        self.assertIsInstance(self.__solarSystem, solarsystem.SolarSystem)
        self.assertIs(self.__sun,self.__solarSystem.sun)         

    def test_adding_orbiter(self):
        mCountBeforeAdd = len(self.__solarSystem.orbiter)
        self.__solarSystem.add_orbiting_object(object(), 1)
        self.assertEqual(mCountBeforeAdd + 1, len(self.__solarSystem.orbiter)) 
