import pygame
import os

class Game():
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.piece_size = self.screen_size[0] // self.board.get_size()[1], self.screen_size[1] // self.board.get_size()[0]
        self.load_images()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    right_click = pygame.mouse.get_pressed()[2]
                    self.handle_click(position, right_click)

            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.get_size()[0]):
            for col in range(self.board.get_size()[1]):
                piece = self.board.get_piece(row, col)
                image = self.get_image(piece)
                self.screen.blit(image, topLeft)
                topLeft = (topLeft[0] + self.piece_size[0], topLeft[1])
            topLeft = (0, topLeft[1] + self.piece_size[1])

    def load_images(self):
        self.images = {}
        for filename in os.listdir("images"):
            if not filename.endswith(".png"):
                continue
            image = pygame.image.load(os.path.join("images", filename))
            image = pygame.transform.scale(image, self.piece_size)
            self.images[filename.split(".")[0]] = image

    def get_image(self, piece):
        string = None
        if piece.get_clicked():
            pass
        else:
            string = "flag" if piece.get_flagged() else "empty-block"

        return self.images[string]

    def handle_click(self, position, right_click):
        row, col = position[1] // self.piece_size[1], position[0] // self.piece_size[0]
        piece = self.board.get_piece(row, col)
        self.board.handle_click(piece, right_click)
