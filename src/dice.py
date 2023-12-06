import pygame
import random

class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.value = 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)
