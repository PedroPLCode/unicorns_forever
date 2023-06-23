import pygame.font

class Button():
    def __init__(self, uf_game, msg):
        """Button initialization."""
        self.settings = uf_game.settings
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = self.settings.buttons_width, self.settings.buttons_height
        self.button_color = self.settings.buttons_color
        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(None, self.settings.buttons_font_size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        msg = self.settings.msg
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Message into the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draws a button with message inside."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)