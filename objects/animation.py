import pygame


class Animation:
    FRAME_DURATION = 5

    def __init__(self,
                 screen: pygame.Surface,
                 spritesheet: pygame.Surface,
                 states: dict[str, list[pygame.Rect]]):
        self._screen = screen
        self._spritesheet = spritesheet
        self._states = states
        self._current_state = next(iter(states))
        self._frame_index = 0
        self._frame_remaining_duration = self.FRAME_DURATION

    def set_state(self, state: str):
        if state not in self._states:
            raise ValueError(f"Invalid state: {state}")
        if state == self._current_state:
            return
        self._current_state = state
        self._frame_index = 0
        self._frame_remaining_duration = self.FRAME_DURATION

    def update(self):
        if self._frame_remaining_duration > 0:
            self._frame_remaining_duration -= 1
            return
        self._frame_index = (self._frame_index + 1) % len(self._states[self._current_state])
        self._frame_remaining_duration = self.FRAME_DURATION

    def draw(self, x: int, y: int):
        self._screen.blit(self._spritesheet, (x, y), self._states[self._current_state][self._frame_index])