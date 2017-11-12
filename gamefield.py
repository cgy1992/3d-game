from gameobject import GameObject
from model_loader import *
from vector import Vector3


class GameField:

    def __init__(self):
        self.objects = []

    def init(self):
        bridge = GameObject().load(
            Vector3(0, -4.5, -27),
            Vector3(0.003, 0.003, 0.003),
            OBJ('models/bridge.obj')
        )

        wall = GameObject().load(
            Vector3(-0.7, 0.45, -10),
            Vector3(0.05, 0.07, 0.05),
            OBJ('models/barrier_1.obj')
        )

        another_wall = GameObject().load(
            Vector3(1, 0.45, -10),
            Vector3(0.05, 0.07, 0.05),
            OBJ('models/barrier_1.obj')
        )

        wall.set_rotation(90, Vector3(0, 1, 0))
        another_wall.set_rotation(90, Vector3(0, 1, 0))

        self.add(bridge)
        self.add(wall)
        self.add(another_wall)

        return self

    def add(self, gameobject):
        self.objects.append(gameobject)

    def render(self):
        for obj in self.objects:
            obj.render()

