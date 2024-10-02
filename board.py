import pygame

class Tile:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 255) 
        self.letter = ""  
        self.font = pygame.font.SysFont('berlinsansfb', 60)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

        if self.letter:
            text_surface = self.font.render(self.letter, True, (0, 0, 0))
            screen.blit(
                text_surface,
                (self.x + (self.size - text_surface.get_width()) // 2,
                 self.y + (self.size - text_surface.get_height()) // 2)
            )

    def set_letter(self, letter):
        self.letter = letter

    def set_color(self, color):
        self.color = color


class Grid:
    def __init__(self, rows, cols, tile_size, padding, margin_x, margin_y):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.padding = padding
        self.margin_x = margin_x
        self.margin_y = margin_y

        self.tiles = [[Tile(
            self.margin_x + col * (self.tile_size + self.padding),
            self.margin_y + row * (self.tile_size + self.padding),
            self.tile_size
        ) for col in range(self.cols)] for row in range(self.rows)]

    def draw(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)

    def set_tile_letter(self, row, col, letter):
        self.tiles[row][col].set_letter(letter)

    def set_tile_color(self, row, col, color):
        self.tiles[row][col].set_color(color)