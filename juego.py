#!/usr/bin/python3

import pygame
from sys import exit
# Se utiliza para que no genere un error al cerrar

# Inicia pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))  # (width, height)
pygame.display.set_caption('PROJECT GAME')
clock = pygame.time.Clock()

while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
