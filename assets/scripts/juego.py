import pygame
import math
from settings import *
from spritevalues import *
import random
from sfx import *





pygame.init() # inicializa todos los módulos de Pygame que sean necesarios para ejecutar un juego o aplicación (display, font, event)
pygame.mixer.init()
pygame.display.set_caption("Asteroids")



#Sonidos que hay que modulizar en el archivo sfx.py(no puedo modulizar que la chupe este codigo)
soundtrack_sfx = pygame.mixer.Sound("assets/sounds/game_soundtrack.mp3")
soundtrack_sfx.set_volume(GAMEOST_VOLUME)

shoot_sfx = pygame.mixer.Sound("assets/sounds/laserShoot.wav")
rapidshoot_sfx = pygame.mixer.Sound("assets/sounds/rapidshoot.wav")

shoot_sfx.set_volume(SHOOT_VOLUME)

asteroidL_sfx = pygame.mixer.Sound("assets/sounds/explosion.wav")
asteroidM_sfx = pygame.mixer.Sound("assets/sounds/explosion_m.wav")
asteroidS_sfx = pygame.mixer.Sound("assets/sounds/explosion_s.wav")

hit_sfx = pygame.mixer.Sound("assets/sounds/hit.wav")

pickup_sfx = pygame.mixer.Sound("assets/sounds/pickup.wav")


powerup_sfx = pygame.mixer.Sound("assets/sounds/powerup.wav")
powerdown_sfx = pygame.mixer.Sound("assets/sounds/powerdown.wav")

select_sfx = pygame.mixer.Sound("assets/sounds/select.wav")

clickselect_sfx = pygame.mixer.Sound("assets/sounds/blipSelect.wav")

returnselect_sfx = pygame.mixer.Sound("assets/sounds/backSelect.wav")


dead_sfx = pygame.mixer.Sound("assets/sounds/dead.wav")
startengine_sfx = pygame.mixer.Sound("assets/sounds/startengine.wav")

clock = pygame.time.Clock() 
display = pygame.display.set_mode((SX, SY))
gg = False
lives = 3
score = 0
fire_boost = False
f_boost = -1
isSoundOn = True


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
        self.angle += PLAYER_ROTATION_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        
    def rotate_right(self):
        self.angle -= PLAYER_ROTATION_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        
    def move_forward(self):
        self.x += self.cos * PLAYER_VEL
        self.y -= self.sin * PLAYER_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w//2, self.y + self.sin * self.h//2)
        self.update_rect() # actualizar rectangulo de coalision
        
    def move_backwards(self):
        self.x += self.cos * PLAYER_VEL
        self.y += self.sin * PLAYER_VEL
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
        self.velx = self.cos * BULLET_VEL
        self.vely = self.sin * BULLET_VEL
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
        self.ran_point = random.choice([(random.randrange(0, SX-self.w), random.choice([-1*self.h - 5, SY + 5])), (random.choice([-1*self.w - 5, SX + 5]), random.randrange(0, SY - self.h))])
        self.x, self.y = self.ran_point
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Rectángulo de colisión
        if self.x < SX//2:
            self.xdir = ASTEROID_VEL
        else:
            self.xdir = -ASTEROID_VEL
        if self.y < SY//2:
            self.ydir = ASTEROID_VEL
        else:
            self.ydir = -ASTEROID_VEL
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

class Star():
    """
    Representa una estrella que puede aparecer en el juego y puede tener dos efectos:
    - Aumentar la habilidad de disparo del jugador.
    - Reducir el número de vidas del jugador.

    Atributos:
        img (pygame.Surface): Imagen de la estrella.
        w (int): Ancho de la imagen de la estrella.
        h (int): Alto de la imagen de la estrella.
        ran_point (tuple): Posición aleatoria inicial de la estrella fuera de la pantalla.
        x (int): Coordenada x actual de la estrella.
        y (int): Coordenada y actual de la estrella.
        xdir (int): Dirección inicial en el eje x (1 o -1).
        ydir (int): Dirección inicial en el eje y (1 o -1).
        xv (int): Velocidad en el eje x.
        yv (int): Velocidad en el eje y.
        rect (pygame.Rect): Rectángulo de colisión de la estrella.
        effect (str): Tipo de efecto de la estrella ('boost' para potencia de fuego, 'lesslife' para restar vida).
    """
    def __init__(self):
        """
        Inicializa una estrella con una posición aleatoria fuera de la pantalla y un efecto aleatorio.
        """
        self.img = fakeheal_big
        self.w = self.img.get_width()
        self.h = self.img.get_height()

        # Generar coordenadas iniciales
        self.ran_point = random.choice([
            (random.randrange(0, max(1, SX - self.w)), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, max(1, SY - self.h)))
        ])

        self.x, self.y = self.ran_point

        # Determinar dirección
        self.xdir = 1 if self.x < SX // 2 else -1
        self.ydir = 1 if self.y < SY // 2 else -1

        # Velocidad
        self.xv = self.xdir * FAKEHEAL_VEL
        self.yv = self.ydir * FAKEHEAL_VEL

        # Rectángulo de colisión
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # Determinar aleatoriamente si la estrella dará un boost de fuego o quitará una vida
        self.effect = random.choice(['boost', 'lesslife'])

    def move(self):
        """
        Actualiza la posición de la estrella y su rectángulo de colisión.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Actualizar rectángulo de colisión

    def draw(self, display):
        """
        Dibuja la estrella en la ventana del juego.

        Args:
            display (pygame.Surface): La superficie del juego donde se dibuja la estrella.
        """
        display.blit(self.img, (self.x, self.y))

class LifeStar():
    """
    Representa una estrella que regenera 1 vida al jugador cuando colisiona con ella.

    Atributos:
        img (pygame.Surface): Imagen de la estrella.
        w (int): Ancho de la imagen de la estrella.
        h (int): Alto de la imagen de la estrella.
        ran_point (tuple): Posición aleatoria inicial de la estrella fuera de la pantalla.
        x (int): Coordenada x actual de la estrella.
        y (int): Coordenada y actual de la estrella.
        xdir (int): Dirección inicial en el eje x (1 o -1).
        ydir (int): Dirección inicial en el eje y (1 o -1).
        xv (int): Velocidad en el eje x.
        yv (int): Velocidad en el eje y.
        rect (pygame.Rect): Rectángulo de colisión de la estrella.
        effect (str): Tipo de efecto de la estrella ('life' para regenerar vida).
    """
    def __init__(self):
        """
        Inicializa una estrella con una posición aleatoria fuera de la pantalla y el efecto 'morelife'.
        """
        self.img = heal_big  # Puedes usar la misma imagen o una diferente si prefieres.
        self.w = self.img.get_width()
        self.h = self.img.get_height()

        # Generar coordenadas iniciales
        self.ran_point = random.choice([  # Estrella apareciendo en el borde de la pantalla.
            (random.randrange(0, max(1, SX - self.w)), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, max(1, SY - self.h)))
        ])

        self.x, self.y = self.ran_point

        # Determinar dirección de la estrella
        self.xdir = 1 if self.x < SX // 2 else -1
        self.ydir = 1 if self.y < SY // 2 else -1

        # Velocidad
        self.xv = self.xdir * HEAL_VEL
        self.yv = self.ydir * HEAL_VEL

        # Rectángulo de colisión
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # Efecto de la estrella (regenerar vida)
        self.effect = 'morelife'

    def move(self):
        """
        Actualiza la posición de la estrella y su rectángulo de colisión.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Actualizar rectángulo de colisión

    def draw(self, display):
        """
        Dibuja la estrella en la ventana del juego.

        Args:
            display (pygame.Surface): La superficie del juego donde se dibuja la estrella.
        """
        display.blit(self.img, (self.x, self.y))

def redraw_game_window():
    display.blit(bg_big, (0, 0))
    font = pygame.font.SysFont('arial',30)
    lives_text = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    play_again_text = font.render('Press Space to Play Again', 1, (255,255,255))
    score_text = font.render('Score: ' + str(score), 1, (255,255,255))
    player.draw(display)
    for pb in player_bullet:
        pb.draw(display)
    for a in asteroids:
        a.draw(display)
    for s in stars:
        s.draw(display)
    
    if fire_boost:
        pygame.draw.rect(display, (0, 0, 0), [SX//2 - 51, 19, 102, 22])
        pygame.draw.rect(display, (255, 255, 255), [SX//2 - 50, 20, 100 - 100*(count - f_boost)/500, 20])

    if gg:
        display.blit(play_again_text, (SX//2-play_again_text.get_width()//2, SY//2 - play_again_text.get_height()//2))
    display.blit(lives_text, (25, 25))
    display.blit(score_text, (SX- score_text.get_width() - 25, 25))
    pygame.display.update()

player = Player()
player_bullet = []
asteroids = []
stars = []
count = 0

run = True
#bandera para verificar si el juego esta siendo renderizado para saber si debe finalizar el codigo
def comenzar_juego():
    global run, count, player_bullet, asteroids, lives, gg, score, stars, fire_boost, f_boost
    soundtrack_sfx.play(loops=-1)
    startengine_sfx.play() 
    while run:
        clock.tick(60)
        count += 1
        if not gg:
            if count % 50 == 0:
                ran = random.choice([1,1,1,2,2,3])
                asteroids.append(Asteroid(ran))
            if count % 1000 == 0:
                stars.append(Star())
            if count % 2500 == 0: 
                stars.append(LifeStar())
            for i in player_bullet:
                i.move()
        
            for a in asteroids:
                a.move()

                # Colisión entre asteroide y jugador
                if player.rect.colliderect(a.rect):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    hit_sfx.play()
                    break

                # Colisión entre bala y asteroide
                for b in player_bullet:
                    if b.rect.colliderect(a.rect):
                        if a.rank == 3:
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x, na1.y = a.x, a.y
                            na2.x, na2.y = a.x, a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                            asteroidL_sfx.play()
                            
                        elif a.rank == 2:
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x, na1.y = a.x, a.y
                            na2.x, na2.y = a.x, a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                            asteroidM_sfx.play()
                            
                        else:    
                            score += 50
                        asteroids.pop(asteroids.index(a))
                        player_bullet.pop(player_bullet.index(b))
                        asteroidS_sfx.play()
                        
                        break

            for s in stars[:]:  # Iterar sobre una copia de la lista
                s.move()  # Usar el método move para actualizar posición

                # Eliminar estrellas fuera del área visible
                if s.x < -100 - s.w or s.x > SX + 100 or s.y > SY + 100 or s.y < -100 - s.h:
                    stars.remove(s)
                    continue
                
                # Colisión entre estrellas y balas
                for b in player_bullet[:]:
                    if s.rect.colliderect(b.rect):  # Usar los rectángulos de colisión
                        if s.effect == 'boost':
                            fire_boost = True
                            f_boost = count
                            pickup_sfx.play()
                        elif s.effect == 'lesslife':
                            lives -= 1
                            hit_sfx.play()
                        elif s.effect == 'morelife':
                            lives += 1 
                            powerup_sfx.play()

                        stars.remove(s)
                        player_bullet.remove(b)
                        break

                # Colisión entre la estrella y el jugador
                if player.rect.colliderect(s.rect):
                        if s.effect == 'boost':
                            fire_boost = True
                            f_boost = count
                            pickup_sfx.play()
                        elif s.effect == 'lesslife':
                            lives -= 1
                            hit_sfx.play()
                        elif s.effect == 'morelife':
                            lives += 1 
                            powerup_sfx.play()
                        stars.remove(s)  # Eliminar la estrella después de recogerla

            if lives <= 0:
                dead_sfx.play()
                gg = True

            if f_boost != -1:
                if count - f_boost > 500:
                    powerdown_sfx.play()
                    fire_boost = False
                    f_boost = -1
                    

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.rotate_left()
            if keys[pygame.K_d]:
                player.rotate_right()
            if keys[pygame.K_w]:
                player.move_forward()
            if keys[pygame.K_s]:
                player.move_backwards()
            if keys[pygame.K_SPACE]:
                if fire_boost:
                    player_bullet.append(Bullet())
                    rapidshoot_sfx.play()
                    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gg:
                        if not fire_boost:
                            player_bullet.append(Bullet())
                            shoot_sfx.play()
                    else:
                        gg = False
                        lives = 3
                        score = 0
                        asteroids.clear()
                        stars.clear()
                if event.key == pygame.K_m:
                    isSoundOn = not isSoundOn
        redraw_game_window()
    pygame.quit()           

            
