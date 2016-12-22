from abc import ABCMeta, abstractmethod
from primitives import *

class IGraphicalRepresentation(metaclass=ABCMeta):
    
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def addPrimitives(self):
        pass

class SvgRepresentation(IGraphicalRepresentation):

    def __init__(self):
        self.start = "<svg>"
        self.representation = ""
        self.end = "</svg>"

    def display(self):
        print(self.start)
        print(self.representation)
        print(self.end)

    def addPrimitives(self, aListOfPrimitives):

        for lElement in aListOfPrimitives:
            pass

