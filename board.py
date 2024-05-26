from piece import Piece
from random import random

class Board():
    def __init__(self, size, probability):
        self.size = size
        self.probability = probability
        self.lost = False
        self.won = False
        self.num_clicked = 0
        self.num_non_bombs = 0
        self.set_board()


    def set_board(self):
        self.board = []
        for row in range(self.size[0]):
            row_pieces = []
            for col in range(self.size[1]):
                has_bomb = random() < self.probability
                if (not has_bomb):
                    self.num_non_bombs += 1
                piece = Piece(has_bomb)
                row_pieces.append(piece)
            self.board.append(row_pieces)
        self.set_neighbors()

    def set_neighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.get_piece(row, col)
                neighbors = self.get_list_of_neighbors((row, col))
                piece.set_neighbors(neighbors)

    def get_list_of_neighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                out_of_bounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if same or out_of_bounds:
                    continue
                neighbors.append(self.get_piece(row, col))
        return neighbors

    def get_size(self):
        return self.size

    def get_piece(self, row, col):
        return self.board[row][col]

    def handle_click(self, piece, flag):
        if (piece.get_clicked() or (not flag and piece.get_flagged())):
            return
        if (flag):
            piece.toggle_flag()
            return
        if  (piece.get_has_bomb()):
            self.lost = True
            return
        self.num_clicked += 1
    def get_lost(self):
        return self.lost
    def get_won(self):
        return self.num_non_bombs == self.num_clicked