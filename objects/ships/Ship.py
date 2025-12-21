import pygame
from abc import ABC
from objects.weapons.EnemyBall import EnemyBall
from config import LEVELS

myimage = pygame.image.load("objects/ships/ship.png")
width = 190
height = 140

class Ship(ABC):
    def __init__(self, surface, level, health, speed, shoot_delay):
        direction = -1 if level % 2 == 0 else 1
        self.surface = surface
        self.x = 1000 if level % 2 == 0 else 0
        self.y = LEVELS[level][0]
        self.level = level
        self.sunk = False
        self.speed = direction * speed
        self.health = health
        self.width = width * LEVELS[level][1]
        self.height = height * LEVELS[level][1]
        self.image = pygame.transform.scale(myimage, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        if direction > 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.last_shot = 0
        self.shoot_delay = shoot_delay

    def draw(self):
        if self.health > 0:
            self.surface.blit(self.image, self.rect)

    def move(self):
        self.x += self.speed
        self.rect.bottomleft = (self.x, self.y)

    def hit(self):
        self.health -= 1

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay:
            self.last_shot = now
            return EnemyBall(self.surface, self.x + self.width/2, self.level)
        return None


