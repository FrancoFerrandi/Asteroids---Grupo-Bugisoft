import pygame
from settings import *
from sprites import *


pygame.display.set_caption("Asteroids")

#para inicializar un delta time 
clock = pygame.time.Clock() 
display = pygame.display.set_mode((SX, SY))


gg = False


class Player(object):
    def __init__(self):
        self.img = player_sprite
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = SX//2
        self.y = SY//2
        
    def draw(self, display):
        display.blit(self.img, (self.x, self.y, self.w, self.h))


def redrawGameWindow():
    display.blit(bg_big, (0, 0))
    player.draw(display)
    pygame.display.update()


run = True
#bandera para verificar si el juego esta siendo renderizado para saber si debe finalizar el codigo

player = Player()



while run:
    clock.tick(60)
    if not gg:
        pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow()
pygame.quit()           
            
