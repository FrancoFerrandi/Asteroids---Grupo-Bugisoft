import pygame
import math
from settings import *
from sprites import *
import random

pygame.init() # inicializa todos los módulos de Pygame que sean necesarios para ejecutar un juego o aplicación (display, font, event)

pygame.display.set_caption("Asteroids")

#para inicializar un delta time 
clock = pygame.time.Clock() 
display = pygame.display.set_mode((SX, SY))
gg = False
lives = 3

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
        self.rect = pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)  # Rectángulo de colisión contra asteroides y balas

    def update_rect(self):
        self.rect.center = (self.x, self.y) # actualizar rectangulo de coalision

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
        self.update_rect() # actualizar rectangulo de coalision
        
    def move_backwards(self):
        self.x += self.cos * 6
        self.y += self.sin * 6
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        self.update_rect() # actualizar rectangulo de coalision

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
    """
    Representa una bala disparada por el jugador.

    Atributos:
        img (pygame.Surface): Imagen de la bala.
        point (tuple): Coordenadas iniciales de la bala (posición del "cañón" del jugador).
        x (float): Coordenada x actual de la bala.
        y (float): Coordenada y actual de la bala.
        w (int): Ancho de la imagen de la bala.
        h (int): Alto de la imagen de la bala.
        cos (float): Valor del coseno de la dirección de disparo (basado en la orientación del jugador).
        sin (float): Valor del seno de la dirección de disparo (basado en la orientación del jugador).
        velx (float): Velocidad horizontal de la bala.
        vely (float): Velocidad vertical de la bala.
        rect (pygame.Rect): Rectángulo de colisión de la bala.
    """
    def __init__(self):
        """
        Inicializa una bala disparada desde la posición y orientación del jugador.
        """
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
        """
        Mueve la bala en la dirección calculada y actualiza su rectángulo de colisión.
        """
        self.x += self.velx
        self.y -= self.vely
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rect

    def draw(self, display):
        """
        Dibuja la bala en la ventana del juego.

        Args:
            display (pygame.Surface): Ventana del juego donde se dibuja la bala.
        """
        display.blit(self.img, (self.x, self.y))

class Asteroid():
    """
    Representa un asteroide en el juego.

    Atributos:
        rank (int): El tamaño del asteroide (1 = grande, 2 = mediano, 3 = pequeño).
        image (pygame.Surface): Imagen del asteroide según su tamaño.
        w (int): Ancho de la imagen del asteroide.
        h (int): Alto de la imagen del asteroide.
        ranPoint (tuple): Posición inicial aleatoria del asteroide fuera de la pantalla.
        x (int): Coordenada x actual del asteroide.
        y (int): Coordenada y actual del asteroide.
        rect (pygame.Rect): Rectángulo de colisión del asteroide.
        xdir (int): Dirección inicial del asteroide en el eje x (-1 o 1).
        ydir (int): Dirección inicial del asteroide en el eje y (-1 o 1).
        xv (int): Velocidad horizontal del asteroide.
        yv (int): Velocidad vertical del asteroide.
    """
    def __init__(self, rank):
        """
        Inicializa un asteroide con un tamaño y posición aleatorios.

        Args:
            rank (int): Tamaño del asteroide (1 = grande, 2 = mediano, 3 = pequeño).
        """
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid_s_big
        elif self.rank == 2:
            self.image = asteroid_m_big
        else:
            self.image = asteroid_l_big
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
        """
        Mueve el asteroide en la dirección y velocidad actuales,
        y actualiza su rectángulo de colisión.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rect

    def draw(self, win):
        """
        Dibuja el asteroide en la ventana del juego.

        Args:
            win (pygame.Surface): Ventana del juego donde se dibuja el asteroide.
        """
        win.blit(self.image, (self.x, self.y))

    
def redraw_game_window():
    display.blit(bg_big, (0, 0))
    font = pygame.font.SysFont('arial',30)
    lives_text = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    playAgainText = font.render('Press Space to Play Again', 1, (255,255,255))
    player.draw(display)
    for i in player_bullet:
        i.draw(display)
    for i in asteroids:
        i.draw(display)
    if gg:
        display.blit(playAgainText, (SX//2-playAgainText.get_width()//2, SY//2 - playAgainText.get_height()//2))
    display.blit(lives_text, (25, 25))
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
        
        for a in asteroids:
            a.move()

            # Colisión entre asteroide y jugador
            if player.rect.colliderect(a.rect):
                lives -= 1
                asteroids.pop(asteroids.index(a))
                break

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
        
        if lives <= 0:
            gg = True

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
                else:
                    gg = False
                    lives = 3
                    asteroids.clear()

    redraw_game_window()
pygame.quit()           
            
