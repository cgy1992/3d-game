import math

class Camera:

    def __init__(self):
        self.m_pos = None
        self.m_view = None
        self.m_up = None

    def set_position(self, v_pos, v_view, v_up):
        self.m_pos = v_pos
        self.m_view = v_view
        self.m_up = v_up

    def strafe(self, speed):
        v_vector = self.get_view_vector()
        self.m_pos.x = self.m_pos.x + -v_vector.z * speed
        self.m_pos.z = self.m_pos.z + v_vector.x * speed
        self.m_view.x = self.m_view.x + -v_vector.z * speed
        self.m_view.z = self.m_view.z + v_vector.x * speed

    def move(self, speed):
        v_vector = self.get_view_vector()
        self.m_pos.x = self.m_pos.x + v_vector.x * speed
        self.m_pos.z = self.m_pos.z + v_vector.z * speed
        self.m_view.x = self.m_view.x + v_vector.x * speed
        self.m_view.z = self.m_view.z + v_vector.z * speed

    def updown(self, speed):
        self.m_pos.y += speed
        self.m_view.y += speed


    def get_view_vector(self):
        return self.m_view - self.m_pos