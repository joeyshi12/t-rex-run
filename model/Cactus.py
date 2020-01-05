from pygame.rect import Rect
from pygame.surface import Surface
import pygame


class Cactus:
    WIDTH: int = 20
    HEIGHT: int = 50
    COLOUR: tuple = (0, 0, 0)
    DX: int = 5

    def __init__(self, display: Surface):
        self.display = display
        self.rect = Rect((display.get_width() + self.WIDTH, self.display.get_height() - self.HEIGHT - 20),
                         (self.WIDTH, self.HEIGHT))

    def update(self):
        self.rect.x -= self.DX

    def draw(self):
        pygame.draw.rect(self.display, self.COLOUR, self.rect)
