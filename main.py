# coding: utf-8

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from camera import Camera
from model_loader import *
from vector import Vector3
from input import Input
from player import Player
from gamefield import GameField

import sys

class Game:

    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 768

    def __init__(self):
        self.camera = Camera()
        self.input = Input()
        self.player = Player(self.camera, self.input)
        self.game_field = GameField(self.player)

    def init_gl(self):

        glClearColor(0.5, 0.5, 0.5, 1)
        glClearDepth(1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE) # нормали к единичной длине
        glDepthFunc(GL_LEQUAL)

        glShadeModel(GL_SMOOTH)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)



        # init light
        glEnable(GL_LIGHTING)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1])
        glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 1, 1])
        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 10)
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 100)

        # ambient
        #glEnable(GL_LIGHT1)
        #glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.5, 0.5, 0.5])
        #glLightfv(GL_LIGHT1, GL_POSITION, [1, 1, 0, 1])
        #glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 1)

        # init fog
        glFogi(GL_FOG_MODE, GL_EXP2)
        glFogfv(GL_FOG_COLOR, [0.5, 0.5, 0.5, 1])
        glFogf(GL_FOG_DENSITY, 0.15)
        glHint(GL_FOG_HINT, GL_FASTEST)
        glFogf(GL_FOG_START, 1.0)
        glFogf(GL_FOG_END, 5.0)
        glEnable(GL_FOG)

        # init camera
        self.camera.set_position(Vector3(0, 1, 1), Vector3(0, 1, 0), Vector3(0, 1, 0))

        # init game field
        self.game_field.init()



    # main render function
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()
        gluLookAt(
            self.camera.m_pos.x, self.camera.m_pos.y, self.camera.m_pos.z,
            self.camera.m_view.x, self.camera.m_view.y, self.camera.m_view.z,
            self.camera.m_up.x, self.camera.m_up.y, self.camera.m_up.z
        )

        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION,
                  [self.camera.m_pos.x, self.camera.m_pos.y - 2, self.camera.m_pos.z - 10])  # point light

        # 0, -4.5, -5, scale: 0.003

        self.player.update()
        self.game_field.render()

        glFinish()
        glutSwapBuffers()
        glutPostRedisplay()

    # reshaping window function
    def reshape(self, width, height):
        if height == 0:
            height = 1

        ratio = width / height
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, ratio, 0.1, 100.0)

    def run(self, argv):
        glutInit(argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
        glutInitWindowPosition(450, 50)
        glutCreateWindow('Computer Graphics Game')
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.input.register_key_down)
        glutKeyboardUpFunc(self.input.register_key_up)
        glutReshapeFunc(self.reshape)
        self.init_gl()
        print(glGetString(GL_VENDOR))
        glutMainLoop()


if __name__ == "__main__":
    Game().run(sys.argv)