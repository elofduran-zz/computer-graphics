# CENG 487 Assignment4 by
# Elif Duran
# StudentId: 230201002
# December 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from camera import Camera
from defs import DrawStyle
from hcoordinates import Position, Vec3d
from scene import Scene
from view import Grid, View

ESCAPE = '\033'
window = 0

if len(sys.argv) < 2:
    input = "tori.obj"
else:
    input = sys.argv[1]
scene = Scene(input)
scene.init()

# create grid
grid = Grid("grid", 10, 10)
grid.setDrawStyle(DrawStyle.WIRE)
grid.setWireWidth(1)

# create camera
camera = Camera()
camera.createView( Position(0.0, 0.0, 10.0), \
                      Position(0.0, 0.0, 0.0), \
                      Vec3d(0.0, 1.0, 0.0) )
camera.setNear(1)
camera.setFar(1000)

# create View
view = View(camera, grid)

# init scene
view.setScene(scene)

# create objects
# cube1 = Cube("cube", 1, 1, 1, 10, 10, 10)
# cube1.Translate( 2, 0.5, 0)
# scene.add(cube1)
#
# cube2 = Cube("cube", 1.5, 1.5, 1.5, 10, 10, 10)
# cube2.Translate( -2, 0, 0)
# scene.add(cube2)

def main():
    global view
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow("CENG487 Assigment Template")

    # define callbacks
    glutDisplayFunc( view.draw )
    glutIdleFunc( view.idleFunction )
    glutReshapeFunc( view.resizeView )
    glutKeyboardFunc( view.keyPressed )
    glutSpecialFunc( view.specialKeyPressed )
    glutMouseFunc( view.mousePressed )
    glutMotionFunc( view.mouseMove )

    # Initialize our window
    width = 640
    height = 480
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LEQUAL)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    # glEnable(GL_LINE_SMOOTH)			# Enable line antialiasing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix

    # create the perpective projection
    gluPerspective( view.camera.fov, float(width ) /float(height), camera.near, camera.far )
    glMatrixMode(GL_MODELVIEW)

    # Start Event Processing Engine
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print ("Hit ESC key to quit.")
main()







# def main():
#     global window
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
#     glutInitWindowSize(640, 480)
#     glutInitWindowPosition(0, 0)
#     window = glutCreateWindow("Elofin")
#     glutDisplayFunc(DrawGLScene)
#     glutIdleFunc(DrawGLScene)
#     glutReshapeFunc(ReSizeGLScene)
#     glutKeyboardFunc(keyPressed)
#     glutSpecialFunc(special_key)
#     InitGL(640, 480)
#     glutMainLoop()
#
#
# print("Hit ESC key to quit.")
# print("Press 'a' to increase subdivision.")
# print("Press 'e' to decrease subdivision.")
# print("Press 'r' to reset subdivision.")
# main()
