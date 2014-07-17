class Orbit():
    def __init__(self, a_center, a_orbiter, a_distance):
        self.__center = a_center
        self.__orbiter = a_orbiter
        self.__distance = a_distance #in AU
    
    def get_center(self):
        return self.__center
    center = property(get_center)            
    
    def get_orbiter(self):
        return self.__orbiter
    orbiter = property(get_orbiter)

    def get_distance(self):
        return self.__distance
    distance = property(get_distance)
