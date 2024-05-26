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
            if self.board.get_won():
                self.display_message("You Won!", (0, 255, 0))
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
            elif self.board.get_lost():
                self.display_message("You Lost!", (255, 0, 0))
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

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
            string = "bomb-at-clicked-block" if piece.get_has_bomb() else str(piece.get_num_around())
        else:
            string = "flag" if piece.get_flagged() else "empty-block"

        return self.images[string]

    def handle_click(self, position, right_click):
        if (self.board.get_lost()) or self.board.get_won():
            return
        row, col = position[1] // self.piece_size[1], position[0] // self.piece_size[0]
        piece = self.board.get_piece(row, col)
        self.board.handle_click(piece, right_click)


    def display_message(self, message, color):
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 74)
        text = self.font.render(message, True, color)
        text_rect = text.get_rect(center=(self.screen_size[0] // 2, self.screen_size[1] // 2))
        self.screen.blit(text, text_rect)
