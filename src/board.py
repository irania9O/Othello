from src.constant import *
from src.square import Square
from src.piece import Piece
import pygame

class Board:

    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

        self.squares[4][4] = Square(4, 4, Piece("white"))
        self.squares[3][3] = Square(3, 3, Piece("white"))

        self.squares[3][4] = Square(3, 4, Piece("black"))
        self.squares[4][3] = Square(5, 3, Piece("black"))

