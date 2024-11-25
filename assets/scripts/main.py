import pygame
import math
from settings import *
from sprites import *
import random


pygame.display.set_caption("Asteroids")

#para inicializar un delta time 
clock = pygame.time.Clock() 
display = pygame.display.set_mode((SX, SY))
gg = False


class Player():
    def __init__(self):
        self.img = player_sprite
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = SX//2
        self.y = SY//2
        
        self.angle = 0
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
    def draw(self, display):
        #display.blit(self.img, (self.x, self.y, self.w, self.h))
        display.blit(self.rotateSprite, self.rotateRect)
        
    def rotate_left(self):
        self.angle += 5
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        
    def rotate_right(self):
        self.angle -= 5
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        
    def move_forward(self):
        self.x += self.cos * 6
        self.y -= self.sin * 6
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        
    def move_backwards(self):
        self.x += self.cos * 6
        self.y += self.sin * 6
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)

"""class Bullet():
    def __init__(self):
        self.img = bullet_f_big
        self.point = player.head
        self.x, self.y = self.point #list self.point
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.cos = player.cos
        self.sin = player.sin
        self.velx = self.cos * 10
        self.vely = self.sin * 10
    
    def move(self):
        self.x += self.velx
        self.y -= self.vely
        
    def draw(self, display):
        display.blit(self.img, (self.x, self.y, self.w, self.h))
    """
class Bullet():
    def __init__(self):
        self.img = bullet_f_big
        self.point = player.head
        self.x, self.y = self.point
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.cos = player.cos
        self.sin = player.sin
        self.velx = self.cos * 10
        self.vely = self.sin * 10
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Rectángulo de colisión

    def move(self):
        self.x += self.velx
        self.y -= self.vely
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rect

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

class Asteroid():
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid_s_big
        elif self.rank == 2:
            self.image = asteroid_m_sprite
        else:
            self.image = asteroid_l_sprite
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.ranPoint = random.choice([(random.randrange(0, SX-self.w), random.choice([-1*self.h - 5, SY + 5])), (random.choice([-1*self.w - 5, SX + 5]), random.randrange(0, SY - self.h))])
        self.x, self.y = self.ranPoint
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Rectángulo de colisión
        if self.x < SX//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < SY//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def move(self):
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rect

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    
def redraw_game_window():
    display.blit(bg_big, (0, 0))
    player.draw(display)
    for i in player_bullet:
        i.draw(display)
    for i in asteroids:
        i.draw(display)
    pygame.display.update()

player = Player()
player_bullet = []
asteroids = []
count = 0

run = True
#bandera para verificar si el juego esta siendo renderizado para saber si debe finalizar el codigo




while run:  
    clock.tick(60)
    count += 1
    if not gg:
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        for i in player_bullet:
            i.move()
        
        """ for a in asteroids:
            a.x += a.xv
            a.y += a.yv

            if (a.x >= player.x - player.w//2 and a.x <= player.x + player.w//2) or (a.x + a.w <= player.x + player.w//2 and a.x + a.w >= player.x - player.w//2):
                if(a.y >= player.y - player.h//2 and a.y <= player.y + player.h//2) or (a.y  +a.h >= player.y - player.h//2 and a.y + a.h <= player.y + player.h//2):
                    #lives -= 1
                    asteroids.pop(asteroids.index(a))
                    #if isSoundOn:
                    #    bangLargeSound.play()
                    break
            # coalision de bala a asteroide
            for b in player_bullet:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        if a.rank == 3:
                            #if isSoundOn:
                            #    bangLargeSound.play()
                            # score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            #if isSoundOn:
                            #    bangSmallSound.play()
                            #score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        #else:
                            #score += 30
                            #if isSoundOn:
                            #    bangSmallSound.play()
                        asteroids.pop(asteroids.index(a))
                        player_bullet.pop(player_bullet.index(b))
                        break"""
        for a in asteroids:
            a.move()
            # Colisión entre bala y asteroide
            for b in player_bullet:
                if b.rect.colliderect(a.rect):
                    if a.rank == 3:
                        na1 = Asteroid(2)
                        na2 = Asteroid(2)
                        na1.x, na1.y = a.x, a.y
                        na2.x, na2.y = a.x, a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                    elif a.rank == 2:
                        na1 = Asteroid(1)
                        na2 = Asteroid(1)
                        na1.x, na1.y = a.x, a.y
                        na2.x, na2.y = a.x, a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                    asteroids.pop(asteroids.index(a))
                    player_bullet.pop(player_bullet.index(b))
                    break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.rotate_left()
        if keys[pygame.K_d]:
            player.rotate_right()
        if keys[pygame.K_w]:
            player.move_forward()
        if keys[pygame.K_s]:
            player.move_backwards()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gg:
                    player_bullet.append(Bullet())
    redraw_game_window()
pygame.quit()           
            
