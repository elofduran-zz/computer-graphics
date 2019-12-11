# CENG 487 Assignment4 by
# Elif Duran
# StudentId: 230201002
# December 2019

from hcoordinates import Vec3d
from object import Object


class Parser:

    @staticmethod
    def read_object(file_name):
        faces = []
        vertices = []
        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            if line.startswith("o"):
                name_line = line.split()
                name = name_line[1]
            elif line.startswith("v"):
                vertices_line = line.split()
                vertex = Vec3d(float(vertices_line[1]), float(vertices_line[2]), float(vertices_line[3]))
                vertices.append(vertex)
            elif line.startswith("f"):
                faces_line = line.split()
                face = [int(faces_line[1]), int(faces_line[2]), int(faces_line[3]), int(faces_line[4])]
                faces.append(face)

        obj = Object(name, vertices, faces)
        return obj