from game import Game
from board import Board


def main():
    screen_width = 800
    screen_height = 800
    screen_size = (screen_width, screen_height)
    size = (9, 9)
    probability = 0.5
    board = Board(size, probability)
    game = Game(board, screen_size)
    game.run()


if __name__ == '__main__':
    main()
