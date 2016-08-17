from abc import ABCMeta, abstractmethod

class IGraphicalRepresentation(metaclass=ABCMeta):
    
    @abstractmethod
    def display(self):
        pass

class SvgRepresentation(IGraphicalRepresentation):

    def display(self):
        pass
