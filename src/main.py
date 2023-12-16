import pygame
from snakes_ladders.constants import WIDTH, HEIGHT
from board import Board
from dice import Dice
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption('Snakes and Ladders: OODP Project')

def main():
    global current_player, player1, player2
    run = True
    clock = pygame.time.Clock()

    board = Board(x=20, y=20)
    dice = Dice(x=WIDTH - 100, y=HEIGHT // 2 - 50 // 2)

    player1 = Player("Chacha Varun", (255, 0, 0, 128))
    player2 = Player("Dadda Pareek", (0, 0, 255, 128))

    player1.set_board(board)
    player2.set_board(board)

    current_player = player1

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

            if event.type == pygame.KEYDOWN: # HAA 'or' se ho skta hai lekin mai aalsi hu ~~Rizzler 2.0
                if event.key == pygame.K_SPACE:
                    dice.roll()
                    steps = dice.value
                    current_player.move(steps)
                    switch_player()

        if current_player.position >= 100:
            winner_message = f"{current_player.name} wins!"
            font = pygame.font.Font(None, 22)
            text = font.render(winner_message, True, (207, 52, 118))  # Magenta hai ye Yuvraj!!!
            text_rect = text.get_rect(midtop=(dice.rect.centerx - 20, dice.rect.top - 10)) 
            
            
            box_width, box_height = text.get_width() + 20, text.get_height() + 20
            box_rect = pygame.Rect(dice.rect.centerx - box_width // 2 - 20, dice.rect.top - box_height - 10, box_width, box_height)  
            
            pygame.draw.rect(screen, (255, 255, 255), box_rect)  
            pygame.draw.rect(screen, (0, 0, 0), box_rect, 2)  

            text_rect.topleft = (box_rect.left + 10, box_rect.top + 10)  

            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(3000)
            run = False

        board.draw(screen)
        dice.draw(screen)
        player1.draw_token(screen)
        player2.draw_token(screen)

        pygame.display.flip()

    pygame.quit()

def switch_player():
    global current_player, player1, player2
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

if __name__ == "__main__":
    main()
