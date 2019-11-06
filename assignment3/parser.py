from assignment3.object import Object
from assignment3.coordinates.vec3d import Vec3d


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
                face_vertices = []

                for face in faces_line[1:]:
                    face = int(face)
                    face_vertices.append(vertices[face-1])
                faces.append(face_vertices)

        obj = Object(name, faces)
        return obj