from src.board import Board
from src.constant import *
import pygame
from src.square import Square

class Game:

    def __init__(self, screen) -> None:
        self.screen  = screen
        self.turn = "white"
        self.board = Board()
        self.possible_squares = []

    def show_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                color = (0, 144, 103)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(self.screen, color, rect)

                color = (0, 0, 0)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
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

    def calculate_piece(self):
        self.possible_squares = []
        def straightline_moves(row, col, incrs):
            for row_incr, col_incr in incrs:
                possible_row = row + row_incr
                possible_col = col + col_incr


                if Square.in_range(possible_row, possible_col):
                    if self.board.squares[possible_row][possible_col].has_enemy_piece(self.turn):
                        row_step = possible_row - row 
                        col_step = possible_col - col

                        for i in range(1,8):
                            c_row = row + i*row_step
                            c_col = col + i*col_step
                            if Square.in_range(c_row, c_col):
                                if self.board.squares[c_row][c_col].has_team_piece(self.turn):
                                    break
                                elif self.board.squares[c_row][c_col].is_empty():
                                    if self.board.squares[c_row-row_step][c_col-col_step].has_enemy_piece(self.turn):
                                        self.possible_squares.append(Square(c_row, c_col))
                                    else:
                                        break
        for row in range(ROWS):
            for col in range(COLS):
                # if we have pice on specific squares
                if self.board.squares[row][col].has_team_piece(self.turn):
                    straightline_moves(row, col,
                    [
                    (-1, +1), # up-right
                    (-1, -1), # up-lefr
                    (+1, -1), # down-right
                    (+1, +1), # down-left
                    (-1, 0), # up
                    (0, +1), # left
                    (+1, 0), # down
                    (0, -1)  # right
                    ])

    def show_possibles(self):
        for sqr in self.possible_squares:
            if isinstance(sqr, Square):
                color = (245, 66, 75)
                rect = (sqr.col * SQSIZE, sqr.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(self.screen, color, rect)      
                color = (0, 0, 0)
                rect = (sqr.col * SQSIZE, sqr.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(self.screen, color, rect, width =1)          

    def next_turn(self):
        self.turn = "white" if self.turn == "black" else "black"