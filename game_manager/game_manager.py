import random

import pygame

from objects import TRex, Cactus, Score

pygame.mixer.init()


class GameManager:
    HIT_SOUND = pygame.mixer.Sound("assets/hit.ogg")
    _t_rex: TRex
    _cacti: list[Cactus]
    _ground: int
    _floor_scroll: int
    _is_over: bool

    def __init__(self,
                 screen: pygame.Surface,
                 spritesheet: pygame.Surface):
        self._screen = screen
        self._spritesheet = spritesheet
        self._ground = screen.get_height() - 70
        self._game_over_rect = pygame.Rect(484, 15, 190, 10)
        self._game_over_dest = ((screen.get_width() - self._game_over_rect.width) // 2, 120)
        self._score = Score(screen)
        self._reset_game()

    def update(self):
        if self._is_over:
            return
        self._t_rex.update()
        self._floor_scroll = (self._floor_scroll + 5) % self._spritesheet.get_width()
        self.remaining_cactus_spawn_time -= 1
        if self.remaining_cactus_spawn_time == 0:
            self._cacti.append(Cactus(self._screen, self._spritesheet))
            self._set_next_cactus_spawn_time()
        next_cacti: list[Cactus] = []
        for cactus in self._cacti:
            cactus.update()
            if not cactus.is_out_of_bounds():
                next_cacti.append(cactus)
            if self._t_rex.collider.colliderect(cactus.collider):
                self._t_rex.set_hurt()
                self._is_over = True
                self.HIT_SOUND.play()
        self._cacti = next_cacti
        self._score.update()

    def draw(self):
        self._screen.fill((255, 255, 255))
        self._draw_floor()
        for cactus in self._cacti:
            cactus.draw()
        self._t_rex.draw()
        if self._is_over:
            self._screen.blit(self._spritesheet, self._game_over_dest, self._game_over_rect)
        self._score.draw()

    def handle_key_down(self, event):
        if event == pygame.K_UP or event == pygame.K_SPACE:
            if self._is_over:
                self._reset_game()
                self._score.update_highscore()
                self._score.current_score = 0
            self._t_rex.is_jumping = True
        elif event == pygame.K_DOWN:
            self._t_rex.is_ducking = True

    def handle_key_up(self, event):
        if event == pygame.K_UP or event == pygame.K_SPACE:
            self._t_rex.is_jumping = False
        elif event == pygame.K_DOWN:
            self._t_rex.is_ducking = False

    def _draw_floor(self):
        if self._floor_scroll < self._spritesheet.get_width() - self._screen.get_width():
            self._screen.blit(
                self._spritesheet,
                (0, self._ground),
                pygame.Rect(2 + self._floor_scroll, 58, self._screen.get_width(), 20)
            )
        else:
            self._screen.blit(
                self._spritesheet,
                (0, self._ground),
                pygame.Rect(2 + self._floor_scroll, 58, self._screen.get_width(), 20)
            )
            overflow = self._floor_scroll - self._spritesheet.get_width() + self._screen.get_width()
            self._screen.blit(
                self._spritesheet,
                (self._screen.get_width() - overflow, self._ground),
                pygame.Rect(2, 58, overflow, 20)
            )

    def _set_next_cactus_spawn_time(self):
        self.remaining_cactus_spawn_time = random.randint(40, 100)

    def _reset_game(self):
        self._t_rex = TRex(self._screen, self._spritesheet)
        self._cacti = []
        self._set_next_cactus_spawn_time()
        self._floor_scroll = 0
        self._is_over = False