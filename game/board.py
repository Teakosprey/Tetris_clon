import pygame

from .config import H, W, TILE


class Board:
    def __init__(self):
        self.field = [[0 for _ in range(W)] for _ in range(H)]
        self.grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

    def reset(self):
        self.field = [[0 for _ in range(W)] for _ in range(H)]

    def collides(self, figure):
        for rect in figure:
            if rect.x < 0 or rect.x >= W:
                return True
            if rect.y >= H:
                return True
            if rect.y >= 0 and rect.y < H and self.field[rect.y][rect.x]:
                return True
        return False

    def merge_figure(self, figure, color):
        for rect in figure:
            if rect.y >= 0:
                self.field[rect.y][rect.x] = color

    def clear_lines(self):
        cleared = 0
        y = H - 1

        while y >= 0:
            if all(self.field[y]):
                self.field.pop(y)
                self.field.insert(0, [0 for _ in range(W)])
                cleared += 1
            else:
                y -= 1

        return cleared

    def is_game_over(self):
        return any(self.field[0])
