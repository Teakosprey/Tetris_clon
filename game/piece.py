from __future__ import annotations

from copy import deepcopy
from random import choice, randrange

import pygame

from .config import W

FIGURES_POS = [
    [(-1, 0), (-2, 0), (0, 0), (1, 0)],
    [(0, -1), (-1, -1), (-1, 0), (0, 0)],
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
    [(0, 0), (-1, 0), (0, 1), (-1, -1)],
    [(0, 0), (0, -1), (0, 1), (-1, -1)],
    [(0, 0), (0, -1), (0, 1), (1, -1)],
    [(0, 0), (0, -1), (0, 1), (-1, 0)],
]


class Piece:
    def __init__(self, cells, color):
        self.cells = cells
        self.color = color

    @classmethod
    def random(cls):
        pattern = choice(FIGURES_POS)
        cells = [pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in pattern]
        color = (randrange(30, 256), randrange(30, 256), randrange(30, 256))
        return cls(cells, color)

    def copy(self):
        return Piece(deepcopy(self.cells), self.color)

    def __iter__(self):
        return iter(self.cells)

    def rotate(self, center):
        rotated = []
        for rect in self.cells:
            x = rect.y - center.y
            y = rect.x - center.x
            rotated.append(
                pygame.Rect(center.x - x, center.y + y, 1, 1)
            )
        self.cells = rotated

    def move(self, dx, dy):
        for rect in self.cells:
            rect.x += dx
            rect.y += dy

    @property
    def x(self):
        return self.cells[0].x

    @property
    def y(self):
        return self.cells[0].y
