import pygame

from objects.animation import Animation

pygame.mixer.init()


class TRex:
    GRAVITY: float = 0.65
    JUMP_VELOCITY: float = -10
    JUMP_SOUND: pygame.mixer.Sound = pygame.mixer.Sound("assets/press.ogg")

    def __init__(self, screen: pygame.Surface, spritesheet: pygame.Surface):
        self._screen = screen
        self._animation = Animation(screen, spritesheet, {
            "running": [
                pygame.Rect(765, 2, 44, 47),
                pygame.Rect(765 + 44, 2, 44, 47),
            ],
            "jumping": [
                pygame.Rect(677, 2, 44, 47),
            ],
            "ducking": [
                pygame.Rect(939, 2, 58, 47),
                pygame.Rect(998, 2, 58, 47),
            ],
            "hurt": [
                pygame.Rect(898, 2, 41, 47)
            ]
        })
        self._ground = screen.get_height() - 110
        self._x = 40
        self._y = self._ground
        self._dy = 0
        self._is_grounded = True
        self.is_jumping = False
        self.is_ducking = False
        self.collider = pygame.Rect(48, self._y + 5, 30, 35)

    def update(self):
        self._animation.update()
        if self._is_grounded:
            if self.is_jumping:
                self._is_grounded = False
                self._dy = self.JUMP_VELOCITY
                self._y = self._ground - 1
                self._animation.set_state("jumping")
                self.JUMP_SOUND.play()
            else:
                self._dy = 0
                self._y = self._ground
                self._update_ducking_animation()
        else:
            self._dy += self.GRAVITY
            self._y += self._dy
            if self._in_ground():
                self._is_grounded = True
                self._y = self._ground
                self._dy = 0
                self._update_ducking_animation()
        self.collider.y = self._y + 5

    def draw(self):
        # pygame.draw.rect(self._screen, pygame.Color("green"), self.collider)
        self._animation.draw(self._x, self._y)

    def set_hurt(self):
        self._animation.set_state("hurt")

    def _update_ducking_animation(self):
        if self.is_ducking:
            self._animation.set_state("ducking")
        else:
            self._animation.set_state("running")

    def _in_ground(self):
        return self._y > self._ground