# CENG 487 Assignment1 by
# Elif Duran
# StudentId: 230201002
# October 2019

class Object:

    def __init__(self, vertices, positions, matrix_stack):
        self.vertices = vertices
        self.positions = positions
        self.matrix_stack = matrix_stack

    def apply_operation(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = mat3d.vector_multiplication(vertex)

    def apply_stack(self):
        for matrix in self.matrix_stack:
            self.apply_operation(matrix)


# Write an object class which hold information about vertices of an object and also the transformation matrix stack for
# Translation (T), Rotation Around X,Y,Z (RX, RY, RZ), and Scale (S). The class should also keep track of the order of
# transformation matrices like TRS, SRT, RTS.

# Then use those classes to transform the triangle and square around one of their vertices. You can wait for a key press
# to do rotation incrementally or wait for a certain elapsed time since last update and then update the scene.