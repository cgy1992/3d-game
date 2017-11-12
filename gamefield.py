from gameobject import GameObject
from model_loader import *
from vector import Vector3


class GameField:

    def __init__(self):
        self.objects = []
        self.aircraft_rot = 0

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

        truck = GameObject().load(
            Vector3(0.7, 0.45, -5),
            Vector3(0.2, 0.2, 0.2),
            OBJ('models/Old_Truck.obj')
        )

        aircraft = GameObject().load(
            Vector3(0.4, 1, -20),
            Vector3(0.3, 0.3, 0.3),
            OBJ('models/aircraft.obj')
        )

        wall.set_rotation(90, Vector3(0, 1, 0))

        truck.set_rotation(-15, Vector3(0, 1, 0))

        self.add(bridge)
        self.add(wall)
        self.add(truck)
        self.add(aircraft)

        return self

    def add(self, gameobject):
        self.objects.append(gameobject)

    def render(self):
        self.aircraft_rot += 1.5
        self.objects[3].set_rotation(self.aircraft_rot, Vector3(0,1,0))
        for obj in self.objects:
            obj.render()

