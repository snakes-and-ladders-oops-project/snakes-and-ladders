import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))

running = True

pygame.display.set_caption("Snakes and Ladders - OODP Project, Group 2")
icon = pygame.image.load('src/img/logo.png')
pygame.display.set_icon(icon)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False