# CENG 487 Assignment6 by
# Elif Duran
# StudentId: 230201002
# January 2020


from hcoordinates import HCoordinates
from object import Cube, Quad


class Scene:

    def __init__(self):
        self.camera = HCoordinates(1.0, 1.0, -10.0, 1.0)
        self.obj = Cube()

    def key_pressed(self, key):
        if key == 'cube':
            cube = Cube()
            self.obj = cube
        elif key == 'quad':
            quad = Quad()
            self.obj = quad
        elif key == 'polygon':
            self.obj.wireOnShaded = True
        elif key == 'polygon off':
            self.obj.wireOnShaded = False


