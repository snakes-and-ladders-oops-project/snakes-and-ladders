import pygame
from player import Player
from board import Board  # Import the updated Board class
from dice import Dice
from spritesheet import SpriteSheet

pygame.init()

# Constants
HEIGHT = 640
WIDTH = 800
COLS = 10
SQUARE_SIZE = WIDTH // COLS

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption('Snakes and Ladders: OODP Project')
icon = pygame.image.load('src/img/logo.png')
pygame.display.set_icon(icon)

# Load player sprites   
playerSprite = pygame.image.load('src/img/player.png').convert_alpha()
sprite_sheet = SpriteSheet(playerSprite)

# Create player images
BLACK = (0, 0, 0)
player1_img = sprite_sheet.get_image(0, 16, 20, BLACK)
player2_img = sprite_sheet.get_image(1, 16, 20, BLACK)

# Create player instances
player1 = Player("Chacha Varun", (255, 0, 0, 128), player_image=player1_img)
player2 = Player("Dadda Pareek", (0, 0, 255, 128), player_image=player2_img)

# Set up board and dice using the updated Board class
board = Board(x=20, y=20)
dice = Dice(x=WIDTH - 100, y=HEIGHT // 2 - 50 // 2)

player1.set_board(board)
player2.set_board(board)

current_player = player1

def switch_player():
    global current_player, player1, player2
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

# Main game loop
run = True
clock = pygame.time.Clock()

# Initialize box_rect with a default value
box_rect = pygame.Rect(0, 0, 0, 0)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if dice.rect.collidepoint(event.pos):
                dice.roll()
                steps = dice.value
                current_player.move(steps)
                switch_player()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice.roll()
                steps = dice.value
                current_player.move(steps)
                switch_player()

    # Check for winner
    if current_player.position >= COLS * COLS:
        winner_message = f"{current_player.name} wins!"
        font = pygame.font.Font(None, 22)
        text = font.render(winner_message, True, (207, 52, 118))
        text_rect = text.get_rect(midtop=(dice.rect.centerx - 20, dice.rect.top - 10))

        box_width, box_height = text.get_width() + 20, text.get_height() + 20
        box_rect = pygame.Rect(
            dice.rect.centerx - box_width // 2 - 20,
            dice.rect.top - box_height - 10,
            box_width,
            box_height
        )

        pygame.draw.rect(screen, (255, 255, 255), box_rect)
        pygame.draw.rect(screen, (0, 0, 0), box_rect, 2)

        text_rect.topleft = (box_rect.left + 10, box_rect.top + 10)

        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        run = False

    # Draw board, dice, and players
    board.draw(screen)
    dice.draw(screen)
    player1.draw_token(screen)
    player2.draw_token(screen)

    pygame.display.flip()

pygame.quit()
