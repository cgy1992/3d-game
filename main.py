from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from engine.mouse import Mouse
from engine.camera import Camera
from e_math.vector import Vector3

CAMERA_LEFT = False
CAMERA_RIGHT = False


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def keyPressed(key, x, y):
    global e_camera, delta_time, CAMERA_LEFT, CAMERA_RIGHT

    if key == 'a':
        CAMERA_LEFT = True
    elif key == 'd':
        CAMERA_RIGHT = True

    if key[0] == '\033':
        sys.exit()

def keyUpPressed(key, x, y):
    global e_camera, delta_time, CAMERA_LEFT, CAMERA_RIGHT

    if key == 'a':
        CAMERA_LEFT = False
    elif key == 'd':
        CAMERA_RIGHT = False

    if key[0] == '\033':
        sys.exit()


def DrawGLScene():

    global e_camera, CAMERA_LEFT, CAMERA_RIGHT, delta_time

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    gluLookAt(
        e_camera.m_pos.x, e_camera.m_pos.y, e_camera.m_pos.z,
        e_camera.m_view.x, e_camera.m_view.y, e_camera.m_view.z,
        e_camera.m_up.x, e_camera.m_up.y, e_camera.m_up.z
    )

    if CAMERA_LEFT:
        e_camera.strafe(-0.03 * delta_time)

    if CAMERA_RIGHT:
        e_camera.strafe(0.03 * delta_time)

    draw_grid()
    glTranslatef(0, 1.0, 0)

    # Draw Cube (multiple quads)
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

    glutSwapBuffers()


def draw_grid():
    for i in xrange(-500, 500, 5):
        glBegin(GL_LINES)
        glColor3ub(150, 190, 150)
        glVertex3f(-500, 0, i)
        glVertex3f(500, 0, i)
        glVertex3f(i, 0, -500)
        glVertex3f(i, 0, 500)
        glEnd()


frame_count = 0
current_time = 0
prev_time = 0
fps = 0
delta_time = 0


def calculate_fps():
    global frame_count, current_time, prev_time, fps, delta_time
    frame_count += 1
    current_time = glutGet(GLUT_ELAPSED_TIME)
    time_interval = current_time - prev_time
    if time_interval > 1000:
        delta_time = time_interval / 1000.
        fps = frame_count / delta_time
        prev_time = current_time
        frame_count = 0

def idle_func():
    global fps, delta_time
    calculate_fps()
    glutPostRedisplay()


def main():
    global window, e_camera

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow('OpenGL Python Cube')

    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(idle_func)
    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUpPressed)

    e_camera = Camera()
    e_camera.set_position(Vector3(0, 2.5, 5), Vector3(0, 2.5, 0), Vector3(0, 1, 0))

    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()