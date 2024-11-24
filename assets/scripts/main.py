import pygame
import math
from settings import *
from sprites import *


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
 

 
class Bullet():
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
    
def redraw_game_window():
    display.blit(bg_big, (0, 0))
    player.draw(display)
    for i in player_bullet:
        i.draw(display)
    pygame.display.update()

player = Player()
player_bullet = []

run = True
#bandera para verificar si el juego esta siendo renderizado para saber si debe finalizar el codigo




while run:  
    clock.tick(60)
    if not gg:
        for i in player_bullet:
            i.move()
            
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
            
