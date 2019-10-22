import math


class Vec3d:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0

    # vector operations

    def calculate_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def add(self, vec):
        result = Vec3d(self.x + vec.x, self.y + vec.y, self.z + vec.z)
        return result

    def scale(self, number):
        result = Vec3d(self.x * number, self.y * number, self.z * number)
        return result

    def normalize_vector(self):
        length = self.calculateLength()
        result = Vec3d(self.x / length, self.y / length, self.z / length)
        return result

    def find_angle(self, vec):
        beta = self.dotProduct(vec) / (self.calculateLength() * vec.calculateLength())
        return math.acos(beta) * (180 / math.pi)  # acos returns in radian

    def dot_product(self, vec2):
        return self.x * vec2.x + self.y * vec2.y + self.z * vec2.z

    def cross_product(self, vec):
        result = Vec3d(
            self.y * vec.z - self.z * vec.y,
            self.z * vec.x - self.x * vec.z,
            self.x * vec.y - self.y * vec.x)
        return result

    def calculate_projection(self):
        return

    # todo calculate it

    # printing a vector
    def __str__(self):
        return "Vector3d [x:" + str(self.x) + ", y:" + str(self.y) + ", z:" + str(self.z) + ", w:" + str(self.w) + "]"