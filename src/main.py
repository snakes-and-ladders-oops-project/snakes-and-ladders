import pygame
import pygame_gui
from player import Player
from board import Board
from dice import Dice
from spritesheet import SpriteSheet

def initialize_game():
    pygame.init()
    WIDTH = 800
    HEIGHT = 640
    COLS = 10
    MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
    
    # Create text input elements for player names
    player1_name_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 100), (150, 30)),
        manager=MANAGER,
        object_id="#player1_name"
    )
    player1_name_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 100), (80, 30)),
        text="Player 1 Name:",
        manager=MANAGER
    )
    
    player2_name_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 150), (150, 30)),
        manager=MANAGER,
        object_id="#player2_name"
    )
    player2_name_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 150), (80, 30)),
        text="Player 2 Name:",
        manager=MANAGER
    )
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 60
    pygame.display.set_caption('Snakes and Ladders: OODP Project')
    icon = pygame.image.load('img/logo.png')
    pygame.display.set_icon(icon)
    
    return WIDTH, HEIGHT, COLS, MANAGER, player1_name_input, player2_name_input, screen, FPS

def load_player_images(sprite_sheet):
    BLACK = (0, 0, 0)
    player1_img = sprite_sheet.get_image(0, 16, 20, BLACK)
    player2_img = sprite_sheet.get_image(1, 16, 20, BLACK)
    return player1_img, player2_img

def main_game_loop(screen, FPS, players, dice, COLS):
    run = True
    clock = pygame.time.Clock()
    current_player_index = 0

    while run:
        UI_REFRESH_RATE = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            MANAGER.process_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dice.rect.collidepoint(event.pos):
                    dice.roll()
                    steps = dice.value
                    players[current_player_index].move(steps)
                    current_player_index = (current_player_index + 1) % len(players)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice.roll()
                    steps = dice.value
                    players[current_player_index].move(steps)
                    current_player_index = (current_player_index + 1) % len(players) if steps != 6 else current_player_index

        winner, winner_message = check_for_winner(players, current_player_index, COLS)
        if winner:
            show_winner_message(winner_message, dice.rect)
            pygame.time.delay(3000)
            run = False

        board.draw(screen)
        dice.draw(screen)
        for player in players:
            player.draw_token(screen)

        # Display current player's turn below the dice in the Pygame window
        font = pygame.font.Font(None, 22)
        text = font.render(f"{players[current_player_index].name}'s turn", True, (0, 0, 0))
        text_rect = text.get_rect(midtop=(WIDTH - 100 + 50, HEIGHT // 2 - 50 // 2 + 60))
        screen.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()

def check_for_winner(players, current_player_index, col_count):
    if players[current_player_index].position >= col_count * col_count:
        return True, f"{players[current_player_index].name} wins!"
    return False, None

def show_winner_message(message, dice_rect):
    font = pygame.font.Font(None, 22)
    text = font.render(message, True, (207, 52, 118))
    text_rect = text.get_rect(midtop=(dice_rect.centerx - 20, dice_rect.top - 10))

    box_width, box_height = text.get_width() + 20, text.get_height() + 20
    box_rect = pygame.Rect(
        dice_rect.centerx - box_width // 2 - 20,
        dice_rect.top - box_height - 10,
        box_width,
        box_height
    )

    pygame.draw.rect(screen, (255, 255, 255), box_rect)
    pygame.draw.rect(screen, (0, 0, 0), box_rect, 2)

    text_rect.topleft = (box_rect.left + 10, box_rect.top + 10)

    screen.blit(text, text_rect)
    pygame.display.flip()

if __name__ == "__main__":
    WIDTH, HEIGHT, COLS, MANAGER, player1_name_input, player2_name_input, screen, FPS = initialize_game()
    
    # Add a loop to wait for user input (for demonstration purposes)
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
                
            MANAGER.process_events(event)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player1_name = player1_name_input.get_text()
                player2_name = player2_name_input.get_text()
                waiting_for_input = False
    
        MANAGER.update(1 / FPS)
        MANAGER.draw_ui(screen)
        pygame.display.flip()

    sprite_sheet = SpriteSheet(pygame.image.load('img/player.png').convert_alpha())
    player1_img, player2_img = load_player_images(sprite_sheet)
    board = Board(x=20, y=20)
    dice = Dice(x=WIDTH - 100, y=HEIGHT // 2 - 50 // 2)
    player1 = Player(player1_name, (255, 0, 0, 128), player_image=player1_img)
    player2 = Player(player2_name, (0, 0, 255, 128), player_image=player2_img)
    player1.set_board(board)
    player2.set_board(board)
    players = [player1, player2]

    main_game_loop(screen, FPS, players, dice, COLS)
