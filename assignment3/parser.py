from assignment3.coordinates.hcoordinates import HCoordinates
from assignment3.object import Object
from assignment3.coordinates.vec3d import Vec3d


class Reading:

    @staticmethod
    def read_object(file_name):
        vertices = []
        faces = []
        file = open(file_name, "r")
        lines = file.readlines()
        for line in lines:
            if line.startswith("o"):
                name_lines = line.split()
                name = name_lines[1]
            elif line.startswith("v"):
                vertices_lines = line.split()
                vertex = Vec3d(vertices_lines[1], vertices_lines[2], vertices_lines[3])
                vertices.append(vertex)
            elif line.startswith("f"):
                faces_lines = line.split()
                face = HCoordinates(faces_lines[1], faces_lines[2], faces_lines[3], faces_lines[4])
                faces.append(face)

        obj = Object(name, vertices, faces)
        return obj