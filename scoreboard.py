import pygame.font
import json

from pygame.sprite import Group

from unicorn import Unicorn

class ScoreBoard():
    """Scores information."""

    def __init__(self, uf_game):
        """Atribures initialization"""
        self.uf_game = uf_game
        self.screen = uf_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = uf_game.settings
        self.stats = uf_game.stats

        self.text_color = self.settings.buttons_color
        self.font = pygame.font.SysFont(None, self.settings.buttons_font_size)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_unicorns()

    def prep_score(self):
        """Generationg score board"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{self.settings.score_text} {format(rounded_score)}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Highest score in game."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{self.settings.high_score_text} {format(high_score)}" 
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Shows score info on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.unicorns.draw(self.screen)

    def check_high_score(self):
        """checking if we have highest score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.stats.save_new_high_score(self.stats.score, self.settings.filename)

    def prep_level(self):
        """Shows current Level."""
        level_str = str(f"{self.settings.level_text} {self.stats.level}")
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_unicorns(self):
        """Shows how much unicorns left."""
        self.unicorns = Group()
        for unicorn_number in range(self.stats.unicorns_left):
            unicorn = Unicorn(self.uf_game)
            unicorn.rect.x = 10 + unicorn_number * unicorn.rect.width
            unicorn.rect.y = 10
            self.unicorns.add(unicorn)