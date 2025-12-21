from objects.weapons.CannonBall import CannonBall


class PlayerBall(CannonBall):
    def __init__(self, surface, x, level):
        super().__init__(surface, x, 600, level, -5, 0.99, 40)