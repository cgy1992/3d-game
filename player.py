class Player:

    def __init__(self, camera, input):
        self.camera = camera
        self.input = input

        self.speed = 0.05

    def update(self):
        self.update_movement()

    def update_movement(self):
        if self.input.LEFT_KEY_PRESSED:
            self.camera.strafe(-self.speed)

        if self.input.RIGHT_KEY_PRESSED:
            self.camera.strafe(self.speed)

        if self.input.SPACE_KEY_PRESSED:
            self.camera.updown(0.05)
