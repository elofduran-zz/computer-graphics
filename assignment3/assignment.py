from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from assignment3.parser import Reading

ESCAPE = '\033'
window = 0


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


def DrawGLScene():
    global obj
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    obj = Reading.read_object("./objects/ecube.obj")
    obj.draw()
    glutSwapBuffers()


def keyPressed(*argv):
    if argv[0] == b'\x1b':
        sys.exit()
    # elif argv[0] == b'p':
    #     bool_pyramid = True
    #     bool_cube = False
    # elif argv[0] == b'c':
    #     bool_cube = True
    #     bool_pyramid = False
    # if pyramid is not None:
    #     if argv[0] == b'a':
    #         pyramid.num_slices += 1
    #     elif argv[0] == b'e' and pyramid.num_slices > 2:
    #         pyramid.num_slices -= 1


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)

    window = glutCreateWindow("Elofin")
    glutDisplayFunc(DrawGLScene())
    glutFullScreen()
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()


print("Hit ESC key to quit.")
main()
