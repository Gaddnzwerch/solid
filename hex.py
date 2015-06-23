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



class FractionalHex:
    pass

class Map:
    pass

class Layout:
    pass


if __name__=="__main__":
    a = Hex(1,0)
    b = Hex(1,0,-1)
    assert(a == b)
    print(a + b)
    print(a - b)
    print(a * 5)
    print(a.length())
    print(a.distance(b))
    print(a.neighbor(7))
