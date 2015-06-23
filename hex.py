# http://www.redblobgames.com/grids/hexagons/implementation.html
from math import sqrt, pi, cos, sin


class Hex:
    directions = None

    def __init__(self, q, r, s=None):
        if s == None:
            s = - q - r
        assert(q+r+s==0)
        self.q = q
        self.r = r
        self.s = s

    def __eq__(self, aOther):
        return self.q == aOther.q and self.r == aOther.r

    def __add__(self, aOther):
        return Hex(self.q + aOther.q, self.r + aOther.r, self.s + aOther.s)

    def __sub__(self, aOther):
        return Hex(self.q - aOther.q, self.r - aOther.r, self.s - aOther.s)

    def __mul__(self, aOther):
        return Hex(self.q * aOther, self.r * aOther, self.s * aOther)

    def __str__(self):
        return ("(" + format(self.q) + "," + format(self.r) + "," + format(self.s) + ")")

    def length(self):
        return int((abs(self.q) + abs(self.r) + abs(self.s)) / 2)

    def distance(self, aOther):
        return (self - aOther).length()

    def neighbor(self, aDirection):
        return self + self.direction(aDirection)

    @classmethod
    def direction(aCls, aDirection):
        if aCls.directions == None:
            aCls.directions = [Hex(1,0,-1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]
        aDirection %=  6
        return aCls.directions[aDirection]

class FractionalHex():
    #maybe subclass of Hex?
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s

    def round(self):
        q = int(round(self.q))
        r = int(round(self.r))
        s = int(round(self.s))
        q_diff = q - self.q
        r_diff = r - self.r
        s_diff = s - self.s
        
        if (q_diff > r_diff and q_diff > s_diff):
            q = -r -s
        elif (r_diff > s_diff):
            r = -q -s
        else:
            s = -q -r
        
        return Hex(q, r, s)



class Layout:
    def __init__(self, aOrientation, aSize, aOrigin):
        self.orientation = aOrientation
        self.size = aSize
        self.origin = aOrigin

    def hex_to_pixel(self, aHex):
        x = (self.orientation.f0 * aHex.q + self.orientation.f1 * aHex.r) * self.size.x
        y = (self.orientation.f2 * aHex.q + self.orientation.f3 * aHex.r) * self.size.y
        return Point(x + self.origin.x, y + self.origin.y)

    def pixel_to_hex(self, aPoint):
        point = Point((aPoint.x - self.origin.x) / self.size.x, (aPoint.y - self.origin.y) / self.size.y)
        q = self.layout.b0 * point.x + self.layout.b1 * point.y
        r = self.layout.b2 * point.x + self.layout.b3 * point.y
        return FractionalHex(q, r)

    def hex_corner_offset(self, aCorner):
        angle = 2.0 * pi * (aCorner + self.orientation.startAngle) / 6
        return Point(self.size.x * cos(angle), self.size.y * sin(angle))

    def polygon_corners(self, aHex):
        corners = []
        center = self.hex_to_pixel(aHex)
        for i in range(0,6):
            offset = self.hex_corner_offset(i)
            corners.append(Point(center.x + offset.x, center.y + offset.y))
        
        return corners

    """
    intrapolate a line between two hexes
    """
    def lerp(self, aHexA, aHexB, aT):
        return FractionalHex( aHexA.q + (aHexB.q - aHexA.q) * aT, aHexA.r + (aHexB.r - aHexB.r) * aT, aHexA.s + (aHexB.s - aHexA.s) * aT ) 

    """
    draw a line between two hexes by getting a list of hexes inbetween
    """
    def linedraw(self, aHexA, aHexB):
        n = aHexA.distance(aHexB)
        results = []
        
        if n < 1: 
            n = 1

        step = 1.0 / n
         
        i = 0
        while i <= n:
            results.append(self.lerp(aHexA,aHexB,step).round())
            i += 1

        return results
        


class Orientation:
    layout_pointy = None
    layout_flat = None

    def __init__(self, f0, f1, f2, f3, b0, b1, b2, b3, startAngle):
        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.startAngle = startAngle

    @classmethod
    def get_layout_pointy(aCls):
        if aCls.layout_pointy == None:
            aCls.layout_pointy = Orientation(sqrt(3.0), sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0, sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0, 0.5)
        return aCls.layout_pointy

    @classmethod
    def get_layout_flat(aCls):
        if aCls.layout_flat == None:
            aCls.layout_flat = Orientation(3.0 / 2.0, 0.0, sqrt(3.0) / 2.0, sqrt(3.0), 2.0 / 3.0, 0.0, -1.0 / 3.0, sqrt(3.0) / 3.0, 0.0)
        return aCls.layout_flat

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + format(self.x) + "," + format(self.y) + ")"

class Map:
    pass


if __name__=="__main__":
    a = Hex(1,0)
    b = Hex(1,0,-1)
    assert(a == b)
    print(a + b)
    print(a - b)
    b = a * 5
    print(a.length())
    print(a.distance(b))
    print(a.neighbor(7))
    l = Layout(Orientation.get_layout_flat(), Point(1,1), Point(0,0))
    print(l.hex_to_pixel(a))
    print(l.polygon_corners(a))
    print(l.linedraw(a,b))
