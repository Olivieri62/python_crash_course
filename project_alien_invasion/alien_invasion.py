import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize te game, and create game ressources"""
        pygame.init()
        #Create an instance of the class Clock from the pygame.time module
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Set the Background color
        self.bg_color=(230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyborad and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass trhrough the loop
            self.screen.fill(self.bg_color)
            #Make the most recently drawn screen visible
            pygame.display.flip()
            #Pygame will do its best to make the loop run exactly 60 times per second
            self.clock.tick(60)

if __name__ == '__main__':
    #Make agame instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

