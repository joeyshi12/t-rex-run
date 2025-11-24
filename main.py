import pygame

from game_manager import GameManager

pygame.init()
pygame.display.set_caption("T-Rex Run")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 300))

spritesheet = pygame.image.load("assets/spritesheet.png")
game_manager = GameManager(screen, spritesheet)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_manager.handle_key_down(event.key)
            if event.type == pygame.KEYUP:
                game_manager.handle_key_up(event.key)
        game_manager.update()
        game_manager.draw()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
