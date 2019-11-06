from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from assignment3.scene import Scene

ESCAPE = '\033'
window = 0

scene = Scene(["./objects/ecube.obj"])
scene.init()


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
    global scene
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    # glTranslatef(0.0, -0.4, -3.0)
    # glRotatef(-40, 1.0, 0.0, 0.0)
    scene.render()
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


def special_key(key, x, y):
    global scene
    if key == GLUT_KEY_LEFT:
        scene.key_pressed('left')
    elif key == GLUT_KEY_RIGHT:
        scene.key_pressed('right')


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Elofin")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(special_key)
    InitGL(640, 480)
    glutMainLoop()


print("Hit ESC key to quit.")
print("Press left or right arrow keys to rotate around the y-axis.")
main()
