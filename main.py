from game import Game
from board import Board
size = (9,9)
screen_width = 800
screen_height = 800
screen_size = (screen_width, screen_height)
board = Board(size)
game = Game(board, screen_size)
game.run()