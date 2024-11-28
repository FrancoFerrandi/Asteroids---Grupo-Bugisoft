import pygame


SX = 720
SY = 720


#VELOCIDADES
PLAYER_VEL = 6 #DEFAULT 6
PLAYER_ROTATION_VEL = 5 #DEFAULT 5

BULLET_VEL = 10 #DEFAULT 10

ASTEROID_VEL = 1 #DEFAULT 1

FAKEHEAL_VEL = 2
HEAL_VEL = 2




#VOLUMEN
GAMEOST_VOLUME = 0.3 #DEFAULT 0.3
SHOOT_VOLUME = 1
EXPLOSION_VOLUME = 1
PICKUP_VOLUME = 1
SELECT_VOLUME = 1
DEAD_VOLUME = 1
HIT_VOLUME = 1

SFX_VOLUME = 1

# Variables de juego.py

clock = pygame.time.Clock() 
display = pygame.display.set_mode((SX, SY))
gg = False
lives = 3
score = 0
fire_boost = False
f_boost = -1
isSoundOn = True

player_bullet = []
asteroids = []
stars = []
count = 0

run = True # bandera para verificar si el juego esta siendo renderizado para saber si debe finalizar el codigo

