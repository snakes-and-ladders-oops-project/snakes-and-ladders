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
            (27, 5),
            (40, 3),
            (43, 18),
            (54, 31),
            (66, 45),
            (76, 58),
            (89, 53),
            (99, 41)
        ]

        ladders = [
            (4, 25),
            (13, 46),
            (33, 49),
            (50, 69),
            (62, 81),
            (74, 92),
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

        # Load the board sprite
        board_sprite = pygame.image.load('src/board.png')

        # Resize the board sprite to fit the entire board
        board_sprite = pygame.transform.scale(board_sprite, (self.width, self.height))

        # Blit the board sprite onto the screen
        screen.blit(board_sprite, (self.x, self.y))


