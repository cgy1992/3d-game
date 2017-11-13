from gameobject import GameObject
from model_loader import *
from vector import Vector3
import math


class GameField:

    def __init__(self, player):
        self.objects = []
        self.aircraft_rot = 0
        self.player = player

    def init(self):
        bridge = GameObject().load(
            'bridge',
            Vector3(0, -4.5, -27),
            Vector3(0.003, 0.003, 0.003),
            OBJ('models/bridge.obj')
        )

        wall = GameObject().load(
            'wall',
            Vector3(-0.7, 0.45, -20),
            Vector3(0.05, 0.07, 0.05),
            OBJ('models/barrier_1.obj'),
            0.7
        )

        truck = GameObject().load(
            'truck',
            Vector3(0.7, 0.45, -5),
            Vector3(0.2, 0.2, 0.2),
            OBJ('models/Old_Truck.obj'),
            1.1
        )

        aircraft = GameObject().load(
            'aircraft',
            Vector3(0.4, 1, -35),
            Vector3(0.3, 0.3, 0.3),
            OBJ('models/aircraft.obj'),
            1
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

        for obj in self.objects:
            player_distance = self.player.camera.m_pos - obj.position # calc player distance to disable rendering objects
            m_dist = math.sqrt(player_distance.x * player_distance.x + player_distance.y * player_distance.y + player_distance.z * player_distance.z)

            if obj.name == 'aircraft':
                obj.set_rotation(self.aircraft_rot, Vector3(0, 1, 0))

            if obj.name not in ['bridge', 'bridge2']:
                if player_distance.z < -0.1 or player_distance.z > 15:
                    obj.hidden = True
                else:
                    obj.hidden = False

            # colission detection
            if m_dist < obj.collide_distance:
                print('collide with ' + obj.name)

            obj.render()

