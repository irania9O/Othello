from src.constant import *
import pygame
import sys

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption("Chess")


    def mainloop(self):
        while True:
            
            for event in pygame.event.get():
                # exit game and close screen
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()

main = Main()
main.mainloop() 