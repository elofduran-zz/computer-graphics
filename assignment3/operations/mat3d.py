import math

from assignment3.coordinates.hcoordinates import HCoordinates
from assignment3.coordinates.vec3d import Vec3d


class Mat3d(object):

    def __init__(self, matrix):
        self.matrix = matrix

    # matrix operations
    def transpose(self):
        return [HCoordinates(self.matrix[0].x, self.matrix[1].x, self.matrix[2].x, self.matrix[3].x),
                HCoordinates(self.matrix[0].y, self.matrix[1].y, self.matrix[2].y, self.matrix[3].y),
                HCoordinates(self.matrix[0].z, self.matrix[1].z, self.matrix[2].z, self.matrix[3].z),
                HCoordinates(self.matrix[0].w, self.matrix[1].w, self.matrix[2].w, self.matrix[3].w)]

    def mat_multiplication(self, mat):
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*mat.matrix)] for X_row in self.matrix]
        return Mat3d(result)


    # todo: make it good
    def multiplyVector(self, vec3d):
        return Vec3d(
            self.matrix[0][0] * vec3d.x + self.matrix[0][1] * vec3d.y + self.matrix[0][2] * vec3d.z + self.matrix[0][3] * vec3d.w,
            self.matrix[1][0] * vec3d.x + self.matrix[1][1] * vec3d.y + self.matrix[1][2] * vec3d.z + self.matrix[1][3] * vec3d.w,
            self.matrix[2][0] * vec3d.x + self.matrix[2][1] * vec3d.y + self.matrix[2][2] * vec3d.z + self.matrix[2][3] * vec3d.w)

    @staticmethod
    def translation_matrix(vec):
        return Mat3d([(1, 0, 0, vec.x),
                      (0, 1, 0, vec.y),
                      (0, 0, 1, vec.z),
                      (0, 0, 0, 1)])

    def translate(self, vec):
        return self.mat_multiplication(vec.trasformation_matrix())  # it must be matrix multiplication

    @staticmethod
    def scaling_matrix(vec):
        return Mat3d([(vec.x, 0, 0, 0),
                      (0, vec.y, 0, 0),
                      (0, 0, vec.z, 0),
                      (0, 0, 0, 1)])

    def scale(self, vec):
        return self.mat_multiplication(vec.scaling_matrix)  # it must be matrix multiplication

    @staticmethod
    def rotate_x(angle):
        return Mat3d([(1, 0, 0, 0),
                      (0, math.cos(angle), -math.sin(angle), 0),
                      (0, math.sin(angle), math.cos(angle), 0),
                      (0, 0, 0, 1)])

    @staticmethod
    def rotate_y(angle):
        return Mat3d([(math.cos(angle), 0, math.sin(angle), 0),
                      (0, 1, 0, 0),
                      (-math.sin(angle), 0, math.cos(angle), 0),
                      (0, 0, 0, 1)])

    @staticmethod
    def rotate_z(angle):
        return Mat3d([(math.cos(angle), -math.sin(angle), 0, 0),
                      (math.sin(angle), math.cos(angle), 0, 0),
                      (0, 0, 1, 0),
                      (0, 0, 0, 1)])

    @staticmethod
    def identity_matrix():
        return Mat3d([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
