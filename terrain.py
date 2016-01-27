from hex import Hex, Map
from random import sample

#==============================================================================
class Terrain(Hex):

    def __init__(self, q, r, aSurface):
        super().__init__(q,r) 
        self.surface = aSurface

    def __str__(self):
        aString = super().__str__()
        aString += self.surface.name
        return aString

#==============================================================================
class SurfaceMap(Map):

    def __init__(self, aHeight, aWidth):
        super().__init__(aHeight, aWidth)
        self.surfaces = {}

    def getSurfaceRelations(self):
        if len(self.surfaces) == 0:
            for terrain in self.map:
                try:
                    self.surfaces[terrain.surface].append(terrain)
                except KeyError as e:
                    self.surfaces[terrain.surface] = [] 
                    self.surfaces[terrain.surface].append(terrain)
        

        aRelation = {}
        for surface, list in self.surfaces.items():
            aRelation[surface] = (len(list) / self.size()) * 100

        return aRelation

#==============================================================================
class SurfaceMapFactory():
    def __init__(self):
        self.surfaceRelations = {}
        self.__surfacePercent = 0
        self.map = None 
        self.terrainPool = []

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
        aSize = aSurfaceMap.size()

        for surface, percent in self.surfaceRelations.items():
            i = 0
            while i < aSize * (percent / 100):
                self.terrainPool.append(surface)
                i += 1
        
        aNewMap = {}
        for hex in aSurfaceMap.map:
            aSurface = sample(self.terrainPool,1)
            terrain = Terrain(hex.r, hex.q, aSurface[0])
            aNewMap[terrain] = terrain

        aSurfaceMap.map = aNewMap

        return aSurfaceMap

#==============================================================================
class Surface:
    def __init__(self, aName, aColour):
        self.name = aName
        self.colour = aColour

    def __str__(self):
        return "" + self.name
