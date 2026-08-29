import pygame

from .board import Board
from .config import FPS, RECORD_PATH
from .piece import Piece
from .scoring import calculate_score
from render.renderer import Renderer


class TetrisGame:
    def __init__(self, screen, game_surface):
        self.screen = screen
        self.game_surface = game_surface
        self.board = Board()
        self.renderer = Renderer(screen, game_surface)
        self.clock = pygame.time.Clock()

        self.started = False
        self.game_over = False

        self.figure = Piece.random()
        self.next_figure = Piece.random()
        self.color = self.figure.color
        self.next_color = self.next_figure.color

        self.score = 0
        self.anim_count = 0
        self.anim_speed = 60
        self.anim_limit = 2000
        self.record = self.get_record()

    def reset_game(self):
        self.board.reset()
        self.figure = Piece.random()
        self.next_figure = Piece.random()
        self.color = self.figure.color
        self.next_color = self.next_figure.color
        self.score = 0
        self.anim_count = 0
        self.anim_speed = 60
        self.anim_limit = 2000
        self.game_over = False
        self.started = True

    def _new_figure(self):
        return Piece.random()

    def get_record(self):
        try:
            with open(RECORD_PATH, "r", encoding="utf-8") as file:
                value = file.readline().strip() or "0"
                return value
        except FileNotFoundError:
            with open(RECORD_PATH, "w", encoding="utf-8") as file:
                file.write("0")
            return "0"

    def set_record(self):
        record_value = max(int(self.record or 0), self.score)
        with open(RECORD_PATH, "w", encoding="utf-8") as file:
            file.write(str(record_value))
        self.record = str(record_value)

    def move_horizontal(self, dx):
        old_figure = self.figure.copy()
        self.figure.move(dx, 0)

        if self.board.collides(self.figure.cells):
            self.figure = old_figure

    def rotate_figure(self):
        center = self.figure.cells[0]
        old_figure = self.figure.copy()
        self.figure.rotate(center)

        if self.board.collides(self.figure.cells):
            self.figure = old_figure

    def spawn_next_figure(self):
        self.figure = self.next_figure.copy()
        self.color = self.next_figure.color
        self.next_figure = self._new_figure()
        self.next_color = self.next_figure.color

    def step_down(self):
        old_figure = self.figure.copy()
        self.figure.move(0, 1)

        if self.board.collides(self.figure.cells):
            self.board.merge_figure(old_figure.cells, self.color)
            self.spawn_next_figure()
            self.anim_limit = 1000
            return True

        return False

    def handle_game_over(self):
        if self.board.is_game_over():
            self.set_record()
            self.game_over = True
            self.started = False

    def run(self):
        while True:
            if not self.started and not self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and (event.key in (pygame.K_RETURN, pygame.K_SPACE)):
                        self.started = True
                self.renderer.render_start_screen(self)
                pygame.display.flip()
                self.clock.tick(FPS)
                continue

            if self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and (event.key in (pygame.K_RETURN, pygame.K_SPACE)):
                        self.reset_game()
                        continue
                self.renderer.render_game_over(self)
                pygame.display.flip()
                self.clock.tick(FPS)
                continue

            dx, rotate = 0, False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    elif event.key == pygame.K_RIGHT:
                        dx = 1
                    elif event.key == pygame.K_DOWN:
                        self.anim_limit = 150
                    elif event.key == pygame.K_UP:
                        rotate = True

            self.move_horizontal(dx)

            self.anim_count += self.anim_speed
            if self.anim_count > self.anim_limit:
                self.anim_count = 0
                self.step_down()

            if rotate:
                self.rotate_figure()

            cleared_lines = self.board.clear_lines()
            if cleared_lines:
                self.anim_speed += 3 * cleared_lines
                self.score += calculate_score(cleared_lines)

            self.renderer.render(self)
            self.handle_game_over()

            pygame.display.flip()
            self.clock.tick(FPS)
