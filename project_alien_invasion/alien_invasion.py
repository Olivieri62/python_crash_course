import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize te game, and create game ressources"""
        pygame.init()
        #Create an instance of the class Clock from the pygame.time module
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)



    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            #Redraw the screen during each pass trhrough the loop
            self._update_screen()
            #Pygame will do its best to make the loop run exactly 60 times per second
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses ans mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #Make agame instance, and run the game
    ai_game = AlienInvasion()
    ai_game.run_game()

