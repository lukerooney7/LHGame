import random
import pygame
from objects.ships.Ship import Ship


small = {
    1: [ pygame.image.load("images/ships/small1.png"), pygame.image.load("images/ships/small2.png")],
}
medium = {
    1: [pygame.image.load("images/ships/medium1.png"), pygame.image.load("images/ships/medium2.png")],
    2: [pygame.image.load("images/ships/medium1.png"), pygame.image.load("images/ships/medium2.png")],
}

large = {
    1: [pygame.image.load("images/ships/large1.png"), pygame.image.load("images/ships/large2.png")],
    2: [pygame.image.load("images/ships/large1.png"), pygame.image.load("images/ships/large2.png")],
    3: [pygame.image.load("images/ships/large1.png"), pygame.image.load("images/ships/large2.png")],
}

class SmallShip(Ship):
    def __init__(self, surface, level):
        super().__init__(
            surface,
            level,
            health=1,
            speed=0.5,
            shoot_delay = random.randint(1900, 2100),
            images = small,
            width=133,
            height=98
        )

class MediumShip(Ship):
    def __init__(self, surface, level):
        super().__init__(
            surface,
            level,
            health=2,
            speed=0.3,
            shoot_delay = random.randint(3500, 4000),
            images = medium,
            width=190,
            height=140
        )

class LargeShip(Ship):
    def __init__(self, surface, level):
        super().__init__(
            surface,
            level,
            health=3,
            speed=0.2,
            shoot_delay = random.randint(5500, 7000),
            images = large,
            width=285,
            height=210
        )
