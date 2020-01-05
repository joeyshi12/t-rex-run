from pygame import image
from pygame.rect import Rect
from pygame.surface import Surface
import pygame


class TRex:
    GRAVITY: float = 0.2
    WIDTH: int = 50
    HEIGHT: int = 50
    SPRITE: image = pygame.transform.scale(pygame.image.load("image/t_rex_sprite.png"), (WIDTH, HEIGHT))

    jumping: bool = False
    dy: int

    def __init__(self, display: Surface):
        self.display = display
        self.rect = Rect((70, display.get_height() - 100), (self.WIDTH, self.HEIGHT))
        self.dy = 0

    def update(self):
        self.rect.y += self.dy
        self.rect.y = int(self.rect.y)
        self.dy += self.GRAVITY

        if self.on_ground():
            if self.jumping:
                self.dy = -5
            else:
                self.rect.y = self.display.get_height() - self.HEIGHT - 10
                self.dy = 0

    def on_ground(self):
        return self.rect.y > self.display.get_height() - self.HEIGHT - 10

    def draw(self):
        self.display.blit(self.SPRITE, self.rect)

