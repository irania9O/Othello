from src.constant import *
import pygame

class Board:

    def __init__(self) -> None:
        pass

    def show(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                # Initialing RGB black
                color = (0, 0, 0)

                # Create square corner positions
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                # Craw square on screen
                pygame.draw.rect(screen, color, rect, width =1)
