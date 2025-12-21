import pygame
from abc import ABC
from objects.weapons.EnemyBall import EnemyBall
from config import LEVELS

myimage = pygame.image.load("objects/ships/ship.png")
width = 190
height = 140


class Ship(ABC):
    def __init__(self, surface, x, level, health, speed):
        self.surface = surface
        self.x =int(x)
        self.y = LEVELS[level][0]
        self.level = level
        self.sunk = False
        self.speed = speed
        self.health = health
        self.width = width * LEVELS[level][1]
        self.height = height * LEVELS[level][1]
        self.image = pygame.transform.scale(myimage, (self.width , self.height))
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        self.last_shot = 0
        self.shoot_delay = 1000

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


