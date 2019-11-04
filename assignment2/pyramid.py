import math
from OpenGL.GL import *


class Pyramid:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.num_slices = 3

    def draw_pyramid(self):
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

        glBegin(GL_TRIANGLE_FAN)  # drawing the back circle
        glColor(1, 0, 0)
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
        glColor(0, 0, 1)
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = -h / 2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)  # draw the tube
        glColor(0, 1, 0)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
            glVertex(x, y, -z)
        glEnd()

