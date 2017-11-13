from vector import Vector3


class Player:

    def __init__(self, camera, input):
        self.camera = camera
        self.input = input

        self.speed = 0.08
        self.velocity_y = 0
        self.gravity = 0.005
        self.grounded = False
        self.jump_height = 0.08

        self.camera_bounds = 1.1

    def update(self):
        self.update_movement()
        self.camera.updown(self.velocity_y)

    def update_movement(self):

        if self.camera.m_pos.z < -44:
            # NEED RE-RENDER MODELS!!!
            self.camera.set_position(Vector3(0, 1, 1), Vector3(0, 1, 0), Vector3(0, 1, 0)) # reset to defaults

        self.velocity_y -= self.gravity

        if self.camera.m_pos.y <= 1:
            self.grounded = True
            self.velocity_y = 0
            self.camera.m_pos.y = 1
            self.camera.m_view.y = 1

        if self.input.LEFT_KEY_PRESSED and self.camera.m_pos.x >= -self.camera_bounds:
            self.camera.strafe(-self.speed)

        if self.input.RIGHT_KEY_PRESSED and self.camera.m_pos.x <= self.camera_bounds:
            self.camera.strafe(self.speed)

        if self.input.UP_KEY_PRESSED:
            self.camera.move(self.speed)

        if self.input.DOWN_KEY_PRESSED:
            self.camera.move(-self.speed)

        if self.input.SPACE_KEY_PRESSED:
            if self.grounded:
                self.velocity_y = self.jump_height
                self.grounded = False
        else:
            if self.velocity_y > self.jump_height:
                self.velocity_y = self.jump_height

