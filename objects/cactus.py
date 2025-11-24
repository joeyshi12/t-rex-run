import pygame


class Cactus:
    WIDTH: int = 24
    HEIGHT: int = 50
    COLOUR: tuple = (0, 0, 0)
    SPRITE_RECT: pygame.Rect = pygame.Rect(332, 2, 24, 50)

    def __init__(self, screen: pygame.Surface, spritesheet: pygame.Surface):
        self._screen = screen
        self._spritesheet = spritesheet
        self._x = screen.get_width() + self.SPRITE_RECT.width
        self._y = screen.get_height() - 110
        self.collider = pygame.Rect(self._x + 2, self._y + 5, 20, 40)

    def update(self):
        self._x -= 5
        self.collider.x -= 5

    def draw(self):
        # pygame.draw.rect(self._screen, pygame.Color("green"), self.collider)
        self._screen.blit(self._spritesheet, (self._x, self._y), self.SPRITE_RECT)

    def is_out_of_bounds(self):
        return self._x < -self.WIDTH