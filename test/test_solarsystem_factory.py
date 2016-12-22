import unittest
import control.solar_system_factory

class TestSolarsystemFactory(unittest.TestCase):
    
    def test_create_sol(self):
        solar_system_factory = control.solar_system_factory.SolarSystemFactory() 
        m_solar_system = solar_system_factory.create_sol()
        self.assertEqual(len(m_solar_system.planets),8)

