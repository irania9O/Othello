class Square:
    def __init__(self, row, col, piece=None) -> None:
        self.row = row
        self.col = col
        self.piece = piece

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col
    
    def has_piece(self):
        return self.piece != None