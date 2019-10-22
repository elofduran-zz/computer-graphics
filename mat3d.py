import math

from vec3d import Vec3d


class Mat3d:

    def __init__(self, matrix):
        self.matrix = matrix

    # matrix operations
    def transpose(self):
        return [Vec3d(self.matrix[0].x, self.matrix[1].x, self.matrix[2].x, self.matrix[3].x),
                Vec3d(self.matrix[0].y, self.matrix[1].y, self.matrix[2].y, self.matrix[3].y),
                Vec3d(self.matrix[0].z, self.matrix[1].z, self.matrix[2].z, self.matrix[3].z),
                Vec3d(self.matrix[0].w, self.matrix[1].w, self.matrix[2].w, self.matrix[3].w)]

    def multiply(self, vec):
        return Vec3d(
            self.matrix[0].dotProduct(vec),
            self.matrix[1].dotProduct(vec),
            self.matrix[2].dotProduct(vec),
            self.matrix[3].dotProduct(vec))

    def translate(self, vec):
        return Mat3d([Vec3d(1, 0, 0, vec.x),
                      Vec3d(0, 1, 0, vec.y),
                      Vec3d(0, 0, 1, vec.z),
                      Vec3d(0, 0, 0, 1)])

    def scale(self, vec):
        return Mat3d([Vec3d(vec.x, 0, 0, 0),
                      Vec3d(0, vec.y, 0, 0),
                      Vec3d(0, 0, vec.z, 0),
                      Vec3d(0, 0, 0, 1)])

    def rotate_x(angle):
        return Mat3d([Vec3d(1, 0, 0, 0),
                      Vec3d(0, math.cos(angle), -math.sin(angle), 0),
                      Vec3d(0, math.sin(angle), math.cos(angle), 0),
                      Vec3d(0, 0, 0, 1)])

    def rotate_y(angle):
        return Mat3d([Vec3d(math.cos(angle), 0, math.sin(angle), 0),
                      Vec3d(0, 1, 0, 0),
                      Vec3d(-math.sin(angle), 0, math.cos(angle), 0),
                      Vec3d(0, 0, 0, 1)])

    def rotate_z(angle):
        return Mat3d([Vec3d(math.cos(angle), -math.sin(angle), 0, 0),
                      Vec3d(math.sin(angle), math.cos(angle), 0, 0),
                      Vec3d(0, 0, 1, 0),
                      Vec3d(0, 0, 0, 1)])