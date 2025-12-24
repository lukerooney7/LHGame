import pygame

from objects.ui.Bar import Bar
from objects.user.user import MAX_HEALTH

MAX_POWER = 100


class UI:
    def __init__(self, surface, user):
        self.surface = surface
        self.power_bar = Bar(surface, MAX_POWER, 50)
        self.health_bar = Bar(surface, MAX_HEALTH, 650)
        self.user = user


    def draw(self, power):
        self.power_bar.draw(power)
        self.health_bar.draw(self.user.health)
        HUD_FONT = pygame.font.Font(None, 36)
        money_text = HUD_FONT.render(
            f"Money: ${self.user.coins}", True, (255, 215, 0)
        )

        cannonball_text = HUD_FONT.render(
            f"Cannonballs: {self.user.cannonballs}", True, (255, 255, 255)
        )

        self.surface.blit(money_text, (20, 20))
        self.surface.blit(cannonball_text, (20, 60))
