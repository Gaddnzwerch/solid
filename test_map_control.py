import unittest
import control.MapControl
from hex import Hex, Map
from primitives import Point

class TestMapControl(unittest.TestCase):

    def setUp(self):
        testmap = Map(10,10)
        self.mapControl = control.MapControl.MapControl(testmap)

        self.mapControl.start = Point(250,250)
        self.mapControl.sizeInPixel = Point(10,10)

    def test_map_control_display(self):
        lGraphicalRepresentation = self.mapControl.getGraphicalRepresentation()
        self.assertNotEqual(lGraphicalRepresentation, None)



