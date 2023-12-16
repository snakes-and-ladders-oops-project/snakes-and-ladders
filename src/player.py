import pygame
from jumper import JumperCell

HEIGHT = 600
WIDTH = 600
COLS = 10
SQUARE_SIZE = WIDTH // COLS

class Player:
    def __init__(self, name, token_color, player_image):
        self.name = name
        self.board = None
        self.position = 1
        self.token_color = token_color
        self.radius = WIDTH // COLS // 6
        self.player_image = player_image
        self.six_count = 0

    def set_board(self, board):
        self.board = board

    def move(self, steps):
        if self.six_count == 3:
            self.six_count = 0
            return

        if self.position == 1:
            if steps != 6:
                return
            
        if self.position == 95:
            if steps == 6:
                return
        
        if self.position == 96:
            if steps >= 5:
                return
            
        if self.position == 97:
            if steps >= 4:
                return
            
        if self.position == 98:
            if steps >= 3:
                return
            
        if self.position == 99:
            if steps >= 2:
                return

        initial_position = self.position
        self.position += steps

        if self.position > COLS * COLS:
            self.position = COLS * COLS

        row = (self.position - 1) // COLS
        col = (self.position - 1) % COLS

        if row % 2 != 0:
            col = COLS - col - 1

        self.x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = HEIGHT - (row * SQUARE_SIZE + SQUARE_SIZE // 2)

        current_cell = self.board.cells[COLS - 1 - row][col]
        if isinstance(current_cell, JumperCell) and current_cell.jump_to is not None:
            self.position = current_cell.jump_to

        if self.position >= COLS * COLS:
            self.position = COLS * COLS

    def draw_token(self, screen):
        if self.board is None:
            return

        cell = self.position - 1
        row = cell // COLS
        col = cell % COLS

        if row % 2 != 0:
            col = COLS - col - 1

        row = COLS - 1 - row

        center_x = self.board.x + col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = self.board.y + row * SQUARE_SIZE + SQUARE_SIZE // 2

        player_image = pygame.transform.scale(self.player_image, (SQUARE_SIZE // 2, SQUARE_SIZE // 2))
        player_image.set_colorkey((0, 0, 0))
        screen.blit(player_image, (center_x - SQUARE_SIZE // 4, center_y - SQUARE_SIZE // 4))
