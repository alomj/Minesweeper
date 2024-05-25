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
                if(event.type == pygame.QUIT):
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.get_size()[0]):
            for col in range(self.board.get_size()[1]):
                image = self.images["empty-block"]
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.piece_size[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.piece_size[1]
    def load_images(self):
        self.images = {}
        for filename in os.listdir("images"):
            if (not filename.endswith(".png")):
                continue
            image = pygame.image.load(r"images/" + filename)
            image = pygame.transform.scale(image, self.piece_size)
            self.images[filename.split(".")[0]] = image