from view.graphical_representation import SvgRepresentation
from hex import Map
from math import sqrt, pi, cos, sin


class MapControl():

    def __init__(self, aMap):
        self.map = aMap
        self.layout = None
        self.orientation = None
        self.start = None
        self.sizeInPixel = None

    def getGraphicalRepresentation(self): 
        if self.layout == None:
            self.layout = Layout(self.orientation, self.sizeInPixel, self.start)

        lines = [] 
        representation = SvgRepresentation()

    def convertHexToSetOfPrimitives(self, aHex):
        lines = aHex.polygon_outlines(aHex)


#==============================================================================
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
    
    def polygon_outlines(self, aHex):
        outlines = []
        firstPoint = None 
        startPoint = None
        endPoint = None

        for corner in self.polygon_corners(aHex):

            if firstPoint == None:
                firstPoint = corner
                startPoint = corner
            elif endPoint == None:
                endPoint = corner
                line = Line(startPoint, endPoint)
                outlines.add(line)
                startPoint = endPoint
                endPoint = None
        
        line = Line(firstPoint, startPoint)
        outlines.add(line)

            
            



#==============================================================================
class Orientation:
    """This class holds two different orientations to display maps with the pointy 
    side up or the flat side up.
    """
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
