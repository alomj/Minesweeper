from game import Game
from board import Board


def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    SIZE = (9, 9)
    PROBABILITY = 0.5
    board = Board(SIZE, PROBABILITY)
    game = Game(board, screen_size)
    game.run()


if __name__ == '__main__':
    main()
