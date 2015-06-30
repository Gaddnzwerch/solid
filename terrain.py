from hex import Hex, Map

#==============================================================================
class Terrain(Hex):
    pass

#==============================================================================
class SurfaceMap(Map):
    pass

#==============================================================================
class SurfaceMapFactory():
    def __init__(self):
        self.surfaceRelations = {}
        self.__surfacePercent = 0
        self.map = None 

    @property
    def surfacePercent(self):
        return self.__surfacePercent
    @surfacePercent.setter
    def surfacePercent(self, aValue):
        if (aValue < 0) or (aValue > 100):
            raise ValueError("surfacePercent should be between 0 and 100")
        else:
            self.__surfacePercent = aValue

    def getFreeSurfacePercent(self):
        return 100 - self.__surfacePercent

    def addSurfacePercent(self, aSurface, aPercent):
        self.surfacePercent += aPercent
        self.surfaceRelations[aSurface] = aPercent

    def generateMap(self):
        aSurfaceMap = SurfaceMap(self.map.height, self.map.width)
        return aSurfaceMap

#==============================================================================
class Surface:
    def __init__(self, aName, aColour):
        self.name = aName
        self.colour = aColour
