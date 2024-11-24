import pygame

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
heal_big = pygame.transform.scale(heal_sprite, (1500, 1500))

fakeheal_sprite = pygame.image.load("assets/sprites/star_e.png")
fakeheal_big = pygame.transform.scale(fakeheal_sprite, (1500, 1500))

#balas

bullet_e_sprite = pygame.image.load("assets/sprites/bullet_e.png")
bullet_e_big = pygame.transform.scale(bullet_e_sprite, (10, 10))

bullet_f_sprite = pygame.image.load("assets/sprites/bullet_f.png")
bullet_f_big = pygame.transform.scale(bullet_f_sprite, (10, 10))

#asteroides

asteroid_s_sprite = pygame.image.load("assets/sprites/asteroid_s.png")
asteroid_s_big = pygame.transform.scale(asteroid_s_sprite, (1500, 1500))

asteroid_m_sprite = pygame.image.load("assets/sprites/asteroid_m.png")
asteroid_m_big = pygame.transform.scale(asteroid_m_sprite, (1500, 1500))

asteroid_l_sprite = pygame.image.load("assets/sprites/asteroid_L.png")
asteroid_l_big = pygame.transform.scale(asteroid_l_sprite, (1500, 1500))