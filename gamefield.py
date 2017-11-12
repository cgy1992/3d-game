from gameobject import GameObject
from model_loader import *
from vector import Vector3

class GameField:

    def __init__(self):
        self.objects = []

    def init(self):
        bridge = GameObject().load(
            Vector3(0, -4.5, -5),
            Vector3(0.003, 0.003, 0.003),
            OBJ('models/bridge.obj')
        )

        self.add(bridge)

        return self

    def add(self, gameobject):
        self.objects.append(gameobject)

    def render(self):
        for obj in self.objects:
            obj.render()

