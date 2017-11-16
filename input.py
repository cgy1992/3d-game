class Input:

    def __init__(self, game_field):
        self.LEFT_KEY_PRESSED = False
        self.RIGHT_KEY_PRESSED = False
        self.UP_KEY_PRESSED = False
        self.DOWN_KEY_PRESSED = False
        self.SPACE_KEY_PRESSED = False

        self.game_field = game_field

    def register_key_down(self, key, x, y):
        if key == 'w':
            self.UP_KEY_PRESSED = True
        if key == 's':
            self.DOWN_KEY_PRESSED = True
        if key == 'a':
            self.LEFT_KEY_PRESSED = True
        if key == 'd':
            self.RIGHT_KEY_PRESSED = True
        if ord(key) == 32:
            self.SPACE_KEY_PRESSED = True
        if key == 'f':
            self.game_field.set_parameter('fog')
        if key == 'l':
            self.game_field.set_parameter('light')
        if key == 'm':
            self.game_field.set_parameter('free_walk')

    def register_key_up(self, key, x, y):
        if key == 'w':
            self.UP_KEY_PRESSED = False
        if key == 's':
            self.DOWN_KEY_PRESSED = False
        if key == 'a':
            self.LEFT_KEY_PRESSED = False
        if key == 'd':
            self.RIGHT_KEY_PRESSED = False
        if ord(key) == 32:
            self.SPACE_KEY_PRESSED = False

