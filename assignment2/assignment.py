from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from assignment2.cube import Cube
from assignment2.pyramid import Pyramid

ESCAPE = '\033'
bool_pyramid = False
bool_cube = False
pyramid = Pyramid(1, 2)

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def keyPressed(*argv):
    global bool_pyramid, bool_cube
    if argv[0] == b'\x1b':
        sys.exit()
    elif argv[0] == b'p':
        bool_pyramid = True
        bool_cube = False
    elif argv[0] == b'c':
        bool_cube = True
        bool_pyramid = False
    if pyramid is not None:
        if argv[0] == b'a':
            pyramid.num_slices += 1
        elif argv[0] == b'e':
            pyramid.num_slices -= 1


def DrawGLScene():
    global bool_pyramid, bool_cube, pyramid
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glTranslatef(0.0, -0.4, -3.0)
    glRotatef(-40, 1.0, 0.0, 0.0)

    if bool_cube:
        Cube.draw_cube()  # Draw cube
    if bool_pyramid:
        pyramid.draw_pyramid()  # Draw pyramid
    glutSwapBuffers()


def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("CENG487 Template")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window.
    InitGL(640, 480)
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
print("Hit 'c' to draw a cube.")
print("Hit 'p' to draw a pyramid.")
print("Hit 'a' to increase pyramid's subdivisions.")
print("Hit 'e' to decrease pyramid's subdivisions.")

main()
