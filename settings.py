from random import randint

class Settings:
    """Storing all settings used in game."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (153, 204, 0) #grass
        self.unicorns_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 255) #pink
        self.bullets_allowed = 3

        self.troll_bullet_width = 8
        self.troll_bullet_height = 25
        self.troll_bullet_color = (153, 51, 0) #brown

        self.bomb_width = 20
        self.bomb_height = 20
        self.bomb_color = (255, 0, 255) #pink
        self.bombs_allowed = 1
        self.bombs_limit = 1

        self.buttons_color = (255, 0, 255) #pink
        self.text_color = (0, 0, 128) #blue
        self.buttons_font_size = 48

        self.buttons_width = 250
        self.buttons_height = 60

        self.instr_width = 600
        self.instr_height = 700
        self.instr_font_size = 22

        self.hord_drop_speed = 10
        self.trolls_starts_shoot_max = 15
        self.trolls_starts_shoot_min = 6
        self.trolls_starts_shoot = randint(self.trolls_starts_shoot_min, self.trolls_starts_shoot_max)

        self.speed_up_scale = 1.1
        self.score_scale = 1.5
        self.new_bombs = 1

        # Language changes here
        self.msg = "g - Game"
        self.quit_msg = 'q - Quit'
        self.help_msg = 'h - Help'
        self.score_text = 'score: '
        self.high_score_text = 'high score: '
        self.level_text = 'level: '

        # information file change here
        self.instructions_file = 'unicorns_forever/readmeEN.txt'

        self.troll_image_left = 'unicorns_forever/images/trollL.bmp'
        self.troll_image_right = 'unicorns_forever/images/trollR.bmp'
        self.unicorn_image_left = 'unicorns_forever/images/unicornL.bmp'
        self.unicorn_image_right = 'unicorns_forever/images/unicornR.bmp'
 
        self.filename = 'unicorns_forever/high_score.json'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """settings initialization."""
        self.unicorn_speed_left_right = 1
        self.unicorn_speed_up_down = 1
        self.bullet_speed = 2.0
        self.troll_bullet_speed = 1.0
        self.bomb_speed = 1.5
        self.troll_speed = 1.0

        self.troll_points = 50

        self.hord_direction = 1

        self.bombs_fired = 0

    def increase_speed(self):
        """change speed settings."""
        self.unicorn_speed_left_right *= self.speed_up_scale
        self.unicorn_speed_up_down *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.bomb_speed *= self.speed_up_scale
        self.troll_speed *= self.speed_up_scale
        self.troll_bullet_speed *= self.speed_up_scale
        self.troll_points = int(self.troll_points * self.score_scale)
        self.bombs_limit += self.new_bombs