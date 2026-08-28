import pygame

from game.config import GAME_RES, RES
from game.game import TetrisGame


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode(RES)
    game_surface = pygame.Surface(GAME_RES)

    game = TetrisGame(screen, game_surface)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
