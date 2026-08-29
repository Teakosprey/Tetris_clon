import pygame

from game.config import TILE, asset_path


class Renderer:
    def __init__(self, screen, game_surface):
        self.screen = screen
        self.game_surface = game_surface

        self.bg = pygame.image.load(asset_path('bg.jpg')).convert()
        self.game_bg = pygame.image.load(asset_path('bg2.webp')).convert()

        self.main_font = pygame.font.Font(asset_path('font.ttf'), 65)
        self.font = pygame.font.Font(asset_path('font.ttf'), 45)
        self.small_font = pygame.font.Font(asset_path('font.ttf'), 24)

        self.title_tetris = self.main_font.render('TETRIS', True, pygame.Color('yellow'))
        self.title_score = self.font.render('Score:', True, pygame.Color('blue'))
        self.title_record = self.font.render('Record:', True, pygame.Color('green'))

    def _draw_overlay(self, title, lines):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 254))
        self.screen.blit(overlay, (0, 0))

        title_label = self.main_font.render(title, True, pygame.Color('yellow'))
        self.screen.blit(title_label, (self.screen.get_width() // 2 - title_label.get_width() // 2, 120))

        for i, line in enumerate(lines):
            text = self.small_font.render(line, True, pygame.Color('white'))
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 300 + i * 50))

    def render_start_screen(self, game):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_surface, (20, 20))
        self.game_surface.blit(self.game_bg, (0, 0))
        self._draw_overlay(
            'TETRIS',
            [
                'Controls:',
                '',
                'Left / Right - move',
                'Up - rotate',
                'Down - soft drop',
                '',
                'Press Enter or Space to start'
            ]
        )


    def render_game_over(self, game):
        self.render(game)
        self._draw_overlay(
            'GAME OVER',
            [
                f'Score: {game.score}',
                f'Record: {game.record}',
                '',
                '',
                '',
                'Press Enter or Space to restart'
            ]
        )

    def render(self, game):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_surface, (20, 20))
        self.game_surface.blit(self.game_bg, (0, 0))

        for rect in game.board.grid:
            pygame.draw.rect(self.game_surface, (40, 40, 40), rect, 1)

        figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
        for rect in game.figure:
            figure_rect.x = rect.x * TILE
            figure_rect.y = rect.y * TILE
            pygame.draw.rect(self.game_surface, game.color, figure_rect)

        for y, row in enumerate(game.board.field):
            for x, color in enumerate(row):
                if color:
                    figure_rect.x = x * TILE
                    figure_rect.y = y * TILE
                    pygame.draw.rect(self.game_surface, color, figure_rect)

        for rect in game.next_figure:
            figure_rect.x = rect.x * TILE + 380
            figure_rect.y = rect.y * TILE + 185
            pygame.draw.rect(self.screen, game.next_color, figure_rect)

        self.screen.blit(self.title_tetris, (485, 35))
        self.screen.blit(self.title_score, (535, 600))
        self.screen.blit(self.font.render(str(game.score), True, pygame.Color('white')), (550, 660))
        self.screen.blit(self.title_record, (525, 730))
        self.screen.blit(self.font.render(game.record, True, pygame.Color('white')), (550, 790))
