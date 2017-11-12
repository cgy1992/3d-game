
class Player:

    def __init__(self, camera, input):
        self.camera = camera
        self.input = input

        self.speed = 0.05
        self.velocity_y = 0
        self.gravity = 0.005
        self.grounded = False

    def update(self):
        self.update_movement()
        self.camera.updown(self.velocity_y)

    def update_movement(self):

        self.velocity_y -= self.gravity

        if self.camera.m_pos.y <= 1:
            self.grounded = True
            self.velocity_y = 0
            self.camera.m_pos.y = 1
            self.camera.m_view.y = 1

        if self.input.LEFT_KEY_PRESSED:
            self.camera.strafe(-self.speed)

        if self.input.RIGHT_KEY_PRESSED:
            self.camera.strafe(self.speed)

        if self.input.UP_KEY_PRESSED:
            self.camera.move(self.speed)

        if self.input.DOWN_KEY_PRESSED:
            self.camera.move(-self.speed)

        if self.input.SPACE_KEY_PRESSED:
            if self.grounded:
                self.velocity_y = 0.1
                self.grounded = False
        else:
            if self.velocity_y > 0.1:
                self.velocity_y = 0.1

