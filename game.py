import pygame
import os
class Game():
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.piece_size = self.screen_size[0] // self.board.getsize()[1], self.screen_size[1] // self.board.getsize()[0]
        self.load_images
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def load_images(self):
        self.images = {}
        for filename in os.listdir("images"):
            if (not filename.endswith(".png")):
                continue
            image = pygame.image.load(r"images\\" + filename)
            image = pygame.transform.scale(image, self.piece_size)
            self.images[filename.split(".")] = image