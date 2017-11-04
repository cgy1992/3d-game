class Mouse:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.button = 0
        self.state = 0

    def handle_motion(self, x, y):
        self.x = x
        self.y = y