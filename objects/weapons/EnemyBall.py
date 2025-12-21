from objects.weapons.CannonBall import CannonBall
from config import LEVELS

class EnemyBall(CannonBall):
    def __init__(self, surface, x, level):
        super().__init__(surface, x, LEVELS[level][0], level, 5, 1.01, 40 * LEVELS[level][1])