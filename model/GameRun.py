from pygame import image, Surface

from model.Cactus import Cactus
from model.TRex import TRex
import pygame


class GameRun:
    background: image

    def __init__(self, display: Surface):
        self.display = display
        self.t_rex = TRex(display)
        self.background = pygame.transform.scale(pygame.image.load("image/background.jpg").convert(),
                                                 (display.get_width(), display.get_height()))
        self.cactus = Cactus(display)

    def update(self):
        self.t_rex.update()
        self.cactus.update()
        if self.cactus.rect.x < -self.cactus.WIDTH:
            self.cactus.rect.x = self.display.get_width() + self.cactus.WIDTH

    def render(self):
        self.display.blit(self.background, (0, 0))
        self.t_rex.draw()
        self.cactus.draw()

    def key_handle_down(self, event):
        if event == pygame.K_SPACE:
            self.t_rex.jumping = True

    def key_handle_up(self, event):
        if event == pygame.K_SPACE:
            self.t_rex.jumping = False
