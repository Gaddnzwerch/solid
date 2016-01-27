import unittest
import solarsystemfactory

class TestSolarsystemFactory(unittest.TestCase):
    
    def test_create_sol(self):
        solar_system_factory = solarsystemfactory.SolarSystemFactory() 
        m_solar_system = solar_system_factory.create_sol()
        self.assertEqual(len(m_solar_system.planets),8)

    def test_create_random(self):
        solar_system_factory = solarsystemfactory.SolarSystemFactory()
        m_solarsystem = solar_system_factory.create() 
        print()
        print(m_solarsystem.sun)

        for m_planetary_system in m_solarsystem.planets:
            print("Planet: " + format(m_planetary_system.center))

            for m_moon in m_planetary_system.moons:
                print("Moon: " + format(m_moon))

