import pygame
from settings import BULLET_SIZE

pygame.font.init()

#scaled_sprite = pygame.transform.scale(sprite, (100, 100))

bg = pygame.image.load("assets/sprites/background.png")
bg_big = pygame.transform.scale(bg, (1500, 1500))

#jugador y enemigo

player_sprite = pygame.image.load("assets/sprites/triangle.png")
player_big = pygame.transform.scale(player_sprite, (1500, 1500))

enemy_sprite = pygame.image.load("assets/sprites/enemy.png")
enemy_big = pygame.transform.scale(enemy_sprite, (1500, 1500))

#objetos interactivos

heal_sprite = pygame.image.load("assets/sprites/star_f.png")
heal_big = pygame.transform.scale(heal_sprite, (30, 30))

fakeheal_sprite = pygame.image.load("assets/sprites/star_e.png")
fakeheal_big = pygame.transform.scale(fakeheal_sprite, (30, 30))

#balas

bullet_e_sprite = pygame.image.load("assets/sprites/bullet_e.png")
bullet_e_big = pygame.transform.scale(bullet_e_sprite, (10, 10))

bullet_f_sprite = pygame.image.load("assets/sprites/bullet_f.png")
bullet_f_big = pygame.transform.scale(bullet_f_sprite, (BULLET_SIZE, BULLET_SIZE))

#asteroides

asteroid_s_sprite = pygame.image.load("assets/sprites/asteroid_s.png")
asteroid_s_big = pygame.transform.scale(asteroid_s_sprite, (30, 30))

asteroid_m_sprite = pygame.image.load("assets/sprites/asteroid_m.png")
asteroid_m_big = pygame.transform.scale(asteroid_m_sprite, (65, 65))

asteroid_l_sprite = pygame.image.load("assets/sprites/asteroid_L.png")
asteroid_l_big = pygame.transform.scale(asteroid_l_sprite, (100, 100))

#logo
logo = pygame.image.load("assets/sprites/logo.png")
logo_grande = logo_grande = pygame.transform.scale(logo, (350,350))

#fuente menu # (Utilizamos la fuente DejaVuSans ya que es una fuente que admite los simbolos de flechas y barra espaciadora)
deja_vu_sans = pygame.font.Font("assets/sprites/DejaVuSans.ttf")
fuente_titulo = pygame.font.Font("assets/sprites/DejaVuSans.ttf", (64)) 
fuente_menu = pygame.font.Font("assets/sprites/DejaVuSans.ttf", (40))