import unittest
import terrain
import control.surface_map_factory

class TestTerrain(unittest.TestCase):
    def setUp(self):
        self.__surfacemap = terrain.SurfaceMap(10,5)
        self.__water = terrain.Surface("Water", "blue")
        self.__earth = terrain.Surface("Earth", "brown")

    def test_surfacemap(self):
        self.assertEqual(self.__surfacemap.size(), 50)

    def test_surface(self):
        self.assertEqual(self.__water.name, "Water")
        self.assertEqual(self.__earth.name, "Earth")

    def test_surfacemapfactory(self):
        x = control.surface_map_factory.SurfaceMapFactory()
        x.addSurfacePercent(self.__water, 75)
        self.assertRaises(ValueError, x.addSurfacePercent, self.__earth, 100)
        x.addSurfacePercent(self.__earth, x.getFreeSurfacePercent())
        self.assertEqual(x.getFreeSurfacePercent(), 0)
        x.map = self.__surfacemap
        mMap = x.generateMap()
        self.assertIsInstance(mMap, terrain.SurfaceMap)
        relation = 0.0
        for percent in mMap.getSurfaceRelations().values():
            relation += percent
        self.assertEqual(relation, 100)
