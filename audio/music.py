import pygame

from game.config import asset_path


class Music:
    def __init__(self):
        pygame.mixer.music.load(asset_path('theme.ogg'))

    def play(self):
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)