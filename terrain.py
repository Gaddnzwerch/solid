from hex import Hex, Map

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
class Surface:
    def __init__(self, aName, aColour):
        self.name = aName
        self.colour = aColour

    def __str__(self):
        return "" + self.name
