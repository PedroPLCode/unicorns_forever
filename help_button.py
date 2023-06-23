import pygame.font

class HelpButton():
    def __init__(self, uf_game, help_msg):
        """Button initialization."""
        self.settings = uf_game.settings
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = self.settings.buttons_width, self.settings.buttons_height
        self.button_color = self.settings.buttons_color
        self.text_color = self.settings.text_color 
        self.font = pygame.font.SysFont(None, self.settings.buttons_font_size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft

        help_msg = self.settings.help_msg
        self._prep_help_msg(help_msg)

    def _prep_help_msg(self, help_msg):
        """Message into the button."""
        self.help_msg_image = self.font.render(help_msg, True, self.text_color, self.button_color)
        self.help_msg_image_rect = self.help_msg_image.get_rect()
        self.help_msg_image_rect.center = self.rect.center

    def draw_help_button(self):
        """Draws a button with message inside."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.help_msg_image, self.help_msg_image_rect)

    