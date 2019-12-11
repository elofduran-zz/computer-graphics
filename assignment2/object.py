# CENG 487 Assignment2 by
# Elif Duran
# StudentId: 230201002
# November 2019

import math
import random

from OpenGL.GL import *

from hcoordinates import HCoordinates, Vec3d
from mat3d import Mat3d


class Shape:

    def __init__(self, type, vertices, faces):
        self.type = type
        self.vertices = vertices
        self.faces = faces
        self.colors = []
        self.create_colors()

        self.operation = Mat3d()
        self.wireOnShaded = False
        self.wireWidth = 2
        self.wireOnShadedColor = HCoordinates(1.0, 1.0, 1.0, 1.0)

    def apply_operation(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = mat3d.multiply_vec(vertex)

    def apply_stack(self):
            self.apply_operation(self.matrix_stack)


    def create_colors(self):
        for i in range(len(self.faces)):
            self.colors.append(Vec3d(random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255))

    def draw(self):
        index = 0
        for face in self.faces:

            if self.wireOnShaded:
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                glLineWidth(self.wireWidth)

                glBegin(GL_POLYGON)
                glColor3f(self.wireOnShadedColor[0], self.wireOnShadedColor[1], self.wireOnShadedColor[2])
                for vertex in range(len(face)):
                    glVertex3f(self.vertices[vertex].x, self.vertices[vertex].y, self.vertices[vertex].z)
                glEnd()

                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

            else:
                glBegin(GL_POLYGON)
                if len(self.colors) > 0:
                    glColor3f(self.colors[index].x, self.colors[index].y, self.colors[index].z)
                else:
                    glColor3f(1.0, 2.0, 0.0)

                for vertex in face:
                    glVertex3f(self.vertices[vertex].x, self.vertices[vertex].y, self.vertices[vertex].z)
                glEnd()

            index += 1

            glLineWidth(2.5)
            glBegin(GL_LINE_LOOP)
            glColor3f(.3, .3, .3)
            for vertex in face:
                glVertex3f(self.vertices[vertex].x, self.vertices[vertex].y, self.vertices[vertex].z)
            glEnd()


class Cube(Shape):

    def __init__(self):
        vertices = [
            HCoordinates(1.0, -1.0, -1.0, 1.0),
            HCoordinates(1.0, -1.0, 1.0, 1.0),
            HCoordinates(-1.0, -1.0, 1.0, 1.0),
            HCoordinates(-1.0, -1.0, -1.0, 1.0),
            HCoordinates(1.0, 1.0, -1.0, 1.0),
            HCoordinates(1.0, 1.0, 1.0, 1.0),
            HCoordinates(-1.0, 1.0, 1.0, 1.0),
            HCoordinates(-1.0, 1.0, -1.0, 1.0)]

        faces = [
            [0, 1, 2, 3],
            [4, 7, 6, 5],
            [0, 4, 5, 1],
            [1, 5, 6, 2],
            [2, 6, 7, 3],
            [4, 0, 3, 7]]

        Shape.__init__(self, "CUBE", vertices, faces)


class Prism(Shape):

    def __init__(self, radius, height):
        self.type = "PRISM"
        self.radius = radius
        self.height = height
        self.num_slices = 3
        self.colors = []
        self.create_colors()

    def create_colors(self):
        for i in range(self.num_slices+20):
            self.colors.append(Vec3d(random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255))

    def draw(self):
        r = self.radius
        h = self.height
        n = float(self.num_slices)

        circle_pts = []
        for i in range(int(n) + 1):
            angle = 2 * math.pi * (i / n)
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            pt = (x, y)
            circle_pts.append(pt)

        a = 0
        glBegin(GL_TRIANGLE_FAN)  # drawing the back circle
        glColor3f(self.colors[a].x, self.colors[a].y, self.colors[a].z)
        a += 1
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
        glColor3f(self.colors[a].x, self.colors[a].y, self.colors[a].z)
        a += 1
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = -h / 2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)  # draw the tube
        for (x, y) in circle_pts:
            glColor3f(self.colors[a].x, self.colors[a].y, self.colors[a].z)
            z = h / 2.0
            glVertex(x, y, z)
            glVertex(x, y, -z)
            a += 1
        glEnd()


class Pyramid(Shape):

    def __init__(self):
        vertices = [
            HCoordinates(1.0, 0.0, 0.0, 1.0),
            HCoordinates(0.0, 1.0, 0.0, 1.0),
            HCoordinates(0.0, 0.0, 1.0, 1.0),
            HCoordinates(0.0, 0.0, -1.0, 1.0),
            HCoordinates(0.0, -1.0, 0.0, 1.0),
            HCoordinates(-1.0, 0.0, 0.0, 1.0)]

        faces = [
            [0, 1, 2],
            [0, 3, 2],
            [0, 2, 4],
            [0, 4, 3],
            [5, 3, 1],
            [5, 1, 3],
            [5, 4, 2],
            [5, 3, 4]]

        Shape.__init__(self, "PYRAMID", vertices, faces)


class Cylinder(Shape):

    def __init__(self, radius, half_length):
        self.type = "CYLINDER"
        self.radius = radius
        self.half_length = half_length
        self.num_slices = 9
        self.colors = []
        self.create_colors()

    def create_colors(self):
        for i in range(self.num_slices+20):
            self.colors.append(Vec3d(random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255))

    def draw(self):
        r = self.radius
        h = self.half_length
        n = self.num_slices

        circle_pts = []
        for i in range(int(n) + 1):
            angle = 2 * math.pi * (i / n)
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            pt = (x, y)
            circle_pts.append(pt)

        glBegin(GL_TRIANGLE_FAN)  # drawing the back circle
        a = 0
        glColor3f(self.colors[a].x, self.colors[a].y, self.colors[a].z)
        a += 1
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
        glColor3f(self.colors[a].x, self.colors[a].y, self.colors[a].z)
        a += 1
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = -h / 2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)  # draw the tube
        for (x, y) in circle_pts:
            glColor3f(self.colors[a].x, self.colors[a].y, self.colors[a].z)
            z = h / 2.0
            glVertex(x, y, z)
            glVertex(x, y, -z)
            a += 1
        glEnd()




