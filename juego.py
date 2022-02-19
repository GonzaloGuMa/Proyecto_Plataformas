#!/usr/bin/python3

import pygame
from sys import exit
# Se utiliza para que no genere un error al cerrar

def mostrar_puntos(): # noqa
    tiempo = int(pygame.time.get_ticks() / 100) - tiempo_inicial
    score_surface = test_font.render('Puntos: {}'.format(tiempo), False, 'Red')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)

# Inicia pygame
pygame.init() # noqa
screen = pygame.display.set_mode((1200, 400))  # (width, height)
pygame.display.set_caption('PROJECT GAME')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/KAISG___.TTF', 50)
game_active = False
tiempo_inicial = 0

# Importar imagenes para el fondo
city_background = pygame.image.load('graphics/fondo.jpg').convert_alpha()
city = pygame.transform.scale(city_background, (1200, 400))

ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
ground = pygame.transform.scale(ground_surface, (1200, 400))

# score_surface = test_font.render('Sobrevive...', True, 'Red')  # (texto, AA, color) # noqa
# score_rect = score_surface.get_rect(center=(600, 50))

# obstacle = pygame.Rect(80, 300, 80, 80)

rubble_texture = pygame.image.load('graphics/rubble.png').convert_alpha()  # noqa
rubble_size = pygame.transform.scale(rubble_texture, (90, 50))
rubble_rect = rubble_size.get_rect(topleft=(80, 320))

reiner_texture = pygame.image.load('graphics/ReinerRunning.png').convert_alpha()  # noqa
reiner_size = pygame.transform.scale(reiner_texture, (350, 350))
reiner_rect = reiner_size.get_rect(bottomright=(1190, 375))

player_surface = pygame.image.load('graphics/eren_running.png').convert_alpha()
eren = pygame.transform.scale(player_surface, (75, 75))
eren_rect = eren.get_rect(midright=(800, 400))

player_gravity = 0


while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN and eren_rect.bottom >= 375:
                if event.key == pygame.K_SPACE:
                    player_gravity = -15

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                rubble_rect.right = 80
                tiempo_inicial = int(pygame.time.get_ticks() / 100)

    if game_active:
        # blit poner una superficie en otra
        screen.blit(city, (0, 0))
        screen.blit(ground, (0, 80))  # screen.blit(score_surface, score_rect)
        mostrar_puntos()

        # Movimiento de los escombros
        rubble_rect.x += 4
        if rubble_rect.right >= 1300:
            rubble_rect.left = 0

        screen.blit(rubble_size, rubble_rect)

        # ***************** Enemigos ***********************

        screen.blit(reiner_size, reiner_rect)

        # ***************** Player *************************
        player_gravity += 0.5
        eren_rect.y += player_gravity
        if eren_rect.bottom >= 375:
            eren_rect.bottom = 375

        screen.blit(eren, eren_rect)

        # colisión y muerte
        if rubble_rect.colliderect(eren_rect):
            game_active = False

    else:
        instrucciones_background = pygame.image.load('graphics/instrucciones.jpg').convert_alpha() # noqa
        instrucciones = pygame.transform.scale(instrucciones_background, (1200, 400)) # noqa
        screen.blit(instrucciones, (0, 0))

    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
