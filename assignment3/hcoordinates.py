# CENG 487 Assignment3 by
# Elif Duran
# StudentId: 230201002
# November 2019


import math


class HCoordinates(object):

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return 'HCoordinates(' + self.x + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'

    @staticmethod
    def list_to_coord(new_list):
        return HCoordinates(new_list[0], new_list[1], new_list[2], new_list[3])

    def calculate_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def add(self, coord):
        result = HCoordinates(self.x + coord.x, self.y + coord.y, self.z + coord.z, self.w + coord.w)
        return result

    def scale(self, number):
        result = HCoordinates(self.x * number, self.y * number, self.z * number, self.w * number)
        return result

    def dot_product(self, coord):
        return self.x * coord.x + self.y * coord.y + self.z * coord.z + self.w * coord.w

    def multiply_vec(self, num):
        return HCoordinates(self.x * num, self.y * num, self.z * num, self.w * num)

    def __mul__(self, scalar):
        return HCoordinates(scalar * self.x, scalar * self.y, scalar * self.z, self.w * scalar)

    def calculate_center(self, vec):
        x = (self.x + vec.x) / 2
        y = (self.y + vec.y) / 2
        z = (self.z + vec.z) / 2
        w = (self.z + vec.w) / 2
        return HCoordinates(x, y, z, w)

class Position(HCoordinates):
    def __init__(self, x, y, z):
        HCoordinates.__init__(self, x, y, z, 1.0)


class Vec3d(HCoordinates):
    def __init__(self, x, y, z):
        HCoordinates.__init__(self, x, y, z, 0.0)

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

    def calculate_center(self, vec):
        x = (self.x + vec.x) / 2
        y = (self.y + vec.y) / 2
        z = (self.z + vec.z) / 2
        return Vec3d(x, y, z)

    def multiply_vec(self, num):
        return Vec3d(self.x * num, self.y * num, self.z * num)

    def get_index(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif i == 2:
            return self.z

    def add(self, other):
        return Vec3d(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z)

    @staticmethod
    def calculate_midpoint(p1, p2):
        return [(p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2]
