import pygame

class Board:
    def __init__(self, rows, cols, square_size, start_x, start_y):
        self.rows = rows
        self.cols = cols
        self.square_size = square_size
        self.start_x = start_x
        self.start_y = start_y

    def draw(self, screen):
        screen.fill((255, 255, 255))
        number = 101
        dir = 1

        for i in range(self.rows):
            if i % 2 == 0:
                for j in range(self.cols):
                    number = number - dir

                    pygame.draw.rect(screen, (0, 0, 0), (self.start_x + j * self.square_size, self.start_y + i * self.square_size, self.square_size, self.square_size), 1)
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(number), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(self.start_x + j * self.square_size + self.square_size // 2, self.start_y + i * self.square_size + self.square_size // 2))
                    screen.blit(text, text_rect)
            else:
                for j in range(self.cols):
                    pygame.draw.rect(screen, (0, 0, 0), (self.start_x + j * self.square_size, self.start_y + i * self.square_size, self.square_size, self.square_size), 1)
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(number), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(self.start_x + j * self.square_size + self.square_size // 2, self.start_y + i * self.square_size + self.square_size // 2))
                    screen.blit(text, text_rect)

                    number = number - dir

            number -= 10
            dir *= -1
