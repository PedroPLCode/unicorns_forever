import json

class GameStats:
    """Statistic data in game."""

    def __init__(self, uf_game):
        """Statistic data initialization."""
        self.settings = uf_game.settings
        self._reset_stats()
        self.game_active = False

        filename = self.settings.filename
        self.high_score = self.get_stored_high_score(filename)

    def _reset_stats(self):
        """Reset of statistic data."""
        self.unicorns_left = self.settings.unicorns_limit
        self.score = 0
        self.level = 1

    def get_stored_high_score(self, filename):
        """Getting highest score from file"""
        try:
            with open(filename) as file_obj:
                high_score = json.load(file_obj)
        except FileNotFoundError:
            return 0
        else:
            return high_score
        
    def save_new_high_score(self, high_score, filename):
        """Saves new high score in file."""
        with open(filename, 'w') as f_obj:
            json.dump(high_score, f_obj)
        return high_score