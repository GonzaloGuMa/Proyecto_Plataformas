#!/usr/bin/python3

import pygame
from sys import exit
from random import randint
# Se utiliza para que no genere un error al cerrar

def mostrar_puntos(): # noqa
    tiempo = int(pygame.time.get_ticks() / 100) - tiempo_inicial
    score_surface = test_font.render('Puntos: {}'.format(tiempo), False, 'Red')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return tiempo

# Funcion para mover a los enemigos
def mov_enemigo(obstacle_list):
    if obstacle_list:
        for obs_rect in obstacle_list:
            obs_rect.x += 4

            if obs_rect.bottom == 474:
                obs_rect.x += 1
                screen.blit(rubble_size, obs_rect)
            else:
                obs_rect.x += 5
                screen.blit(small_titan, obs_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x < 1250]

        return obstacle_list

    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obs_rect in obstacles:
            if player.colliderect(obs_rect):
                return False
    return True

def eren_animation_fun():
    global eren_surf, eren_index

    if eren_rect.bottom < 470:
        eren_surf = eren_walk7_size
    else:
        eren_index += 0.1
        if eren_index >= len(eren_walk):
            eren_index = 0

        eren_surf = eren_walk[int(eren_index)]


# Inicia pygame
pygame.init() # noqa
screen = pygame.display.set_mode((1200, 500))  # (width, height)
pygame.display.set_caption('PROJECT GAME')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/KAISG___.TTF', 50)
game_active = False
tiempo_inicial = 0
puntos = 0

# Importar imagenes para el fondo
city_background = pygame.image.load('graphics/fondo.jpg').convert_alpha()
city = pygame.transform.scale(city_background, (1200, 500))

ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
ground = pygame.transform.scale(ground_surface, (1200, 500))

# score_surface = test_font.render('Sobrevive...', True, 'Red')  # (texto, AA, color) # noqa
# score_rect = score_surface.get_rect(center=(600, 50))

# ***************** Enemigos / Obstáculos ***********************

rubble_texture = pygame.image.load('graphics/rubble.png').convert_alpha()  # noqa
rubble_size = pygame.transform.scale(rubble_texture, (90, 50))


small_titan_surf = pygame.image.load('graphics/pure_titan.png').convert_alpha()
small_titan_size = pygame.transform.scale(small_titan_surf, (100, 100))
small_titan = pygame.transform.flip(small_titan_size, True, False)

reiner_texture = pygame.image.load('graphics/reiner_2.png').convert_alpha()  # noqa
reiner_size = pygame.transform.scale(reiner_texture, (350, 450))
reiner_rect = reiner_size.get_rect(bottomright=(1190, 475))

lista_enemigos = []

# ******************** Jugador (Texturas y Animacion) **********************

eren_walk1 = pygame.image.load('graphics/eren_animation/eren_run1.png').convert_alpha()
eren_walk1_size = pygame.transform.scale(eren_walk1, (75, 75))

eren_walk2 = pygame.image.load('graphics/eren_animation/eren_run2.png').convert_alpha()
eren_walk2_size = pygame.transform.scale(eren_walk2, (75, 75))

eren_walk3 = pygame.image.load('graphics/eren_animation/eren_run3.png').convert_alpha()
eren_walk3_size = pygame.transform.scale(eren_walk3, (75, 75))

eren_walk4 = pygame.image.load('graphics/eren_animation/eren_run4.png').convert_alpha()
eren_walk4_size = pygame.transform.scale(eren_walk4, (75, 75))

eren_walk5 = pygame.image.load('graphics/eren_animation/eren_run5.png').convert_alpha()
eren_walk5_size = pygame.transform.scale(eren_walk5, (75, 75))

eren_walk6 = pygame.image.load('graphics/eren_animation/eren_run6.png').convert_alpha()
eren_walk6_size = pygame.transform.scale(eren_walk6, (75, 75))

eren_walk7 = pygame.image.load('graphics/eren_animation/eren_run7.png').convert_alpha()
eren_walk7_size = pygame.transform.scale(eren_walk7, (75, 75))

eren_walk8 = pygame.image.load('graphics/eren_animation/eren_run8.png').convert_alpha()
eren_walk8_size = pygame.transform.scale(eren_walk8, (75, 75))

eren_walk = [eren_walk1_size, eren_walk2_size, eren_walk3_size, eren_walk4_size, eren_walk5_size, eren_walk6_size, eren_walk7_size, eren_walk8_size]
eren_index = 0
eren_surf = eren_walk[eren_index]

eren_rect = eren_surf.get_rect(midright=(800, 475))

player_gravity = 0

# ******************* Sonidos **************************

jump_sound = pygame.mixer.Sound('sounds/tatakae.mp3')

bg_music = pygame.mixer.Sound('sounds/bg_music2.mp3')
bg_music.set_volume(0.1)

# Timer
# el +1 es para evitar conflicto con los eventos
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)  # (evento a triggerear, tiempo en milisegundos)

while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN and eren_rect.bottom >= 475:
                if event.key == pygame.K_SPACE:
                    jump_sound.play()
                    player_gravity = -15

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                tiempo_inicial = int(pygame.time.get_ticks() / 100)

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                lista_enemigos.append(rubble_size.get_rect(bottomleft=(randint(-200,-50), 474)))

            else:
                lista_enemigos.append(small_titan.get_rect(bottomleft=(randint(-200,-50), 475)))


    if game_active:
        # blit poner una superficie en otra
        screen.blit(city, (0, 0))
        screen.blit(ground, (0, 80))  # screen.blit(score_surface, score_rect)
        puntos = mostrar_puntos()

        # ***************** Enemigos ***********************

        screen.blit(reiner_size, reiner_rect)

        # ***************** Player *************************
        player_gravity += 0.5
        eren_rect.y += player_gravity
        if eren_rect.bottom >= 475:
            eren_rect.bottom = 475

        eren_animation_fun()
        screen.blit(eren_surf, eren_rect)

        lista_enemigos = mov_enemigo(lista_enemigos)

        # colisión y muerte
        game_active = collisions(eren_rect, lista_enemigos)

    else:


        instrucciones_background = pygame.image.load('graphics/instrucciones.jpg').convert_alpha() # noqa
        instrucciones = pygame.transform.scale(instrucciones_background, (1200, 500)) # noqa

        screen.blit(instrucciones, (0, 0))

        lista_enemigos.clear()
        eren_rect.midright=(800, 475)
        player_gravity = 0

        puntos_ganados = test_font.render('Tu puntuación: {}'.format(puntos), False, ('Red'))
        puntos_ganados_rect = puntos_ganados.get_rect(center=(550, 250))

        if puntos != 0:
            bg_music.stop()
            bg_music.play()
            screen.blit(puntos_ganados, puntos_ganados_rect)
        else:
            bg_music.play(loops=-1)

    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
