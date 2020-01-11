# CENG 487 Assignment6 by
# Elif Duran
# StudentId: 230201002
# January 2020


import numpy


class Shape:

    def __init__(self, name, pos_cols, faces):
        self.name = name
        self.pos_cols = pos_cols
        self.faces = faces
        self.wireOnShaded = False


class Quad(Shape):
    def __init__(self):
        name = 'QUAD'

        pos_cols = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                    0.5, 0.5, 0.0, 0.0, 0.0, 1.0,
                    -0.5, 0.5, 0.0, 1.0, 1.0, 1.0]

        pos_cols = numpy.array(pos_cols, dtype=numpy.float32)

        faces = [0, 1, 2,
                 2, 3, 0]

        faces = numpy.array(faces, dtype=numpy.uint32)

        Shape.__init__(self, name, pos_cols, faces)


class Cube(Shape):
    def __init__(self):
        name = 'CUBE'

        pos_cols = [-0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.5, 0.0, 1.0, 0.0,
                    0.5, 0.5, 0.5, 0.0, 0.0, 1.0,
                    -0.5, 0.5, 0.5, 1.0, 1.0, 1.0,

                    -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
                    0.5, -0.5, -0.5, 0.0, 1.0, 0.0,
                    0.5, 0.5, -0.5, 0.0, 0.0, 1.0,
                    -0.5, 0.5, -0.5, 1.0, 1.0, 1.0]

        pos_cols = numpy.array(pos_cols, dtype=numpy.float32)

        faces = [0, 1, 2, 2, 3, 0,
                 4, 5, 6, 6, 7, 4,
                 4, 5, 1, 1, 0, 4,
                 6, 7, 3, 3, 2, 6,
                 5, 6, 2, 2, 1, 5,
                 7, 4, 0, 0, 3, 7]

        faces = numpy.array(faces, dtype=numpy.uint32)

        Shape.__init__(self, name, pos_cols, faces)
