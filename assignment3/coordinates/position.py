from assignment3.coordinates.hcoordinates import HCoordinates


class Position(HCoordinates):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1
