from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from camera import Camera
from model_loader import *
from vector import Vector3
from input import Input
from player import Player


import sys

class Game:

    def __init__(self):
        self.camera = Camera()
        self.input = Input()
        self.player = Player(self.camera, self.input)
        self.objects = []

    def init_gl(self):

        glClearColor(0, 0, 0, 1)
        glClearDepth(1)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glShadeModel(GL_SMOOTH)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

        # init camera
        self.camera.set_position(Vector3(0, 1, 1), Vector3(0, 1, 0), Vector3(0, 1, 0))

        # load models
        test_model = OBJ("models/road.obj")
        self.objects.append(test_model)

    def create_cube(self, x, y, z, w_x=1, w_y=1, w_z=1):
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(w_x, w_y, w_z)
        glBegin(GL_QUADS)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)

        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)

        glEnd()
        glPopMatrix()

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

        # draw_grid()

        glPushMatrix()
        glScalef(0.1, 0.1, 0.1)
        glTranslatef(1, 0, -30)
        glRotatef(-90, 0, 1, 0)

        for obj in self.objects:
            glCallList(obj.gl_list)

        glPopMatrix()

        self.player.update()

        glutSwapBuffers()
        glutPostRedisplay()

    def draw_grid(self):
        glPushMatrix()
        for i in xrange(-100, 100, 1):
            glBegin(GL_LINES)
            glColor3ub(150, 190, 150)
            glVertex3f(-100, 0, i)
            glVertex3f(100, 0, i)
            glVertex3f(i, 0, -100)
            glVertex3f(i, 0, 100)
            glEnd()
        glPopMatrix()

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
        glutInitWindowSize(1024, 768)
        glutInitWindowPosition(450, 50)
        glutCreateWindow('Computer Graphics Game')
        glutDisplayFunc(self.display)

        glutKeyboardFunc(self.input.register_key_down)
        glutKeyboardUpFunc(self.input.register_key_up)

        glutReshapeFunc(self.reshape)
        self.init_gl()
        glutMainLoop()

if __name__ == "__main__":
    Game().run(sys.argv)