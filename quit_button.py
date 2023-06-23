import pygame.font

class QuitButton():
    def __init__(self, uf_game, quit_msg):
        """Button initialization."""
        self.settings = uf_game.settings
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = self.settings.buttons_width, self.settings.buttons_height
        self.button_color = self.settings.buttons_color
        self.text_color = self.settings.text_color 
        self.font = pygame.font.SysFont(None, self.settings.buttons_font_size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        quit_msg = self.settings.quit_msg
        self._prep_quit_msg(quit_msg)

    def _prep_quit_msg(self, quit_msg):
        """Message into the button."""
        self.quit_msg_image = self.font.render(quit_msg, True, self.text_color, self.button_color)
        self.quit_msg_image_rect = self.quit_msg_image.get_rect()
        self.quit_msg_image_rect.center = self.rect.center

    def draw_quit_button(self):
        """Draws a button with message inside."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.quit_msg_image, self.quit_msg_image_rect)