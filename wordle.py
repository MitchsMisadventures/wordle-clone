import pygame
from pygame.locals import K_a, K_z, K_BACKSPACE, K_RETURN
import random
from collections import Counter
from button import Button


INCORRECT = (192, 192, 192)
WRONG_PLACEMENT = (255, 255, 200)
CORRECT = (200, 255, 200)

class Wordle:
    def __init__(self, grid):
        self.grid = grid
        self.current_row = 0
        self.current_col = 0
        self.max_cols = self.grid.cols
        self.current_guess = []
        self.victory = False 
        self.in_progress = True  
        self.correct_word = random.choice(list(open('word-list.txt'))).strip().upper()
        self.correct_letters = Counter(self.correct_word)
        self.next_word_button = Button(300, 700, 200, 50, "Next Word", (255, 255, 255), (0, 0, 0))  # Add this line

    def handle_key_event(self, event):
        if not self.in_progress:
            return 

        if event.type == pygame.KEYDOWN:
            if pygame.K_a <= event.key <= pygame.K_z:
                letter = chr(event.key).upper()
                if self.current_col < self.max_cols:
                    self.grid.set_tile_letter(self.current_row, self.current_col, letter)
                    self.current_guess.append(letter) 
                    self.current_col += 1 

            elif event.key == pygame.K_BACKSPACE:
                if self.current_col > 0:
                    self.current_col -= 1
                    self.grid.set_tile_letter(self.current_row, self.current_col, "")
                    self.current_guess.pop()  

            elif event.key == pygame.K_RETURN:
                if self.current_col == self.max_cols:
                    self.submit_guess(self.current_guess)  
    
    def submit_guess(self, guess):
        self.guess = ''.join(guess).upper()
        self.current_letters = self.correct_letters.copy()
        
        for col in range(self.max_cols):
            letter = self.guess[col]
            
            if letter == self.correct_word[col] and self.current_letters[letter] > 0:  # Correct position
                self.grid.set_tile_color(self.current_row, col, CORRECT)
                self.current_letters[letter] -= 1

            elif letter in self.correct_word and self.current_letters[letter] > 0:  # Wrong placement
                self.grid.set_tile_color(self.current_row, col, WRONG_PLACEMENT)
                self.current_letters[letter] -= 1

            else:  
                self.grid.set_tile_color(self.current_row, col, INCORRECT)

        if self.guess == self.correct_word:
            self.in_progress = False 
            return 
        else:
            self.current_guess = []
            self.current_row += 1
            self.current_col = 0
            
            if self.current_row > 5:  
                self.in_progress = False  
                return  
            
    def draw(self, screen):
        self.grid.draw(screen)
        font = pygame.font.SysFont('berlinsansfb', 40)

        if not self.in_progress and self.current_row > 5: 
            text_surface = font.render(f'The word was: {self.correct_word}', True, (255, 255, 255))  

            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 75)) 
            
            screen.blit(text_surface, text_rect.topleft) 

        if not self.in_progress:  
            self.next_word_button.draw(screen)
                
    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.in_progress:  
                if self.next_word_button.is_clicked(event.pos):
                    self.start_new_game() 

    def start_new_game(self):
        self.current_row = 0
        self.current_col = 0
        self.current_guess = []
        self.in_progress = True
        self.correct_word = random.choice(list(open('word-list.txt'))).strip().upper()
        self.correct_letters = Counter(self.correct_word)

        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                self.grid.set_tile_letter(row, col, "")  
                self.grid.set_tile_color(row, col, (255, 255, 255)) 
