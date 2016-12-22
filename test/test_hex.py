import unittest
import hex
from view.graphical_representation import IGraphicalRepresentation

class TestHex(unittest.TestCase): 
    def setUp(self):
        self.hexA = hex.Hex(1,0)
        self.hexB = hex.Hex(2,1)

    def test_identity(self):
        self.assertEqual(self.hexA.q, 1)
        self.assertEqual(self.hexA.r, 0)

    def test_hex_add(self):
        hexC = self.hexA + self.hexB
        hexShould = hex.Hex(3,1)
        self.assertEqual(hexC, hexShould)

    def test_hex_sub(self):
        hexC = self.hexA - self.hexB
        hexShould = hex.Hex(-1,-1)
        self.assertEqual(hexC, hexShould)

    def test_hex_mul(self):
        hexC = self.hexA * 5
        hexShould = hex.Hex(5,0) 
        self.assertEqual(hexC, hexShould)

    def test_hex_distance(self):
        dist = self.hexA.distance(self.hexB)
        self.assertEqual(dist, 2)

    def test_hex_neighbor(self):
        hexNeighbor = self.hexA.neighbor(0)
        hexShould = hex.Hex(2,0)
        self.assertEqual(hexNeighbor, hexShould)

    def test_hex_interpolateLinear(self):
        self.assertEqual((self.hexA.interpolateLinear(self.hexB, 0).round()),self.hexA)
        self.assertEqual((self.hexA.interpolateLinear(self.hexB, 0.5).round()), hex.Hex(2,0))
        self.assertEqual((self.hexA.interpolateLinear(self.hexB, 1).round()),self.hexB)

    def test_line(self):
        line = self.hexA.line(self.hexB)
        self.assertEqual(len(line), 3)
        line = self.hexB.line(self.hexA)
        self.assertEqual(len(line), 3)
        self.assertEqual(line[0], self.hexB)
        self.assertEqual(line[2], self.hexA)
        line = self.hexA.line(self.hexA)
        self.assertEqual(len(line), 1)
        self.assertEqual(line[0], self.hexA)

    def test_map(self):
        testmap = hex.Map(10,10)
        self.assertEqual(testmap.size(), 100)


if __name__ == '__main__':
    unittest.main()
