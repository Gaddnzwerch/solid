import unittest
import sun

class TestSun(unittest.TestCase): 
    def setUp(self):
        self.__sun = sun.Sun()

    def test_default_diameter(self):
        self.assertEqual(self.__sun.diameter, 1392684) 

    def test_add_orbiter(self):
        numberBeforeAdd = self.__sun.get_number_of_orbiters()
        self.__sun.add_orbiter(object(),1)
        self.assertEqual(self.__sun.get_number_of_orbiters(), numberBeforeAdd+1)
    
if __name__ == '__main__':
    unittest.main()
