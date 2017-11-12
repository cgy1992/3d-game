from vector import Vector3

from OpenGL.GL import *

class GameObject:
    def __init__(self):
        self.position = Vector3(0, 0, 0)
        self.size = Vector3(0, 0, 0)
        self.object = None
        self.hidden = False

    def load(self, position, size, object):
        self.position = position
        self.size = size
        self.object = object
        return self

    def set_position(self, position):
        self.position = position

    def render(self):
        if not self.hidden:
            glPushMatrix()
            glTranslatef(self.position.x, self.position.y, self.position.z)
            glScalef(self.size.x, self.size.y, self.size.z)
            glCallList(self.object.gl_list)
            glPopMatrix()