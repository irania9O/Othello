from game import Game
from src.constant import *
from src.board import Board
import pygame
import sys

class Main:
    def __init__(self) -> None:
        # Initialing pygame screen
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption("Chess")

        # Initialing RGB green 
        color = (0, 144, 103)
    
        # Changing surface color
        self.screen.fill(color)
        
        # Store Game object in blew varivble
        self.game = Game(self.screen)

    def mainloop(self):
        while True:
            self.game.show_board()
            self.game.show_pieces()

            for event in pygame.event.get():
                # exit game and close screen
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()

main = Main()
main.mainloop() 