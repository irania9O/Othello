from src.board import Board
from src.constant import *
from src.piece import Piece
from src.square import Square
import pygame
import os

class Game:

    def __init__(self, screen) -> None:
        self.screen  = screen
        self.turn = "white"
        self.board = Board()
        self.possible_squares = []
        self.reverse_squares = []
        self.black_pieces = 0
        self.white_pieces = 0

    def show_board(self):
        self.screen.fill((0, 144, 103))
        for row in range(ROWS):
            for col in range(COLS):
                # color = (0, 144, 103)
                # rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # pygame.draw.rect(self.screen, color, rect)
                color = (0, 0, 0)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(self.screen, color, rect, width = 1)

                self.calculate_pieces()
                self.font = pygame.font.SysFont('arial', 22)

                img_black = pygame.image.load(os.path.join(f"assets/images/black-100.png"))
                img_black_center = 50, 650
                self.screen.blit(img_black, img_black.get_rect(center=img_black_center))
                self.label = self.font.render(f"{self.black_pieces}", 1, (255,255,255))
                label_position = [40 , 637]
                if self.black_pieces < 10:
                    label_position[0] = 45
                self.screen.blit(self.label, label_position)

                img_white = pygame.image.load(os.path.join(f"assets/images/white-100.png"))
                img_white_center = 550, 650
                self.screen.blit(img_white, img_white.get_rect(center=img_white_center))
                self.label = self.font.render(f"{self.white_pieces}", 1, (0,0,0))
                label_position = [540 , 637]
                if self.white_pieces < 10:
                    label_position[0] = 545
                self.screen.blit(self.label, label_position)                

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


    def calculate_reverse(self, row, col):
        for row_incr, col_incr in [
                (-1, +1), # up-right
                (-1, -1), # up-lefr
                (+1, -1), # down-right
                (+1, +1), # down-left
                (-1, 0), # up
                (0, +1), # left
                (+1, 0), # down
                (0, -1)  # right
                ]:
            possible_row = row + row_incr
            possible_col = col + col_incr


            if Square.in_range(possible_row, possible_col):
                if self.board.squares[possible_row][possible_col].has_enemy_piece(self.turn):
                    row_step = possible_row - row 
                    col_step = possible_col - col
                    between = []
                    status = False
                    for i in range(1,8):
                        c_row = row + i*row_step
                        c_col = col + i*col_step
                        if Square.in_range(c_row, c_col):
                            if self.board.squares[c_row][c_col].has_enemy_piece(self.turn):
                                try:
                                    if self.board.squares[c_row+row_step][c_col+col_step].has_enemy_piece(self.turn):
                                        between.append(Square(c_row, c_col))
                                    elif self.board.squares[c_row+row_step][c_col+col_step].has_team_piece(self.turn):
                                        between.append(Square(c_row, c_col))
                                        break
                                    elif self.board.squares[c_row+row_step][c_col+col_step].is_empty():
                                        between.clear()
                                        break
                                    else:
                                        between.clear()
                                        break                                 
                                except:
                                        between.clear()
                                        break
                                
                    for sqr in between:
                        self.board.squares[sqr.row][sqr.col] = Square(sqr.row, sqr.col, Piece(self.turn))

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

    def calculate_pieces(self):
        self.black_pieces = 0
        self.white_pieces = 0
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    if self.board.squares[row][col].piece.color == "black":
                        self.black_pieces += 1
                    elif self.board.squares[row][col].piece.color == "white":
                        self.white_pieces += 1

    def reset(self):
        self.__init__(self.screen)