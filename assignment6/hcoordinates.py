# CENG 487 Assignment6 by
# Elif Duran
# StudentId: 230201002
# January 2020


import math


class HCoordinates:

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
