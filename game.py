from src.board import Board
from src.constant import *
import pygame

class Game:

    def __init__(self, screen) -> None:
        self.screen  = screen
        self.board = Board()

    def show_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                # Initialing RGB black
                color = (0, 0, 0)

                # Create square corner positions
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                # Craw square on screen
                pygame.draw.rect(self.screen, color, rect, width =1)

    def show_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                # if we have pice on specific squares
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    # all pices except dragger piece
                    piece.set_texture()
                    img = pygame.image.load(piece.texture)
                    
                    # centring image
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)

                    self.screen.blit(img, piece.texture_rect)
