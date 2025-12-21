import pygame
from abc import ABC

levels = {
    0: 500,
    1: 400,
    2: 320,
    3: 250,
    4: 190,
    5: 150
}

class CannonBall(ABC):
    def __init__(self, surface, x, y, level, speed, scale, size):
        self.surface = surface
        self.x = x
        self.y = y
        self.z = 1
        self.size = size
        self.level = level
        self.max_distance = levels[level]
        self.landed = False
        self.speed = speed
        self.scale = scale

    def hit(self):
        self.landed = True

    def move(self):
        self.y += self.speed
        if self.y < self.max_distance:
            self.landed = True
        self.size *= self.scale

    def draw(self):
        pygame.draw.circle(
            self.surface,
            (40, 50, 20),
            (self.x, self.y),
            self.size
        )
