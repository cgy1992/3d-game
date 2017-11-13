from vector import Vector3

from OpenGL.GL import *

class GameObject:
    def __init__(self):
        self.position = Vector3(0, 0, 0)
        self.size = Vector3(0, 0, 0)
        self.rot_angle = 0
        self.rot_coord = Vector3(0, 0, 0)
        self.object = None
        self.hidden = False
        self.name = ''
        self.collide_distance = 0

    def load(self, name, position, size, object, collide_distance=0):
        self.position = position
        self.size = size
        self.object = object
        self.name = name
        self.collide_distance = collide_distance
        return self

    def set_position(self, position):
        self.position = position

    def set_rotation(self, angle, coords):
        self.rot_angle = angle
        self.rot_coord = coords

    def render(self):
        if not self.hidden:
            glPushMatrix()
            glTranslatef(self.position.x, self.position.y, self.position.z)
            if self.rot_angle != 0:
                glRotatef(self.rot_angle, self.rot_coord.x, self.rot_coord.y, self.rot_coord.z)
            glScalef(self.size.x, self.size.y, self.size.z)
            glCallList(self.object.gl_list)
            glPopMatrix()