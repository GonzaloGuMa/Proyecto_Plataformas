#!/usr/bin/python3
# Proyecto python
# Autores: Gonzalo Gutiérrez Mata B53279
#          Eduardo Cubilla Barquero B92495

import pygame
from sys import exit
from random import randint
# Se utiliza para que no genere un error al cerrar


# Función para obtener el tiempo en milisegundos y contar la cantidad de puntos
def mostrar_puntos():
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
                screen.blit(rublle_s, obs_rect)
            else:
                obs_rect.x += 5
                screen.blit(small_titan_surf, obs_rect)

        obstacle_list = [obstacle for
                         obstacle in obstacle_list if obstacle.x < 1250]

        return obstacle_list

    else:
        return []


# Función para detectar colisiones en una lista y reproducir sonido
def collisions(player, obstacles):
    if obstacles:
        for obs_rect in obstacles:
            if player.colliderect(obs_rect):
                death_sound.play()
                return False
    return True


# Función para la animación del personaje principal
def eren_animation_fun():
    global eren_surf, eren_index

    if eren_rect.bottom < 470:
        eren_surf = eren_walk7_size
    else:
        eren_index += 0.1
        if eren_index >= len(eren_walk):
            eren_index = 0

        eren_surf = eren_walk[int(eren_index)]


# Función para la animcación del titán acorazado
def reiner_animation_fun():
    global reiner_surf, reiner_index
    reiner_index += 0.1
    if reiner_index >= len(reiner_frames):
        reiner_index = 0

    reiner_surf = reiner_frames[int(reiner_index)]


# Función para la animación del obstáculo (titan pequeño)
def small_titan_animation():
    global small_titan_surf, small_titan_index
    small_titan_index += 0.1
    if small_titan_index >= len(small_titan):
        small_titan_index = 0

    small_titan_surf = small_titan[int(small_titan_index)]


# Inicia pygame
pygame.init()
# Se crea objeto screen
screen = pygame.display.set_mode((1200, 480))  # (width, height)
pygame.display.set_caption('Proyecto Python')
# Objeto reloj que nos funciona para cauntizar el tiempo del juego
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/KAISG___.TTF', 50)
game_active = False
tiempo_inicial = 0
puntos = 0

# Importar imagenes para el fondo
city_background = pygame.image.load('graphics/background_mov'
                                    '/Background_OG.png').convert_alpha()
city = pygame.transform.scale(city_background, (1200, 500))

houses = pygame.image.load('graphics/background_mov'
                           '/houses.png').convert_alpha()

# ***************** Enemigos / Obstáculos ***********************

rubble_texture = pygame.image.load('graphics/rubble.png').convert_alpha()
rublle_s = pygame.transform.scale(rubble_texture, (90, 50))

# ************** Textura y Animacion del Titan pequeño ***********************

small_titan_surf1 = pygame.image.load('graphics'
                                      '/pure_titan_animation'
                                      '/titan_walk1.png').convert_alpha()

small_titan_size1 = pygame.transform.scale(small_titan_surf1, (100, 100))
small_titan1 = pygame.transform.flip(small_titan_size1, True, False)

small_titan_surf2 = pygame.image.load('graphics/pure_titan_animation/'
                                      'titan_walk2.png').convert_alpha()
small_titan_size2 = pygame.transform.scale(small_titan_surf2, (100, 100))
small_titan2 = pygame.transform.flip(small_titan_size2, True, False)

small_titan_surf3 = pygame.image.load('graphics/pure_titan_animation/'
                                      'titan_walk3.png').convert_alpha()

small_titan_size3 = pygame.transform.scale(small_titan_surf3, (100, 100))
small_titan3 = pygame.transform.flip(small_titan_size3, True, False)

small_titan_surf4 = pygame.image.load('graphics/pure_titan_animation'
                                      '/titan_walk4.png').convert_alpha()

small_titan_size4 = pygame.transform.scale(small_titan_surf4, (100, 100))
small_titan4 = pygame.transform.flip(small_titan_size4, True, False)

small_titan_surf5 = pygame.image.load('graphics/pure_titan_animation'
                                      '/titan_walk5.png').convert_alpha()

small_titan_size5 = pygame.transform.scale(small_titan_surf5, (100, 100))
small_titan5 = pygame.transform.flip(small_titan_size5, True, False)

small_titan_surf6 = pygame.image.load('graphics/pure_titan_animation'
                                      '/titan_walk6.png').convert_alpha()

small_titan_size6 = pygame.transform.scale(small_titan_surf6, (100, 100))
small_titan6 = pygame.transform.flip(small_titan_size6, True, False)

small_titan = [small_titan1,
               small_titan2,
               small_titan3,
               small_titan4,
               small_titan5,
               small_titan6]

small_titan_index = 0
small_titan_surf = small_titan[small_titan_index]


# Reiner Animation and Surface

reiner_surf1 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk1.png').convert_alpha()
reiner_frame1 = pygame.transform.scale(reiner_surf1, (350, 450))

reiner_surf2 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk2.png').convert_alpha()
reiner_frame2 = pygame.transform.scale(reiner_surf2, (350, 450))

reiner_surf3 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk3.png').convert_alpha()
reiner_frame3 = pygame.transform.scale(reiner_surf3, (350, 450))

reiner_surf4 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk4.png').convert_alpha()
reiner_frame4 = pygame.transform.scale(reiner_surf4, (350, 450))

reiner_surf5 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk5.png').convert_alpha()
reiner_frame5 = pygame.transform.scale(reiner_surf5, (350, 450))

reiner_surf6 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk6.png').convert_alpha()
reiner_frame6 = pygame.transform.scale(reiner_surf6, (350, 450))

reiner_surf7 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk7.png').convert_alpha()
reiner_frame7 = pygame.transform.scale(reiner_surf7, (350, 450))

reiner_surf8 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk8.png').convert_alpha()
reiner_frame8 = pygame.transform.scale(reiner_surf8, (350, 450))

reiner_surf9 = pygame.image.load('graphics/reiner_animation'
                                 '/reiner_walk9.png').convert_alpha()
reiner_frame9 = pygame.transform.scale(reiner_surf9, (350, 450))

reiner_frames = [reiner_frame1,
                 reiner_frame2,
                 reiner_frame3,
                 reiner_frame4,
                 reiner_frame5,
                 reiner_frame6,
                 reiner_frame7,
                 reiner_frame8,
                 reiner_frame9]

reiner_index = 0
reiner_surf = reiner_frames[reiner_index]
reiner_rect = reiner_surf.get_rect(bottomright=(1190, 475))

en_list = []

# ******************** Jugador (Texturas y Animacion) **********************

eren_walk1 = pygame.image.load('graphics/eren_animation'
                               '/eren_run1.png').convert_alpha()
eren_walk1_size = pygame.transform.scale(eren_walk1, (75, 75))

eren_walk2 = pygame.image.load('graphics/eren_animation'
                               '/eren_run2.png').convert_alpha()
eren_walk2_size = pygame.transform.scale(eren_walk2, (75, 75))

eren_walk3 = pygame.image.load('graphics/eren_animation'
                               '/eren_run3.png').convert_alpha()
eren_walk3_size = pygame.transform.scale(eren_walk3, (75, 75))

eren_walk4 = pygame.image.load('graphics/eren_animation'
                               '/eren_run4.png').convert_alpha()
eren_walk4_size = pygame.transform.scale(eren_walk4, (75, 75))

eren_walk5 = pygame.image.load('graphics/eren_animation'
                               '/eren_run5.png').convert_alpha()
eren_walk5_size = pygame.transform.scale(eren_walk5, (75, 75))

eren_walk6 = pygame.image.load('graphics/eren_animation'
                               '/eren_run6.png').convert_alpha()
eren_walk6_size = pygame.transform.scale(eren_walk6, (75, 75))

eren_walk7 = pygame.image.load('graphics/eren_animation'
                               '/eren_run7.png').convert_alpha()
eren_walk7_size = pygame.transform.scale(eren_walk7, (75, 75))

eren_walk8 = pygame.image.load('graphics/eren_animation'
                               '/eren_run8.png').convert_alpha()
eren_walk8_size = pygame.transform.scale(eren_walk8, (75, 75))

eren_walk = [eren_walk1_size,
             eren_walk2_size,
             eren_walk3_size,
             eren_walk4_size,
             eren_walk5_size,
             eren_walk6_size,
             eren_walk7_size,
             eren_walk8_size]

eren_index = 0
eren_surf = eren_walk[eren_index]
eren_rect = eren_surf.get_rect(midright=(800, 475))

player_gravity = 0

# ******************* Sonidos **************************

death_sound = pygame.mixer.Sound('sounds/tatakae.mp3')

bg_music = pygame.mixer.Sound('sounds/bg_music.mp3')
bg_music.set_volume(0.1)

bg_music2 = pygame.mixer.Sound('sounds/bg_music2.mp3')
bg_music2.set_volume(0.1)

# ****************  Timers *******************************
# el +1 o +2 es para evitar conflicto con los eventos
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)  # tiempo en milisegundos

small_titan_timer = pygame.USEREVENT + 2
pygame.time.set_timer(small_titan_timer, 200)

# ************** Movimiento del Fondo ********************
muralla_mov = 0
casas_mov = 0

bg_music.play()

while True:
    # Se utiliza para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Evento de mecánica del salto
        if game_active:
            if event.type == pygame.KEYDOWN and eren_rect.bottom >= 475:
                if event.key == pygame.K_SPACE:
                    player_gravity = -16

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                tiempo_inicial = int(pygame.time.get_ticks() / 100)

        # Para poder alternar entre obstaculos se crea este evento que depende
        # del numero aleatorio generado por randint
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    en_list.append(rublle_s.get_rect(bottomleft=(randint(-200, -50), 474)))  # noqa
                else:
                    en_list.append(small_titan_surf.get_rect(bottomleft=(randint(-200, -50), 475)))  # noqa

    if game_active:
        # blit poner una superficie en otra
        screen.fill((0, 0, 0))
        screen.blit(city, (muralla_mov, -200))
        screen.blit(houses, (casas_mov, 120))

        screen.blit(city, (-1200 + muralla_mov, -200))
        screen.blit(houses, (-1250 + casas_mov, 120))

        if muralla_mov == 6000:
            screen.blit(city, (-1200 + muralla_mov, -200))
            screen.blit(houses, (-1250 + casas_mov, 120))
            muralla_mov = 0
            casas_mov = 0

        elif casas_mov == 1250:
            screen.blit(city, (-1200 + muralla_mov, -200))
            screen.blit(houses, (-1250 + casas_mov, 120))
            casas_mov = 0
            muralla_mov = 0

        muralla_mov += 0.5
        casas_mov += 1.25

        puntos = mostrar_puntos()

        # ***************** Enemigos ***********************

        reiner_animation_fun()
        screen.blit(reiner_surf, reiner_rect)

        small_titan_animation()
        # ***************** Player *************************
        player_gravity += 0.5
        eren_rect.y += player_gravity
        if eren_rect.bottom >= 475:
            eren_rect.bottom = 475

        eren_animation_fun()
        screen.blit(eren_surf, eren_rect)

        en_list = mov_enemigo(en_list)

        # colisión y muerte
        game_active = collisions(eren_rect, en_list)

    # Menú Principal y después menú de continuar
    else:
        if puntos != 0:
            bg_music.stop()
            bg_music.play()
            pts_won = test_font.render('Tu puntuación: '
                                       '{}'.format(puntos), False, ('Red'))

            pts_won_rect = pts_won.get_rect(center=(900, 250))

            screen.fill((0, 0, 0))
            screen.blit(pts_won, pts_won_rect)
            tatakae = pygame.image.load('graphics/'
                                        'space_continue'
                                        '.png').convert_alpha()

            continuar = pygame.transform.scale(tatakae, (500, 480))
            screen.blit(continuar, (0, 0))

        else:
            bg_music.play()
            menu_background = pygame.image.load('graphics/'
                                                'menu_inicio'
                                                '.png').convert_alpha()

            menu = pygame.transform.scale(menu_background, (1200, 500))

            screen.blit(menu, (0, 0))

        en_list.clear()
        eren_rect.midright = (800, 475)
        player_gravity = 0

    # actualiza la ventana creada con el obj screen
    pygame.display.update()
    # Frame rate del juego, max frame rate
    clock.tick(60)
