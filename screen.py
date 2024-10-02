import pygame
from board import Grid
from wordle import Wordle

class Window:
    def __init__(self, width=800, height=800):
        pygame.init() 
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wordle Clone // MitchsMiscodes")
        self.rows = 6
        self.cols = 5
        self.tile_size = 80 
        self.padding = 10 
        self.grid_width = self.cols * (self.tile_size + self.padding) - self.padding
        self.grid_height = self.rows * (self.tile_size + self.padding) - self.padding
        self.margin_x = (self.width - self.grid_width) // 2
        self.margin_y = (self.height - self.grid_height) // 2
        self.grid = Grid(self.rows, self.cols, self.tile_size, self.padding, self.margin_x, self.margin_y)
        self.wordle = Wordle(self.grid)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.wordle.handle_key_event(event)
                self.wordle.handle_mouse_event(event)  

            self.screen.fill((80, 100, 150)) 
            
            self.wordle.draw(self.screen) 
            pygame.display.update() 

        pygame.quit()