# CENG 487 Assignment6 by
# Elif Duran
# StudentId: 230201002
# January 2020


import glfw
from OpenGL.GL import *
import pyrr

from scene import Scene
from shaderloader import ShaderLoader

scene = Scene()


def get_shader(object):
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    s = ShaderLoader()
    shader = s.compile_shader("shaders/vshader.vs", "shaders/fshader.fs")

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 192, object.pos_cols, GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, object.faces, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    return shader


def key_event(window, key, scancode, action, mods):
    if glfw.get_key(window, glfw.KEY_C):
        scene.key_pressed('cube')
    elif glfw.get_key(window, glfw.KEY_Q):
        scene.key_pressed('quad')
    elif glfw.get_key(window, glfw.KEY_P):
        scene.key_pressed('polygon')
    elif glfw.get_key(window, glfw.KEY_O):
        scene.key_pressed('polygon off')


def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    window = glfw.create_window(800, 600, "OpenGL Core Profile window", None, None)

    if not window:
        glfw.terminate()
        return

    # Enable key events
    glfw.set_input_mode(window, glfw.STICKY_KEYS, GL_TRUE)
    glfw.set_cursor_pos(window, 1024 / 2, 768 / 2)
    glfw.set_key_callback(window, key_event)

    glfw.make_context_current(window)

    while glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and not glfw.window_should_close(window):

        shader = get_shader(scene.obj)
        glUseProgram(shader)

        glClearColor(0.2, 0.3, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)

        if scene.obj.wireOnShaded:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())

        transformLoc = glGetUniformLocation(shader, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rot_x * rot_y)

        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    print("Hit 'q' to draw quad.")
    print("Hit 'c' to draw cube.")
    print("Hit 'p' to see polygon model.")
    print("Hit 'o' to off polygon model.")
    main()


