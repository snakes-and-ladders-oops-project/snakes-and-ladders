import pygame
from snakes_ladders.constants import WHITE, BLACK
from jumper import JumperCell, SnakeCell, LadderCell

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

        snakes = [
            (98, 78),
            (95, 75),
            (92, 88),
            (83, 57),
            (73, 15),
            (46, 5),
            (44, 22),
            (33, 9),
            (28, 12),
            (21, 2)
        ]

        ladders = [
            (8, 29),
            (16, 45),
            (26, 54),
            (36, 89),
            (49, 67),
            (62, 91),
            (64, 84),
            (71, 93),
            (87, 99),
            (94, 98)
        ]

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

                    for snake in snakes:
                        if snake[0] == number:
                            cell_instance = SnakeCell(position, height, isFirst, isLast, jump_to=snake[1])
                            break
                    else:
                        for ladder in ladders:
                            if ladder[0] == number:
                                cell_instance = LadderCell(position, height, isFirst, isLast, jump_to=ladder[1])
                                break
                        else:
                            cell_instance = JumperCell(position, height, isFirst, isLast)

                    row.append(cell_instance)

            else:
                for j in range(self.cols):
                    position = number
                    isFirst = isLast = False

                    if number == 1:
                        isFirst = True
                    elif number == 100:
                        isLast = True

                    for snake in snakes:
                        if snake[0] == number:
                            cell_instance = SnakeCell(position, height, isFirst, isLast, jump_to=snake[1])
                            break
                    else:
                        for ladder in ladders:
                            if ladder[0] == number:
                                cell_instance = LadderCell(position, height, isFirst, isLast, jump_to=ladder[1])
                                break
                        else:
                            cell_instance = JumperCell(position, height, isFirst, isLast)

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

                # Fill the entire cell with the specified color
                pygame.draw.rect(screen, cell_instance.color if hasattr(cell_instance, 'color') else (255, 255, 255), rect)
                
                # Draw black borders for each cell
                pygame.draw.rect(screen, BLACK, rect, 1)

                font = pygame.font.Font(None, 36)
                text = font.render(str(cell_instance.cellValue), True, BLACK)
                text_rect = text.get_rect(center=(self.x + j * height + height // 2, self.y + i * height + height // 2))
                screen.blit(text, text_rect)

                # Skip rendering "Jump to" message
                if isinstance(cell_instance, JumperCell) and cell_instance.jump_to is not None:
                    pass
