from piece import Piece
from random import random
class Board():
    def __init__(self, size, probability):
        self.size = size
        self.probability = probability
        self.set_board()


    def set_board(self):
        self.board = []
        for row in range(self.size[0]):
            row_pieces = []
            for col in range(self.size[1]):
                has_bomb = random() < self.probability
                piece = Piece(has_bomb)
                row_pieces.append(piece)
            self.board.append(row_pieces)

    def get_size(self):
        return self.size