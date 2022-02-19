#!/usr/bin/python3

import pygame
from sys import exit
# Se utiliza para que no genere un error al cerrar

# Inicia pygame
pygame.init()
screen = pygame.display.set_mode((1200, 400))  # (width, height)
pygame.display.set_caption('PROJECT GAME')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/KAISG___.TTF', 50)

# Importar imagenes para el fondo
city_background = pygame.image.load('graphics/fondo.jpg').convert_alpha()
city = pygame.transform.scale(city_background, (1200, 400))

ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
ground = pygame.transform.scale(ground_surface, (1200, 400))

score_surface = test_font.render('Sobrevive...', True, 'Red')  # (texto, AA, color) # noqa
score_rect = score_surface.get_rect(center=(600, 50))

reiner_texture = pygame.image.load('graphics/ReinerRunning.png').convert_alpha()  # noqa
reiner_size = pygame.transform.scale(reiner_texture, (300, 300))
reiner_rect = reiner_size.get_rect(bottomright=(1175, 375))

rubble_texture = pygame.image.load('graphics/rubble.png').convert_alpha()  # noqa
rubble_size = pygame.transform.scale(rubble_texture, (50, 50))
rubble_rect = rubble_size.get_rect(bottomright=(80, 375))

player_surface = pygame.image.load('graphics/eren_running.png').convert_alpha()
eren = pygame.transform.scale(player_surface, (75, 75))
eren_rect = eren.get_rect(bottomleft=(800, 375))

player_gravity = 0


while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and eren_rect.bottom >= 375:
            if event.key == pygame.K_SPACE:
                player_gravity = -17

    # blit poner una superficie en otra
    screen.blit(city, (0, 0))
    screen.blit(ground, (0, 80))
    screen.blit(score_surface, score_rect)

    # Movimiento de los escombros
    rubble_rect.x += 4
    if rubble_rect.right >= 1300:
        rubble_rect.left = 0

    screen.blit(rubble_size, rubble_rect)

    # ***************** Enemigos ***********************

    screen.blit(reiner_size, reiner_rect)

    # ***************** Player *************************
    # print(eren_rect.left)
    player_gravity += 1
    eren_rect.y += player_gravity
    if eren_rect.bottom >= 375:
        eren_rect.bottom = 375

    screen.blit(eren, eren_rect)

    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
