from objects.ui.Bar import Bar

MAX_POWER = 100
MAX_HEALTH = 50

class UI:
    def __init__(self, surface):
        self.surface = surface
        self.power_bar = Bar(surface, MAX_POWER, 50)
        self.health_bar = Bar(surface, MAX_HEALTH, 650)

    def draw(self, power, health):
        self.power_bar.draw(power)
        self.health_bar.draw(health)