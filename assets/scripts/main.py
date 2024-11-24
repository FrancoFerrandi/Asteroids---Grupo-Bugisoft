import pygame
from sprites import *
from settings import *

pygame.display.set_caption("Asteroids")

#para inicializar un delta time
clock = pygame.time.Clock()
display = pygame.display.set_mode((SX, SY))


gg = False

def redrawGameWindow():
    display.blit(bg, (0, 0))
    pygame.display.update()


run = True
#bandera para verificar si el juego esta siendo renderizado para saber si debe finalizar el codigo
while run:
    clock.tick(60)
    if not gg:
        pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow()
pygame.quit()           
            
