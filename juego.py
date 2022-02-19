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
city_background = pygame.image.load('graphics/background').convert_alpha()
city = pygame.transform.scale(city_background, (800, 400))

ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
ground = pygame.transform.scale(ground_surface, (800, 400))

text_surface = test_font.render('Sobrevive...', True, 'Red')  # (texto, AA, color) # noqa

reiner_texture = pygame.image.load('graphics/ReinerRunning.png').convert_alpha()  # noqa
reiner = pygame.transform.scale(reiner_texture, (200, 200))
reiner_x_pos = 600

player_surface = pygame.image.load('graphics/eren_running.png').convert_alpha()
eren = pygame.transform.scale(player_surface, (75, 75))

while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # blit poner una superficie en otra
    screen.blit(city, (0, 0))
    screen.blit(ground, (0, 50))
    screen.blit(text_surface, (300, 50))

    reiner_x_pos -= 4
    if reiner_x_pos < -200:
        reiner_x_pos = 800

    screen.blit(reiner, (reiner_x_pos, 200))
    screen.blit(eren, (80, 300))

    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
