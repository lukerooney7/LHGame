from objects.ships.Ship import Ship

class SmallShip(Ship):
    def __init__(self, surface, x, level,):
        super().__init__(surface, x, level, health=1, speed=-0.5)

class MediumShip(Ship):
    def __init__(self, surface, x, level,):
        super().__init__(surface, x, level, health=2, speed=-0.3)

class LargeShip(Ship):
    def __init__(self, surface, x, level, ):
        super().__init__(surface, x, level, health=3, speed=-0.2)
