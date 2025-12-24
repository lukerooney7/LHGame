import pygame
from config import WINDOW_HEIGHT


class Bar:
    def __init__(self, surface, max_value, x):
        self.bar_width = 300
        self.bar_height = 20
        self.x = x
        self.y = WINDOW_HEIGHT - 50
        self.surface = surface
        self.max_value = max_value

    def draw(self, value):
        pygame.draw.rect(self.surface, (50, 50, 50), (self.x, self.y, self.bar_width, self.bar_height))
        fill_width = int((value / self.max_value) * self.bar_width)
        pygame.draw.rect(self.surface, (255, 0, 0), (self.x, self.y, fill_width, self.bar_height))
        pygame.draw.rect(self.surface, (255, 255, 255), (self.x, self.y, self.bar_width, self.bar_height), 2)


