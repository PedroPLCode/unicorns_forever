import pygame
from pygame.sprite import Sprite

class Unicorn(Sprite):
    """Unicorn managment."""

    def __init__(self, uf_game):
        """Unicorn initialization."""
        super().__init__()

        self.screen = uf_game.screen
        self.settings = uf_game.settings
        self.screen_rect = uf_game.screen.get_rect()

        self.image_left = pygame.image.load(self.settings.unicorn_image_left)
        self.image_right = pygame.image.load(self.settings.unicorn_image_right)
        self.image = self.image_right
        
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Unicorn location updating."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.unicorn_speed_left_right
            self.image = self.image_right
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.unicorn_speed_left_right
            self.image = self.image_left
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.unicorn_speed_up_down
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.unicorn_speed_up_down

        self.rect_x = self.x
        self.rect_y = self.y

    def blitme(self):
        """Shows unicorn in current location on the screen."""

        self.screen.blit(self.image, self.rect)

    def center_unicorn(self):
        """New unicorn in the center bottom of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)