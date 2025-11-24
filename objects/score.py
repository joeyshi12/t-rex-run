import os

import pygame


class Score:
    FONT_COLOUR: tuple = (120, 120, 120)
    FONT_SIZE: int = 15
    HIGH_SCORE_FILE: str = "data/highscore.txt"
    current_score: int = 0
    high_score: int

    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        self.font = pygame.font.SysFont("lucidaconsole", self.FONT_SIZE)
        self.load()

    def update(self):
        self.current_score += 1

    def draw(self):
        high_score_render = self.font.render(f"High Score: {self.high_score // 4}", True, self.FONT_COLOUR)
        score_render = self.font.render(f"Score: {self.current_score // 4}", True, self.FONT_COLOUR)
        self._screen.blit(high_score_render, (10, 10))
        self._screen.blit(score_render, (10, 10 + self.FONT_SIZE))

    def update_highscore(self):
        with open(self.HIGH_SCORE_FILE, 'w') as file:
            self.high_score = max(self.current_score, self.high_score)
            file.write(str(self.high_score))

    def load(self):
        if not os.path.exists(self.HIGH_SCORE_FILE):
            self.high_score = 0
            return
        with open(self.HIGH_SCORE_FILE, 'r') as file:
            self.high_score = int(file.read())