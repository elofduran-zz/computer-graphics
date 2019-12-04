# CENG 487 Assignment2 by
# Elif Duran
# StudentId: 230201002
# November 2019

import math
import random
from functools import reduce


# Reference: https://rosettacode.org/wiki/Catmull%E2%80%93Clark_subdivision_surface#Python
from OpenGL.GL import *

from hcoordinates import HCoordinates, Vec3d
from mat3d import Mat3d


class Shape:

    def __init__(self, type, vertices, faces):
        self.type = type
        self.vertices = vertices
        self.faces = faces
        self.colors = []
        self.operation = Mat3d()
        self.wireOnShaded = False
        self.wireWidth = 2
        self.wireOnShadedColor = HCoordinates(1.0, 1.0, 1.0, 1.0)

    def apply_operation(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = mat3d.multiply_vec(vertex)

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
                    glColor3f(1.0, 2.6, 0.0)

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


    # face points are calculated for each face by computing the average of all vertices of the face
    def get_face_points(self):
        NUM_DIMENSIONS = 3
        # face_points will have one point for each face
        # face_points = []
        face_points = [reduce(lambda v1, v2: v1.add(v2), map(lambda idx: self.vertices[idx], face)) * (1.0 / len(face)) for
                      face in self.faces]

        # for curr_face in self.faces:
        #     face_point = Vec3d(0.0, 0.0, 0.0)
        #     for curr_point_index in curr_face:
        #         curr_point = self.vertices[curr_point_index]
        #         # add curr_point to face_point
        #         # will divide later
        #         for i in range(NUM_DIMENSIONS):
        #             f = face_point.get_index(i)
        #             f += curr_point.get_index(i)
        #     # divide by number of points for average
        #     num_points = len(curr_face)
        #     for i in range(NUM_DIMENSIONS):
        #         f = face_point.get_index(i)
        #         f /= num_points
        #     face_points.append(face_point)

        return face_points

    def get_edges_faces(self):
        """
        Get list of edges and the one or two adjacent faces in a list.
        also get center point of edge
        Each edge would be [pointnum_1, pointnum_2, facenum_1, facenum_2, center]
        """
        # will have [pointnum_1, pointnum_2, facenum]
        edges = []

        # get edges from each face
        for facenum in range(len(self.faces)):
            face = self.faces[facenum]
            num_points = len(face)
            # loop over index into face
            for pointindex in range(num_points):
                # if not last point then edge is curr point and next point
                if pointindex < num_points - 1:
                    pointnum_1 = face[pointindex]
                    pointnum_2 = face[pointindex + 1]
                else:
                    # for last point edge is curr point and first point
                    pointnum_1 = face[pointindex]
                    pointnum_2 = face[0]
                # order points in edge by lowest point number
                if pointnum_1 > pointnum_2:
                    temp = pointnum_1
                    pointnum_1 = pointnum_2
                    pointnum_2 = temp
                edges.append([pointnum_1, pointnum_2, facenum])

        # sort edges by pointnum_1, pointnum_2, facenum
        edges = sorted(edges)

        # merge edges with 2 adjacent faces
        merged_edges = []
        length = int(len(edges)/2)
        for edgeIndex in range(length):
            edge1 = edges[2 * edgeIndex]
            edge2 = edges[2 * edgeIndex - 1]
            merged_edges.append([edge1[0], edge1[1], edge1[2], edge2[2]])

        # add edge centers
        edges_centers = []

        for me in merged_edges:
            p1 = self.vertices[me[0]]
            p2 = self.vertices[me[1]]
            center_point = p1.calculate_center(p2)
            edges_centers.append(me + [center_point])

        return edges_centers

    def get_edge_points(self, edges_faces, face_points):
        """
        for each edge, an edge point is created which is the average
        between the center of the edge and the center of the segment made
        with the face points of the two adjacent faces.
        """
        edge_points = []
        for edge in edges_faces:
            # get center of edge
            cp = edge[4]
            # get center of two facepoints
            fp1 = face_points[edge[2]]
            # if not two faces just use one facepoint
            # should not happen for solid like a cube
            if edge[3] == None:
                fp2 = fp1
            else:
                fp2 = face_points[edge[3]]
            cfp = fp1.calculate_center(fp2)
            # get average between center of edge and
            # center of facepoints
            edge_point = cp.calculate_center(cfp)
            edge_points.append(edge_point)
        return edge_points

    def get_avg_face_points(self, face_points):
        """
        for each point calculate
        the average of the face points of the faces the point belongs to (avg_face_points)

        create a list of lists of two numbers [facepoint_sum, num_points] by going through the
        points in all the faces.
        then create the avg_face_points list of point by dividing point_sum (x, y, z) by num_points
        """

        # initialize list with [[0.0, 0.0, 0.0], 0]
        num_points = len(self.vertices)
        temp_points = []

        for pointnum in range(num_points):
            temp_points.append([Vec3d(0.0, 0.0, 0.0), 0])

        # loop through faces updating temp_points
        for facenum in range(len(self.faces)):
            for pointnum in self.faces[facenum]:
                temp_points[pointnum][0] = face_points[facenum].add(temp_points[pointnum][0])
                temp_points[pointnum][1] += 1

        # divide to create avg_face_points
        avg_face_points = []

        for tp in temp_points:
            if tp[1] == 0:
                tp[1] += 1.0
            avg_face_points.append(tp[0] * (1.0 / tp[1]))

        return avg_face_points

    def get_avg_mid_edges(self, edges_faces):
        """
        the average of the centers of edges the point belongs to (avg_mid_edges)
        create list with entry for each point
        each entry has two elements. one is a point that is the sum of the centers of the edges
        and the other is the number of edges. after going through all edges divide by
        number of edges.
        """

        # initialize list with [[0.0, 0.0, 0.0], 0]
        num_points = len(self.vertices)
        temp_points = []

        for pointnum in range(num_points):
            temp_points.append([Vec3d(0.0, 0.0, 0.0), 0])

        # go through edges_faces using center updating each point
        for edge in edges_faces:
            for pointnum in [edge[0], edge[1]]:
                temp_points[pointnum][0] = temp_points[pointnum][0].add(edge[4])
                temp_points[pointnum][1] += 1

        # divide out number of points to get average
        avg_mid_edges = []
        for tp in temp_points:
            if tp[1] == 0:
                tp[1] += 1.0
            avg_mid_edges.append(tp[0] * (1.0 / tp[1]))

        return avg_mid_edges

    def get_points_faces(self):
        # initialize list with 0
        num_points = len(self.vertices)
        points_faces = []

        for pointnum in range(num_points):
            points_faces.append(0)

        # loop through faces updating points_faces
        for facenum in range(len(self.faces)):
            for pointnum in self.faces[facenum]:
                points_faces[pointnum] += 1

        return points_faces

    def get_new_points(self, points_faces, avg_face_points, avg_mid_edges):
        """
        m1 = (n - 3) / n
        m2 = 1 / n
        m3 = 2 / n
        new_coords = (m1 * old_coords)
                   + (m2 * avg_face_points)
                   + (m3 * avg_mid_edges)
        """
        new_vertices = []
        vertices = self.vertices.copy()
        for pointnum in range(len(self.vertices)):
            n = points_faces[pointnum]
            m1 = (n - 3) / n
            m2 = 1 / n
            m3 = 2 / n
            new_coords = (vertices[pointnum].multiply_vec(m1)).add((avg_face_points[pointnum].scale(m2)).add(avg_mid_edges[pointnum].scale(m3)))
            new_vertices.append(Vec3d(new_coords.x, new_coords.y, new_coords.z))

        return new_vertices

    def switch_nums(self, point_nums):
        """
        Returns tuple of point numbers
        sorted least to most
        """
        if point_nums[0] < point_nums[1]:
            return point_nums
        else:
            return (point_nums[1], point_nums[0])

    def subdivide(self):
        # for each face, a face point is created which is the average of all the points of the face.
        # each entry in the returned list is a point (x, y, z).
        face_points = self.get_face_points()

        # get list of edges with 1 or 2 adjacent faces
        # [pointnum_1, pointnum_2, facenum_1, facenum_2, center] or
        # [pointnum_1, pointnum_2, facenum_1, None, center]
        edges_faces = self.get_edges_faces()

        # get edge points, a list of points
        edge_points = self.get_edge_points(edges_faces, face_points)

        # the average of the face points of the faces the point belongs to (avg_face_points)
        avg_face_points = self.get_avg_face_points(face_points)

        # the average of the centers of edges the point belongs to (avg_mid_edges)
        avg_mid_edges = self.get_avg_mid_edges(edges_faces)

        # how many faces a point belongs to
        points_faces = self.get_points_faces()

        """
        m1 = (n - 3) / n
        m2 = 1 / n
        m3 = 2 / n
        new_coords = (m1 * old_coords)
                   + (m2 * avg_face_points)
                   + (m3 * avg_mid_edges)
        """
        new_points = self.get_new_points(points_faces, avg_face_points, avg_mid_edges)

        """
        Then each face is replaced by new faces made with the new points,

        for a triangle face (a,b,c):
           (a, edge_point ab, face_point abc, edge_point ca)
           (b, edge_point bc, face_point abc, edge_point ab)
           (c, edge_point ca, face_point abc, edge_point bc)

        for a quad face (a,b,c,d):
           (a, edge_point ab, face_point abcd, edge_point da)
           (b, edge_point bc, face_point abcd, edge_point ab)
           (c, edge_point cd, face_point abcd, edge_point bc)
           (d, edge_point da, face_point abcd, edge_point cd)

        face_points is a list indexed by face number so that is
        easy to get.

        edge_points is a list indexed by the edge number
        which is an index into edges_faces.

        need to add face_points and edge points to
        new_points and get index into each.

        then create two new structures

        face_point_nums - list indexes by facenum
        whose value is the index into new_points

        edge_point num - dictionary with key (pointnum_1, pointnum_2)
        and value is index into new_points

        """

        # add face points to new_points
        face_point_nums = []

        # point num after next append to new_points
        next_pointnum = len(new_points)

        for face_point in face_points:
            new_points.append(face_point)
            face_point_nums.append(next_pointnum)
            next_pointnum += 1

        # add edge points to new_points
        edge_point_nums = dict()

        for edgenum in range(len(edges_faces)):
            pointnum_1 = edges_faces[edgenum][0]
            pointnum_2 = edges_faces[edgenum][1]
            edge_point = edge_points[edgenum]
            new_points.append(edge_point)
            edge_point_nums[(pointnum_1, pointnum_2)] = next_pointnum
            next_pointnum += 1

        # new_points now has the points to output. Need new
        # faces

        """
        just doing this case for now:

        for a quad face (a,b,c,d):
           (a, edge_point ab, face_point abcd, edge_point da)
           (b, edge_point bc, face_point abcd, edge_point ab)
           (c, edge_point cd, face_point abcd, edge_point bc)
           (d, edge_point da, face_point abcd, edge_point cd)

        new_faces will be a list of lists where the elements are like this:

        [pointnum_1, pointnum_2, pointnum_3, pointnum_4]

        """

        new_faces = []

        for oldfacenum in range(len(self.faces)):
            oldface = self.faces[oldfacenum]
            # 4 point face
            if len(oldface) == 4:
                a = oldface[0]
                b = oldface[1]
                c = oldface[2]
                d = oldface[3]
                face_point_abcd = face_point_nums[oldfacenum]
                edge_point_ab = edge_point_nums[self.switch_nums((a, b))]
                edge_point_da = edge_point_nums[self.switch_nums((d, a))]
                edge_point_bc = edge_point_nums[self.switch_nums((b, c))]
                edge_point_cd = edge_point_nums[self.switch_nums((c, d))]
                new_faces.append([a, edge_point_ab, face_point_abcd, edge_point_da])
                new_faces.append([b, edge_point_bc, face_point_abcd, edge_point_ab])
                new_faces.append([c, edge_point_cd, face_point_abcd, edge_point_bc])
                new_faces.append([d, edge_point_da, face_point_abcd, edge_point_cd])

        self.vertices = new_points
        self.faces = new_faces
        self.colors = []
        for i in range(0, len(new_faces) + 1):
            r = random.uniform(0, 1)
            g = random.uniform(0, 1)
            b = random.uniform(0, 1)
            self.colors.append(HCoordinates(r, g, b, 1.0))


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

class Prizma(Shape):

    def __init__(self, radius, height):
        self.type = "PRIZMA"
        self.radius = radius
        self.height = height
        self.num_slices = 3

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

        glLineWidth(2.5)
        glBegin(GL_LINE_LOOP)
        glColor3f(.3, .3, .3)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
            glVertex(x, y, -z)
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

        Shape.__init__(self, "PRIZMA", vertices, faces)

