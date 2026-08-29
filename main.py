import pygame

from game.config import GAME_RES, RES
from game.game import TetrisGame
from audio.music import Music




def main() -> None:
    pygame.init()
    pygame.mixer.init()

    music = Music()
    music.set_volume(1)
    music.play()

    screen = pygame.display.set_mode(RES)
    game_surface = pygame.Surface(GAME_RES)

    game = TetrisGame(screen, game_surface)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
