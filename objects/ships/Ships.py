import random
from objects.ships.Ship import Ship

class SmallShip(Ship):
    def __init__(self, surface, level):
        super().__init__(surface, level, health=1, speed=0.5, shoot_delay = random.randint(1900, 2100))

class MediumShip(Ship):
    def __init__(self, surface, level):
        super().__init__(surface, level, health=2, speed=0.3, shoot_delay = random.randint(3500, 4000))

class LargeShip(Ship):
    def __init__(self, surface, level):
        super().__init__(surface, level, health=3, speed=0.2, shoot_delay = random.randint(5500, 7000))
