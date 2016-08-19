#==============================================================================
class Point:
    """Helper class that represents a point with two coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + format(self.x) + "," + format(self.y) + ")"

#==============================================================================
class Line():
    """Helper class that represents a line with a start and an end point"""

    def __init__(self, aStart, aEnd):
        self.start = aStart
        self.end = aEnd

    def __str__(self):
        return "Line: " + format(self.start) + " - " + format(self.end)
