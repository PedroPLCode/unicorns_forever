import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    """Unicorn bombs management."""

    def __init__(self, uf_game):
        """Create bomb in current Unicorn position."""

        super().__init__()
        self.screen = uf_game.screen
        self.settings = uf_game.settings
        self.color = self.settings.bomb_color

        self.rect = pygame.Rect(0, 0, self.settings.bomb_width, self.settings.bomb_height)
        self.rect.midtop = uf_game.unicorn.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Bomb moving up."""

        self.y -= self.settings.bomb_speed
        self.rect.y = self.y

    def draw_bomb(self):
        """Shows bomb on the screen."""

        pygame.draw.ellipse(self.screen, self.color, self.rect)