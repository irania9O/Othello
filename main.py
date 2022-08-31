from src.game import Game
from src.piece import Piece
from src.square import Square
from src.constant import *
import pygame
import sys

class Main:
    def __init__(self) -> None:
        # Initialing pygame screen
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption("Reversi (Othello)")

        # Initialing RGB green 
        color = (0, 144, 103)
    
        # Changing surface color
        self.screen.fill(color)
        
        # Store Game object in blew varivble
        self.game = Game(self.screen)

    def mainloop(self):
        while True:
            self.game.show_board()
            self.game.calculate_piece()
            self.game.show_possibles()
            self.game.show_pieces()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_row = event.pos[1] // SQSIZE
                    clicked_col = event.pos[0] // SQSIZE

                    if Square(clicked_row, clicked_col) in  self.game.possible_squares:
                        self.game.board.squares[clicked_row][clicked_col] = Square(clicked_row, clicked_col, Piece(self.game.turn))
                        self.game.calculate_reverse(clicked_row, clicked_col)
                        self.game.next_turn()
                        self.game.show_board()
                        self.game.calculate_piece()

                        if len(self.game.possible_squares) == 0:
                            self.game.winner = True

                        self.game.show_possibles()
                        self.game.show_pieces()
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game.reset()

                # exit game and close screen
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()

main = Main()
main.mainloop() 