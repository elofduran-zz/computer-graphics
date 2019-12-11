# CENG 487 Assignment3 by
# Elif Duran
# StudentId: 230201002
# November 2019


from hcoordinates import HCoordinates
from parser import Parser


class Scene:

    def __init__(self, file):
        self.camera = HCoordinates(1.0, 1.0, -10.0, 1.0)
        self.parser = Parser()
        self.file = file
        self.obj = self.init()
        self.subdivisionLevel = 1

    def init(self):
        obj = self.parser.read_object(self.file)
        return obj

    def render(self):
        self.obj.draw(self.camera)

    def key_pressed(self, key):
        if key == "increase" and self.subdivisionLevel < 5:
            self.subdivisionLevel += 1
            self.subdivide(self.subdivisionLevel)
            # self.obj.draw(self.camera)
        elif key == "decrease" and self.subdivisionLevel > 1:
            self.subdivisionLevel -= 1
            self.subdivide(self.subdivisionLevel)
            # self.obj.draw(self.camera)
        elif key == "reset":
            self.subdivisionLevel = 1
            self.subdivide(self.subdivisionLevel)
            # self.obj.draw(self.camera)

    def subdivide(self, subdivisionLevel):
        self.obj = self.init()
        for i in range(subdivisionLevel - 1):
            self.obj.subdivide()



