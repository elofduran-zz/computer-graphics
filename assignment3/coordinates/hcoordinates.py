import math


class HCoordinates:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return 'HCoordinates(' + self.x + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'

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
