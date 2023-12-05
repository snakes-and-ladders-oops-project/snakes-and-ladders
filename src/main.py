import pygame
import sys
from board import Board
from dice import Dice

# Initialize Pygame
pygame.init()

# Set up the Pygame window
WIDTH, HEIGHT = 800, 900
SQUARE_SIZE = 600 // 10
WHITE = (255, 255, 255)

# Calculate the starting position to center the grid
start_x = (WIDTH - (10 * SQUARE_SIZE)) // 2
start_y = (HEIGHT - (10 * SQUARE_SIZE)) // 2 - 100
start_dice_x = 340
start_dice_y = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Create instances of Board and Dice
board = Board(10, 10, SQUARE_SIZE, start_x, start_y)
dice = Dice()

# Function to draw the dice button
def draw_dice_button(value, x, y):
    button_rect = pygame.Rect(x, y, 120, 80)
    pygame.draw.rect(screen, WHITE, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Dice: {value}", True, (0, 0, 0))
    
    # Adjust the button's center based on the text width
    text_rect = text.get_rect(center=(button_rect.centerx, y + button_rect.height // 2))
    screen.blit(text, text_rect)
    
    return button_rect

# Main game loop
def main():
    dice_value = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice_value = dice.roll()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    button_rect = draw_dice_button(dice_value, start_dice_x, start_dice_y)
                    if button_rect.collidepoint(event.pos):
                        dice_value = dice.roll()

        board.draw(screen)
        button_rect = draw_dice_button(dice_value, start_dice_x, start_dice_y)
        pygame.display.flip()

if __name__ == "__main__":
    main()