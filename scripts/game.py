import pygame
import math
import random
from .spritevalues import *
from .sfx import *


pygame.init() # inicializa todos los módulos de Pygame que sean necesarios para ejecutar un juego o aplicación (display, font, event)
pygame.mixer.init()
pygame.display.set_caption("Asteroids")


class Player():
    """
    Represents the player in the game.

    Attributes:
        img (pygame.Surface): Image of the player sprite.
        w (int): Width of the player sprite.
        h (int): Height of the player sprite.
        x (int): Current x-coordinate of the player (centered horizontally).
        y (int): Current y-coordinate of the player (centered vertically).
        angle (float): Current angle of rotation of the player in degrees.
        rotateSprite (pygame.Surface): Rotated image of the player based on the current angle.
        rotateRect (pygame.Rect): Collision rectangle of the rotated player sprite.
        cos (float): Cosine of the player's angle (used for movement and rotation calculations).
        sin (float): Sine of the player's angle (used for movement and rotation calculations).
        head (tuple): Coordinates of the player's "head" (used for bullet origin).
        rect (pygame.Rect): Collision rectangle used for detecting collisions with asteroids and bullets.
    """

    def __init__(self):
        """
        Initializes the player with default position, orientation, and sprite image.
        """
        self.img = player_sprite
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = SX // 2  # Center the player horizontally on the screen
        self.y = SY // 2  # Center the player vertically on the screen
        
        self.angle = 0  # Initial rotation angle
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)

        # Calculate initial cosine and sine for movement
        self.cos = math.cos(math.radians(self.angle + 90)) 
        self.sin = math.sin(math.radians(self.angle + 90))
        
        # Determine the position of the player's "head" (used for bullet firing)
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2)
        self.rect = pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)  # Collision rectangle #default: - - | current: + +

    def update_rect(self):
        """
        Updates the collision rectangle's position to match the player's current position.
        """
        self.rect.center = (self.x, self.y)

    def draw(self, display):
        """
        Draws the rotated player sprite on the game window.

        Args:
            display (pygame.Surface): The game surface where the player is drawn.
        """
        display.blit(self.rotateSprite, self.rotateRect)

    def rotate_left(self):
        """
        Rotates the player to the left by a fixed rotation velocity.
        Updates the sprite image, rectangle, and movement direction.
        """
        self.angle += PLAYER_ROTATION_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2) #default: + | current: -

    def rotate_right(self):
        """
        Rotates the player to the right by a fixed rotation velocity.
        Updates the sprite image, rectangle, and movement direction.
        """
        self.angle -= PLAYER_ROTATION_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2) #default: + | current: -

    def move_forward(self):
        """
        Moves the player forward in the direction it is facing.
        Updates the sprite image, rectangle, and collision rectangle.
        """
        self.x += self.cos * PLAYER_VEL
        self.y -= self.sin * PLAYER_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2)
        self.update_rect()  # Update collision rectangle

    def move_backwards(self):
        """
        Moves the player backward in the direction it is facing.
        Updates the sprite image, rectangle, and collision rectangle.
        """
        self.x += self.cos * PLAYER_VEL
        self.y += self.sin * PLAYER_VEL
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2)
        self.update_rect()  # Update collision rectangle

class Bullet():
    """
    Represents a bullet fired by the player.

    Attributes:
        img (pygame.Surface): Image of the bullet.
        point (tuple): Initial coordinates of the bullet (player's "cannon" position).
        x (float): Current x-coordinate of the bullet.
        y (float): Current y-coordinate of the bullet.
        w (int): Width of the bullet image.
        h (int): Height of the bullet image.
        cos (float): Cosine value of the shooting direction (based on player's orientation).
        sin (float): Sine value of the shooting direction (based on player's orientation).
        velx (float): Horizontal velocity of the bullet.
        vely (float): Vertical velocity of the bullet.
        rect (pygame.Rect): Collision rectangle of the bullet.
    """
    def __init__(self):
        """
        Initializes a bullet fired from the player's position and orientation.
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
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Collision rectangle

    def move(self):
        """
        Moves the bullet in the calculated direction and updates its collision rectangle.
        """
        self.x += self.velx
        self.y -= self.vely
        self.rect.topleft = (self.x, self.y)  # Update the position of the rectangle

    def draw(self, display):
        """
        Draws the bullet on the game window.

        Args:
            display (pygame.Surface): The game window where the bullet is drawn.
        """
        display.blit(self.img, (self.x, self.y))

class Asteroid():
    """
    Represents an asteroid in the game.

    Attributes:
        rank (int): The size of the asteroid (3 = large, 2 = medium, 1 = small).
        image (pygame.Surface): The asteroid image according to its size.
        w (int): The width of the asteroid image.
        h (int): The height of the asteroid image.
        ran_point (tuple): The initial random position of the asteroid outside the screen.
        x (int): The current x-coordinate of the asteroid.
        y (int): The current y-coordinate of the asteroid.
        rect (pygame.Rect): The collision rectangle of the asteroid.
        xdir (int): The initial direction of the asteroid on the x-axis (-1 or 1).
        ydir (int): The initial direction of the asteroid on the y-axis (-1 or 1).
        xv (int): The horizontal velocity of the asteroid.
        yv (int): The vertical velocity of the asteroid.
    """
    def __init__(self, rank):
        """
        Initializes an asteroid with a random size and position.

        Args:
            rank (int): The size of the asteroid (3 = large, 2 = medium, 1 = small).
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
        self.ran_point = random.choice([
            (random.randrange(0, SX - self.w), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, SY - self.h))
        ])
        self.x, self.y = self.ran_point
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Collision rectangle
        if self.x < SX // 2:
            self.xdir = ASTEROID_VEL
        else:
            self.xdir = -ASTEROID_VEL
        if self.y < SY // 2:
            self.ydir = ASTEROID_VEL
        else:
            self.ydir = -ASTEROID_VEL
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def move(self):
        """
        Moves the asteroid in the current direction and velocity,
        and updates its collision rectangle.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Update the position of the rectangle

    def draw(self, display):
        """
        Draws the asteroid on the game window.

        Args:
            display (pygame.Surface): The game window where the asteroid is drawn.
        """
        display.blit(self.image, (self.x, self.y))

class Star():
    """
    Represents a star that can appear in the game and has two possible effects:
    - Increases the player's shooting ability.
    - Reduces the player's lives.

    Attributes:
        img (pygame.Surface): Image of the star.
        w (int): Width of the star image.
        h (int): Height of the star image.
        ran_point (tuple): Initial random position of the star outside the screen.
        x (int): Current x-coordinate of the star.
        y (int): Current y-coordinate of the star.
        xdir (int): Initial direction on the x-axis (1 or -1).
        ydir (int): Initial direction on the y-axis (1 or -1).
        xv (int): Velocity on the x-axis.
        yv (int): Velocity on the y-axis.
        rect (pygame.Rect): Collision rectangle of the star.
        effect (str): Type of effect of the star ('boost' for firepower, 'lesslife' to decrease life).
    """
    def __init__(self):
        """
        Initializes a star with a random position outside the screen and a random effect.
        """
        self.img = fakeheal_big
        self.w = self.img.get_width()
        self.h = self.img.get_height()

        # Generate initial coordinates
        self.ran_point = random.choice([
            (random.randrange(0, max(1, SX - self.w)), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, max(1, SY - self.h)))
        ])

        self.x, self.y = self.ran_point

        # Determine direction
        self.xdir = 1 if self.x < SX // 2 else -1
        self.ydir = 1 if self.y < SY // 2 else -1

        # Velocity
        self.xv = self.xdir * FAKEHEAL_VEL
        self.yv = self.ydir * FAKEHEAL_VEL

        # Collision rectangle
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # Randomly determine if the star will give a firepower boost or reduce a life
        self.effect = random.choice(['boost', 'lesslife'])

    def move(self):
        """
        Updates the position of the star and its collision rectangle.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Update collision rectangle

    def draw(self, display):
        """
        Draws the star on the game window.

        Args:
            display (pygame.Surface): The game surface where the star is drawn.
        """
        display.blit(self.img, (self.x, self.y))

class LifeStar():
    """
    Represents a star that restores 1 life to the player upon collision.

    Attributes:
        img (pygame.Surface): Image of the star.
        w (int): Width of the star image.
        h (int): Height of the star image.
        ran_point (tuple): Initial random position of the star outside the screen.
        x (int): Current x-coordinate of the star.
        y (int): Current y-coordinate of the star.
        xdir (int): Initial direction on the x-axis (1 or -1).
        ydir (int): Initial direction on the y-axis (1 or -1).
        xv (int): Velocity on the x-axis.
        yv (int): Velocity on the y-axis.
        rect (pygame.Rect): Collision rectangle of the star.
        effect (str): Type of effect of the star ('morelife' to restore life).
    """
    def __init__(self):
        """
        Initializes a star with a random position outside the screen and the 'morelife' effect.
        """
        self.img = heal_big  # You can use the same image or a different one if preferred.
        self.w = self.img.get_width()
        self.h = self.img.get_height()

        # Generate initial coordinates
        self.ran_point = random.choice([  # Star appearing at the edge of the screen.
            (random.randrange(0, max(1, SX - self.w)), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, max(1, SY - self.h)))
        ])

        self.x, self.y = self.ran_point

        # Determine the direction of the star
        self.xdir = 1 if self.x < SX // 2 else -1
        self.ydir = 1 if self.y < SY // 2 else -1

        # Velocity
        self.xv = self.xdir * HEAL_VEL
        self.yv = self.ydir * HEAL_VEL

        # Collision rectangle
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # Effect of the star (restore life)
        self.effect = 'morelife'

    def move(self):
        """
        Updates the position of the star and its collision rectangle.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Update collision rectangle

    def draw(self, display):
        """
        Draws the star on the game window.

        Args:
            display (pygame.Surface): The game surface where the star is drawn.
        """
        display.blit(self.img, (self.x, self.y))

def redraw_game_window():
    """
    Redraws all game elements on the game window.

    This function updates the game display by drawing the background, player, bullets,
    asteroids, stars, and UI elements such as lives and score. It also handles the 
    display of power-up indicators and the "Game Over" message when applicable.
    """

    display.blit(bg_big, (0, 0))
    lives_text = font_ingame.render('Vidas: ' + str(lives), 1, (255, 255, 255))
    play_again_text = font_ingame.render('Apreta \u2423 para volver a jugar', 1, (255,255,255))
    score_text = font_ingame.render('Score: ' + str(score), 1, (255,255,255))
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
        display.blit(play_again_text, (SX // 2 - play_again_text.get_width() // 2, SY // 2 - play_again_text.get_height() // 2))
    display.blit(lives_text, (25, 25))
    display.blit(score_text, (SX - score_text.get_width() - 10, 25))  
    pygame.display.update()



def save_score(name, score):
    """
    Appends the player's name and score to a text file named 'puntuaciones.txt'.
    
    Args:
        name (str): The player's name.
        score (int): The player's score.
    """
    with open("puntuaciones.txt", "a") as file:
        file.write(f"{name}: {score}\n")


def read_scores():
    """
    Reads the scores from the 'puntuaciones.txt' file and returns them as a list of tuples.
    
    Returns:
        list: A list of tuples containing player names and their scores, or an empty list if the file is not found.
    """
    try:
        with open("puntuaciones.txt", "r") as file:
            scores = []
            for line in file:
                name, score = line.strip().split(": ")
                scores.append((name, int(score)))
            return scores
    except FileNotFoundError:
        return []

player = Player()

def show_game_over_screen():
    """
    Displays the 'Game Over' screen where the player can enter their name 
    and save their score. It also resets the game when the player presses 'Enter'.
    """
    global run, gg
    input_active = True
    name = ""

    while input_active:
        display.fill((0, 0, 0))  # Black screen
        game_over_text = font_menu.render("GAME OVER", True, (255, 255, 255))
        enter_name_text = font_menu.render("Ingresa tu nombre:", True, (255, 255, 255))
        name_text = font_menu.render(name, True, (255, 255, 255))

        display.blit(game_over_text, (SX // 2 - game_over_text.get_width() // 2, 100))
        display.blit(enter_name_text, (SX // 2 - enter_name_text.get_width() // 2, 200))
        display.blit(name_text, (SX // 2 - name_text.get_width() // 2, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                input_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name != "":
                    save_score(name, score)
                    gg = False  # Restart the game
                    input_active = False
                    show_top_5()
                    reset_game()  # Reset game variables
                    startengine_sfx.play()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10:
                        name += event.unicode


def bubble_sort_scores(scores: list[tuple[str, int]]) -> None: #Usamos bubble sort como algoritmo de ordenamiento para ubicar los scores mayor a menor
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j][1] < scores[j+1][1]:  # Usando < (menor que) para que sea descendiente
                scores[j], scores[j+1] = scores[j+1], scores[j]


def show_top_5() -> None:
    """
    Displays the Top 5 players with the highest scores on the screen.
    The player can press 'Enter' to return to the game.
    """
    scores = read_scores()
    bubble_sort_scores(scores)  # Aplicacion de Bubble sort
    top_5 = scores[:5]  # Top 5 scores mas altos

    showing_top_5 = True
    while showing_top_5:
        display.fill((BLACK))  
        title = font_menu.render("TOP 5 JUGADORES", True, (WHITE))
        display.blit(title, (SX // 2 - title.get_width() // 2, 50))

        for i, (name, score) in enumerate(top_5):
            score_text = font_menu.render(f"{i + 1}. {name}: {score}", True, (WHITE))
            display.blit(score_text, (SX // 2 - score_text.get_width() // 2, 150 + i * 50))

        exit_text = font_menu.render("Oprime ENTER para volver a jugar", True, (WHITE))
        display.blit(exit_text, (SX // 2 - exit_text.get_width() // 2, SY - 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showing_top_5 = False
                global run
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    showing_top_5 = False

def reset_game():
    """
    Resets the game's variables to their initial state.
    """
    global lives, score, asteroids, player_bullet, stars
    lives = 3
    score = 0
    asteroids.clear()
    player_bullet.clear()
    stars.clear()

def start_game():
    """
    Main game loop that handles all gameplay logic.
    The game runs until the player loses all lives, at which point the game over screen is displayed.

    The function also checks for events such as key presses and window closure.

    Controls:
        - 'A': Rotate the player to the left.
        - 'D': Rotate the player to the right.
        - 'W': Move the player forward.
        - 'S': Move the player backwards.
        - 'SPACE': Fire a bullet or shoot with the fire boost if active.
        - 'M': Toggle sound on/off.
    """
    global run, count, player_bullet, asteroids, lives, gg, score, stars, fire_boost, f_boost
    soundtrack_sfx.play(loops=-1)  # Loop the background music
    startengine_sfx.play()  # Play the start engine sound effect

    while run:
        clock.tick(60)  # Limit the frame rate to 60 FPS
        count += 1  # Increment the game counter

        if not gg:  # Game is running
            if count % ASTEROID_CHANCE == 0:  # Every 50 frames
                ran = random.choice([1, 1, 1, 2, 2, 3])  # Random asteroid rank
                asteroids.append(Asteroid(ran))  # Add a new asteroid

            if count % STAR_CHANCE == 0:  # Every 1000 frames
                stars.append(Star())  # Add a new star

            if count % LIFESTAR_CHANCE == 0:  # Every 2500 frames
                stars.append(LifeStar())  # Add a life star

            for i in player_bullet:  # Move the bullets
                i.move()

            for a in asteroids:  # Move asteroids
                a.move()

                # Collision between player and asteroid
                if player.rect.colliderect(a.rect):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    hit_sfx.play()  # Play hit sound
                    break

                # Collision between bullet and asteroid
                for b in player_bullet:
                    if b.rect.colliderect(a.rect):
                        if a.rank == 3:  # Large asteroid
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x, na1.y = a.x, a.y
                            na2.x, na2.y = a.x, a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                            asteroidL_sfx.play()  # Large asteroid destroyed sound
                        elif a.rank == 2:  # Medium asteroid
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x, na1.y = a.x, a.y
                            na2.x, na2.y = a.x, a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                            asteroidM_sfx.play()  # Medium asteroid destroyed sound
                        else:  # Small asteroid
                            score += 50
                        asteroids.pop(asteroids.index(a))
                        player_bullet.pop(player_bullet.index(b))
                        asteroidS_sfx.play()  # Small asteroid destroyed sound
                        break

            for s in stars[:]:  # Iterate over a copy of the list to avoid modification issues (shallow copy) 
                s.move()

                # Remove stars outside the visible area
                if s.x < -100 - s.w or s.x > SX + 100 or s.y > SY + 100 or s.y < -100 - s.h:
                    stars.remove(s)
                    continue

                # Collision between stars and bullets
                for b in player_bullet[:]:
                    if s.rect.colliderect(b.rect):
                        if s.effect == 'boost':
                            fire_boost = True
                            f_boost = count
                            pickup_sfx.play()  # Pickup sound effect
                        elif s.effect == 'lesslife':
                            lives -= 1
                            hit_sfx.play()  # Hit sound effect
                        elif s.effect == 'morelife':
                            lives += 1
                            powerup_sfx.play()  # Power-up sound effect

                        stars.remove(s)
                        player_bullet.remove(b)
                        break

                # Collision between the star and the player
                if player.rect.colliderect(s.rect):
                    if s.effect == 'boost':
                        fire_boost = True
                        f_boost = count
                        pickup_sfx.play()  # Pickup sound effect
                    elif s.effect == 'lesslife':
                        lives -= 1
                        hit_sfx.play()  # Hit sound effect
                    elif s.effect == 'morelife':
                        lives += 1
                        powerup_sfx.play()  # Power-up sound effect

                    stars.remove(s)  # Remove the star after it is collected

            # Check if the player has lost all lives
            if lives <= 0:
                dead_sfx.play()  # Play dead sound
                gg = True  # Game over

            # Handle fire boost expiration
            if f_boost != -1:
                if count - f_boost > 500:
                    powerdown_sfx.play()  # Power-down sound effect
                    fire_boost = False
                    f_boost = -1

            # Player movement and shooting
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.rotate_left()
            if keys[pygame.K_RIGHT]:
                player.rotate_right()
            if keys[pygame.K_UP]:
                player.move_forward()
            if keys[pygame.K_DOWN]:
                player.move_backwards()
            if keys[pygame.K_SPACE]:
                if fire_boost:
                    player_bullet.append(Bullet())  # Fire with boost
                    rapidshoot_sfx.play()  # Rapid shoot sound


        else:  # If game over
            show_game_over_screen()

        # Handle events (e.g., key presses, window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gg:  # If not game over
                        if not fire_boost:
                            player_bullet.append(Bullet())  # Fire bullet
                            shoot_sfx.play()  # Shoot sound effect
                    else:
                        gg = False  # Restart game
                        reset_game()  # Reset game state
                if event.key == pygame.K_m:
                    isSoundOn = not isSoundOn  # Toggle sound on/off

        redraw_game_window()  # Redraw the game window

    pygame.quit()  # Quit pygame when the loop ends


