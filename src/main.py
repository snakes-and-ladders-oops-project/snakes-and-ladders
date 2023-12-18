import pygame
import pygame_gui
from player import Player
from board import Board
from dice import Dice
from spritesheet import SpriteSheet

class Game:
    def __init__(self, width, height, cols, fps):
        self.WIDTH = width
        self.HEIGHT = height
        self.COLS = cols
        self.FPS = fps
        self.players = []
        self.current_player_index = 0
        self.board = None
        self.dice = None
        self.screen = None
        self.manager = None
        self.player1_name_input = None
        self.player2_name_input = None

    def initialize_game(self):
        pygame.init()
        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))

        # Create text input elements for player names
        self.player1_name_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((120, 100), (150, 30)),
            manager=self.manager,
            object_id="#player1_name"
        )
        player1_name_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 100), (80, 30)),
            text="Player 1:",
            manager=self.manager
        )

        self.player2_name_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((120, 150), (150, 30)),
            manager=self.manager,
            object_id="#player2_name"
        )
        player2_name_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 150), (80, 30)),
            text="Player 2:",
            manager=self.manager
        )

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Snakes and Ladders: OODP Project')
        icon = pygame.image.load('img/logo.png')
        pygame.display.set_icon(icon)

    def load_player_images(self, sprite_sheet):
        BLACK = (0, 0, 0)
        player1_img = sprite_sheet.get_image(0, 16, 20, BLACK)
        player2_img = sprite_sheet.get_image(1, 16, 20, BLACK)
        return player1_img, player2_img

    def main_game_loop(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            UI_REFRESH_RATE = clock.tick(self.FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                self.manager.process_events(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dice.rect.collidepoint(event.pos):
                        self.dice.roll()
                        steps = self.dice.value
                        self.players[self.current_player_index].move(steps)
                        self.current_player_index = (self.current_player_index + 1) % len(self.players)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dice.roll()
                        steps = self.dice.value
                        self.players[self.current_player_index].move(steps)
                        self.current_player_index = (self.current_player_index + 1) % len(self.players) if steps != 6 else self.current_player_index

            winner, winner_message = self.check_for_winner()
            if winner:
                self.show_winner_message(winner_message, self.dice.rect)
                pygame.time.delay(3000)
                run = False

            self.board.draw(self.screen)
            self.dice.draw(self.screen)
            for player in self.players:
                player.draw_token(self.screen)

            font = pygame.font.Font(None, 22)
            text = font.render(f"{self.players[self.current_player_index].name}'s turn", True, (0, 0, 0))
            text_rect = text.get_rect(midtop=(self.WIDTH - 100 + 25, self.HEIGHT // 2 - 50 // 2 + 60))
            self.screen.blit(text, text_rect)

            pygame.display.flip()

        pygame.quit()

    def check_for_winner(self):
        if self.players[self.current_player_index].position >= self.COLS * self.COLS:
            return True, f"{self.players[self.current_player_index].name} wins!"
        return False, None

    def show_winner_message(self, message, dice_rect):
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

        pygame.draw.rect(self.screen, (255, 255, 255), box_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), box_rect, 2)

        text_rect.topleft = (box_rect.left + 10, box_rect.top + 10)

        self.screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == "__main__":
    WIDTH, HEIGHT, COLS, FPS = 800, 640, 10, 60
    game = Game(WIDTH, HEIGHT, COLS, FPS)

    game.initialize_game()

    # Add a loop to wait for user input (for demonstration purposes)
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False

            game.manager.process_events(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player1_name = game.player1_name_input.get_text()
                player2_name = game.player2_name_input.get_text()
                waiting_for_input = False

        game.manager.update(1 / game.FPS)
        game.manager.draw_ui(game.screen)
        pygame.display.flip()

    sprite_sheet = SpriteSheet(pygame.image.load('img/player.png').convert_alpha())
    player1_img, player2_img = game.load_player_images(sprite_sheet)
    game.board = Board(x=20, y=20)
    game.dice = Dice(x=WIDTH - 100, y=HEIGHT // 2 - 50 // 2)
    player1 = Player(player1_name, (255, 0, 0, 128), player_image=player1_img)
    player2 = Player(player2_name, (0, 0, 255, 128), player_image=player2_img)
    player1.set_board(game.board)
    player2.set_board(game.board)
    game.players = [player1, player2]

    game.main_game_loop()
