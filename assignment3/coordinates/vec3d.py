import math

from assignment3.coordinates.hcoordinates import HCoordinates


class Vec3d(HCoordinates):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0

    # vector operations
    def normalize_vector(self):
        length = self.calculateLength()
        result = Vec3d(self.x / length, self.y / length, self.z / length)
        return result

    def find_angle(self, vec):
        beta = self.dotProduct(vec) / (self.calculateLength() * vec.calculateLength())
        return math.acos(beta) * (180 / math.pi)  # acos returns in radian

    def cross_product(self, vec):
        result = Vec3d(
            self.y * vec.z - self.z * vec.y,
            self.z * vec.x - self.x * vec.z,
            self.x * vec.y - self.y * vec.x)
        return result