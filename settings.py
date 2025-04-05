class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.fullscreen = False
        # Dimensions for windowed
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_wrap_around = False
        self.ship_limit = 3 # 3

        # Bullet settings
        self.bullet_speed = 50
        self.bullet_width = 300 # 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 60 # 10
        # fleet direction of represents right; -1 represents left.
        self.fleet_direction = 1