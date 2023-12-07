import pygame
from snakes_ladders.constants import WHITE, BLACK
from cell import Cell  

HEIGHT = 600
WIDTH = 600

class Board:
    def __init__(self, x, y):
        self.height = HEIGHT
        self.width = WIDTH
        self.rows = 10
        self.cols = 10
        self.x = x
        self.y = y
        self.cells = self.create_board()

    def create_board(self):
        height = WIDTH // self.cols
        number = 101
        dir = 1
        cells = []

        for i in range(self.rows):
            row = []
            if (i % 2 == 0):
                for j in range(self.cols):
                    number = number - dir
                    position = number
                    isFirst = isLast = False

                    if number == 1:
                        isFirst = True
                    elif number == 100:
                        isLast = True

                    cell_instance = Cell(position, height, isFirst, isLast)
                    row.append(cell_instance)

                    
            else:
                for j in range(self.cols):
                    position = number
                    isFirst = isLast = False

                    if number == 1:
                        isFirst = True
                    elif number == 100:
                        isLast = True

                    cell_instance = Cell(position, height, isFirst, isLast)
                    row.append(cell_instance)

                    number = number - dir

            number -= 10
            dir *= -1
            cells.append(row)

        return cells

    def draw(self, screen):
        screen.fill(WHITE)

        for i, row in enumerate(self.cells):
            for j, cell_instance in enumerate(row):
                height = cell_instance.CellHeight
                rect = pygame.Rect(self.x + j * height, self.y + i * height, height, height)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                font = pygame.font.Font(None, 36)
                text = font.render(str(cell_instance.cellValue), True, BLACK)
                text_rect = text.get_rect(center=(self.x + j * height + height // 2, self.y + i * height + height // 2))
                screen.blit(text, text_rect)