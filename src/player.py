import pygame
from jumper import JumperCell, SnakeCell, LadderCell

HEIGHT = 600
WIDTH = 600
COLS = 10
SQUARE_SIZE = WIDTH // COLS

class Player:
    def __init__(self, name, token_color):
        self.name = name
        self.board = None
        self.position = 1  
        self.token_color = token_color
        self.radius = SQUARE_SIZE // 6  

    def set_board(self, board):
        self.board = board

    def move(self, steps):
        initial_position = self.position
        self.position += steps

        if self.position > COLS * COLS:  
            self.position = COLS * COLS

        row = (self.position - 1) // COLS  
        col = (self.position - 1) % COLS

        if row % 2 != 0:
            col = COLS - 1 - col

        self.x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = HEIGHT - (row * SQUARE_SIZE + SQUARE_SIZE // 2)

        # Check if the current cell has a jump destination
        current_cell = self.board.cells[COLS - 1 - row][col]
        if isinstance(current_cell, JumperCell) and current_cell.jump_to is not None:
            self.position = current_cell.jump_to

        # Check if the player has reached the last cell
        if self.position >= 100:
            self.position = 100

    def draw_token(self, screen):
        if self.board is None:
            return  

        cell = self.position - 1
        row = cell // COLS
        col = cell % COLS

        if row % 2 != 0:
            col = COLS - 1 - col

        row = COLS - 1 - row

        center_x = self.board.x + col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = self.board.y + row * SQUARE_SIZE + SQUARE_SIZE // 2

        pygame.draw.circle(screen, self.token_color, (center_x, center_y), self.radius)
