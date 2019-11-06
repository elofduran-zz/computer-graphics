from assignment3.coordinates.position import Position
from assignment3.coordinates.vec3d import Vec3d
from assignment3.coordinates.hcoordinates import HCoordinates
from OpenGL.GL import *

from assignment3.operations.mat3d import Mat3d
from assignment3.operations.operations import Operations


class Object:

    def __init__(self, name, faces):
        self.name = name
        self.faces = faces
        self.operation = Operations(Position(0.0, 0.0, 0.0), Position(0.0, 0.0, 0.0), Position(1.0, 1.0, 1.0))

    def draw(self):
        translation = Mat3d.translation_matrix(Vec3d(0.0, 0.0, -10.0))
        matrix = translation.mat_multiplication(self.operation.last_matrix)
        for face in self.faces:
            vertex = [matrix.multiplyVector(vector) for vector in face]
            glBegin(GL_POLYGON)
            glColor3f(0.9, 0.2, 0.3)
            for v in vertex:
                glVertex3f(v.x, v.y, v.z)
            glEnd()

            glLineWidth(2.5)
            glBegin(GL_LINE_LOOP)
            glColor3f(.3, .3, .3)
            for v in vertex:
                glVertex3f(float(v.x), float(v.y), float(v.z))
            glEnd()

