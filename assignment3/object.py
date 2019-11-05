from assignment3.coordinates.vec3d import Vec3d
from assignment3.coordinates.hcoordinates import HCoordinates
from OpenGL.GL import *


class Object:

    def __init__(self, name, vertices, faces):
        self.name = name
        self.vertices = vertices
        self.faces = faces
        self.new_vertices = Vec3d(0, 0, 0)
        self.matrix_stack = []

    def apply_operation(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.new_vertices[i] = mat3d.vector_multiplication(vertex)

    def apply_stack(self):
        for matrix in self.matrix_stack:
            self.apply_operation(matrix)

    def draw(self):
        for face in self.faces:
            glBegin(GL_POLYGON)
            glColor4f(float(face.x), float(face.y), float(face.z), float(face.w))
            for vertex in self.vertices:
                glVertex3f(float(vertex.x), float(vertex.y), float(vertex.z))
            glEnd()

            # glLineWidth(2.5)
            # glBegin(GL_LINE_LOOP)
            # glColor3f(.3, .3, .3)
            # for vertex in self.vertices:
            #     glVertex3f(float(vertex.x), float(vertex.y), float(vertex.z))
            # glEnd()

    def __str__(self):
        print("Name: " + str(self.name))
        print("Vertices: ")
        for vector in self.vertices:
            print(Vec3d.__str__(vector))
        print("Faces: ")
        for face in self.faces:
            print(HCoordinates.__str__(face))
