# CENG 487 Assignment2 by
# Elif Duran
# StudentId: 230201002
# November 2019

from hcoordinates import HCoordinates
from object import Cube, Pyramid, Cylinder, Prism


class Scene:

    def __init__(self):
        self.camera = HCoordinates(1.0, 1.0, -10.0, 1.0)
        self.obj = None
        self.subdivision_level = 3

    def render(self):
        if self.obj is not None:
            self.obj.draw()
        else:
            pass

    def divide(self):
        if self.obj.type == "CUBE":
            self.subdivide(self.obj, self.subdivision_level)
        elif self.obj.type == "PRISM":
            self.obj.num_slices = self.subdivision_level
        elif self.obj.type == "CYLINDER":
            self.obj.num_slices = self.subdivision_level
        self.render()

    def key_pressed(self, key):
        if key == "cube":
            cube = Cube()
            self.obj = cube
        elif key == "pyramid":
            pyramid = Pyramid()
            self.obj = pyramid
        elif key == "prism":
            prism = Prism(1, 2)
            self.obj = prism
        elif key == "cylinder":
            cylinder = Cylinder(1, 2)
            self.obj = cylinder
        elif key == "increase" and self.subdivision_level < 10:
            self.subdivision_level += 1
            self.divide()
        elif key == "decrease" and self.subdivision_level > 3:
            self.subdivision_level -= 1
            self.divide()
        elif key == "reset":
            self.subdivision_level = 3
            self.divide()


    def subdivide(self, obj, subdivision_level):
        for i in range(subdivision_level - 1):
            obj.subdivide()
