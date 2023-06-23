import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Unicorn bullets management."""

    def __init__(self, uf_game):
        """Create bullet in current Unicorn position."""

        super().__init__()
        self.screen = uf_game.screen
        self.settings = uf_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = uf_game.unicorn.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Bullet moving up."""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Shows bullet on the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)