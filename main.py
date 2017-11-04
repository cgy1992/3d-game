from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from camera import Camera
from vector import Vector3

import sys

pos_z = -10
camera = None

# init opengl additional settings
def init_gl():

    global camera

    glClearColor(0, 0, 0, 1)
    glClearDepth(1)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    # init camera
    camera = Camera()
    camera.set_position(Vector3(0, 2.5, 5), Vector3(0, 2.5, 0), Vector3(0, 1, 0))


def create_cube(x, y, z):

    glPushMatrix()
    glTranslatef(x, y, z)
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
def display():
    global pos_z, camera
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    gluLookAt(
        camera.m_pos.x, camera.m_pos.y, camera.m_pos.z,
        camera.m_view.x, camera.m_view.y, camera.m_view.z,
        camera.m_up.x, camera.m_up.y, camera.m_up.z
    )

    draw_grid()

    create_cube(0, 0, pos_z)
    create_cube(-3, 0, pos_z)

    glutSwapBuffers()
    glutPostRedisplay()


def draw_grid():
    glPushMatrix()
    for i in xrange(-500, 500, 5):
        glBegin(GL_LINES)
        glColor3ub(150, 190, 150)
        glVertex3f(-500, 0, i)
        glVertex3f(500, 0, i)
        glVertex3f(i, 0, -500)
        glVertex3f(i, 0, 500)
        glEnd()
    glPopMatrix()


# reshaping window function
def reshape(width, height):
    if height == 0:
        height = 1

    ratio = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, ratio, 0.1, 100.0)

def keyboard(key, x, y):
    global pos_z, camera
    if key == 'w':
        pos_z += 1
    if key == 's':
        pos_z -= 1
    if key == 'a':
        camera.strafe(-0.3)
    if key == 'd':
        camera.strafe(0.3)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutInitWindowPosition(450, 50)
    glutCreateWindow('Computer Graphics Game')
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    init_gl()
    glutMainLoop()

if __name__ == "__main__":
    main()