#!/usr/bin/python3

import pygame
from sys import exit
# Se utiliza para que no genere un error al cerrar

# Inicia pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))  # (width, height)
pygame.display.set_caption('PROJECT GAME')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/KAISG___.TTF', 50)

# Importar imagenes para el fondo
city_background = pygame.image.load('graphics/background')
ground_surface = pygame.image.load('graphics/floor.png')
text_surface = test_font.render('Sobrevive...', False, 'Red')  # (texto, AA, color) # noqa


while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # blit poner una superficie en otra
    screen.blit(city_background, (0, 0))
    screen.blit(ground_surface, (0, 50))
    screen.blit(text_surface, (300, 50))

    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
