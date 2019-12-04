# CENG 487 Assignment2 by
# Elif Duran
# StudentId: 230201002
# November 2019

import math

from hcoordinates import HCoordinates


class Mat3d(object):

    def __init__(self, matrix  =None):
        if matrix == None:
            self.cols = [HCoordinates(1.0, 0.0, 0.0, 0.0), HCoordinates(0.0, 1.0, 0.0, 0.0),
                         HCoordinates(0.0, 0.0, 1.0, 0.0), HCoordinates(0.0, 0.0, 0.0, 1.0)]
            self.rows = self.get_rows()
        else:
            self.rows = [rows for rows in matrix]
            self.cols = self.get_cols()

    def get_rows(self):
        x = HCoordinates(self.cols[0].x, self.cols[1].x, self.cols[2].x, self.cols[3].x)
        y = HCoordinates(self.cols[0].y, self.cols[1].y, self.cols[2].y, self.cols[3].y)
        z = HCoordinates(self.cols[0].z, self.cols[1].z, self.cols[2].z, self.cols[3].z)
        w = HCoordinates(self.cols[0].w, self.cols[1].w, self.cols[2].w, self.cols[3].w)
        return [x, y, z, w]

    def get_cols(self):
        x = HCoordinates(self.rows[0].x, self.rows[1].x, self.rows[2].x, self.rows[3].x)
        y = HCoordinates(self.rows[0].y, self.rows[1].y, self.rows[2].y, self.rows[3].y)
        z = HCoordinates(self.rows[0].z, self.rows[1].z, self.rows[2].z, self.rows[3].z)
        w = HCoordinates(self.rows[0].w, self.rows[1].w, self.rows[2].w, self.rows[3].w)
        return [x, y, z, w]

    # matrix operations
    def transpose(self):
        return Mat3d(self.rows)

    def multiply_mat(self, mat):
        res = self.zero_list()
        i = 0
        for rows in self.rows:
            j = 0
            for cols in mat.cols:
                res[i][j] = rows.dot_product(cols)
                j += 1
            i += 1
        coord_matrix = []
        for rows in res:
            coord_matrix.append(HCoordinates(rows[0], rows[1], rows[2], rows[3]))

        return Mat3d(coord_matrix)

    def multiply_vec(self, vector):
        x = self.cols[0] * vector.x
        y = self.cols[1] * vector.y
        z = self.cols[2] * vector.z
        w = self.cols[3] * vector.w
        return x.add(y.add(z.add(w)))

    @staticmethod
    def translation_matrix(vec):
        return Mat3d([HCoordinates(1, 0, 0, vec.x),
                      HCoordinates(0, 1, 0, vec.y),
                      HCoordinates(0, 0, 1, vec.z),
                      HCoordinates(0, 0, 0, 1)])

    @staticmethod
    def scaling_matrix(scalar):
        return Mat3d([HCoordinates(scalar, 0, 0, 0),
                      HCoordinates(0, scalar, 0, 0),
                      HCoordinates(0, 0, scalar, 0),
                      HCoordinates(0, 0, 0, 1)])

    @staticmethod
    def rotate_x(angle):
        return Mat3d([HCoordinates(1, 0, 0, 0),
                      HCoordinates(0, math.cos(angle), -math.sin(angle), 0),
                      HCoordinates(0, math.sin(angle), math.cos(angle), 0),
                      HCoordinates(0, 0, 0, 1)])

    @staticmethod
    def rotate_y(angle):
        return Mat3d([HCoordinates(math.cos(angle), 0, math.sin(angle), 0),
                      HCoordinates(0, 1, 0, 0),
                      HCoordinates(-math.sin(angle), 0, math.cos(angle), 0),
                      HCoordinates(0, 0, 0, 1)])

    @staticmethod
    def rotate_z(angle):
        return Mat3d([HCoordinates(math.cos(angle), -math.sin(angle), 0, 0),
                      HCoordinates(math.sin(angle), math.cos(angle), 0, 0),
                      HCoordinates(0, 0, 1, 0),
                      HCoordinates(0, 0, 0, 1)])

    @staticmethod
    def identity_matrix():
        return Mat3d([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def zero_list():
        return [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
