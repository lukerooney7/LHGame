import random

import pygame
from abc import ABC
from objects.weapons.EnemyBall import EnemyBall
from config import LEVELS

class Ship(ABC):
    def __init__(self, surface, level, health, speed, shoot_delay, images, width, height):
        direction = -1 if level % 2 == 0 else 1

        self.surface = surface
        self.images = images
        self.level = level
        self.health = health
        self.speed = direction * speed
        self.shoot_delay = shoot_delay
        self.cannonballs = random.randint(0, 2)
        self.coins = random.randint(0, 10)
        self.x = 1000 if level % 2 == 0 else 0
        self.y = LEVELS[level][0]

        scale = LEVELS[level][1]
        self.width = int(width * scale)
        self.height = int(height * scale)

        self.rect = pygame.Rect(self.x, self.y - self.height, self.width, self.height)

        # Animation
        self.frame = 0
        self.last_frame_time = 0
        self.frame_delay = 300  # ms
        self.last_shot = 0

    def draw(self):
        if self.health <= 0:
            return

        now = pygame.time.get_ticks()
        if now - self.last_frame_time >= self.frame_delay:
            self.frame = (self.frame + 1) % 2
            self.last_frame_time = now

        image = self.images[self.health][self.frame]
        image = pygame.transform.scale(image, (self.width, self.height))

        if self.speed > 0:
            image = pygame.transform.flip(image, True, False)

        self.surface.blit(image, self.rect)

    def move(self):
        self.x += self.speed
        self.rect.bottomleft = (self.x, self.y)

    def hit(self):
        self.health -= 1

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay:
            self.last_shot = now
            return EnemyBall(self.surface, self.x + self.width // 2, self.level)
        return None
