from terrain import SurfaceMap, Terrain
from random import sample


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
