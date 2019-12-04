# CENG 487 Assignment2 by
# Elif Duran
# StudentId: 230201002
# November 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from object import Cube, Prizma, Pyramid
from scene import Scene

ESCAPE = '\033'
scene = Scene()

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
    if argv[0] == b'\x1b':
        sys.exit()
    elif argv[0] == b'c':
        scene.key_pressed('cube')
    elif argv[0] == b'p':
        scene.key_pressed('prizma')
    elif argv[0] == b'y':
        scene.key_pressed('pyramid')
    elif argv[0] == b'a':
        scene.key_pressed('increase')
    elif argv[0] == b'e':
        scene.key_pressed('decrease')
    elif argv[0] == b'r':
        scene.key_pressed('reset')

def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glTranslatef(0.0, -0.4, -3.0)
    glRotatef(-40, 40.0, 00.0, 40.0)
    scene.render()
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
print("Hit 'p' to draw a prizma.")
print("Hit 'y' to draw a pyramid.")
print("Hit 'a' to increase pyramid's or cube's subdivisions.")
print("Hit 'e' to decrease pyramid's subdivisions.")
print("Hit 'r' to reset pyramid.")

main()
