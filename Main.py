import pygame

from model.GameRun import GameRun

pygame.init()
pygame.display.set_caption('T-Rex Run')
clock = pygame.time.Clock()
display_width = 800
display_height = 500
display = pygame.display.set_mode((display_width, display_height))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_run.key_handle_down(event.key)
            if event.type == pygame.KEYUP:
                game_run.key_handle_up(event.key)
        game_run.render()
        game_run.update()
        pygame.display.update()
        clock.tick(100)


if __name__ == '__main__':
    game_run = GameRun(display)
    main()
