import unittest
import sun

class TestSun(unittest.TestCase): 
    def setUp(self):
        self.__sun = sun.Sun()

    def test_default_diameter(self):
        self.assertEqual(self.__sun.diameter, 1392684) 
    
if __name__ == '__main__':
    unittest.main()
