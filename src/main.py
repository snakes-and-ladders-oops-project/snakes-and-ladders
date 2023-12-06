import pygame
from snakes_ladders.constants import WIDTH, HEIGHT
from board import Board
from dice import Dice

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption('Snakes and Ladders: OODP Project')

def main():
    run = True
    clock = pygame.time.Clock()

    board = Board(x=0, y=0)  # Adjust x and y values based on your preference
    dice = Dice(x=WIDTH - 100, y=50)  # Adjust x and y values based on your preference

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if dice.rect.collidepoint(event.pos):
                    dice.roll()

        board.draw(screen)
        dice.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
