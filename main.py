import pygame
import sys
from scripts.game import *
from scripts.sfx import *

# Load sound effects
select_sfx = pygame.mixer.Sound("assets/sounds/select.wav")

# Create the game window
window = pygame.display.set_mode((SX, SY))
pygame.display.set_caption("Asteroids by Bugisoft")


# Initialize Pygame and Pygame Mixer
pygame.init()
pygame.mixer.init()

def main_menu():
    """
    Displays the main menu and handles user interaction for navigating through the options.
    """
    global selected_option, window, SX, SY

    menu_running = True
    while menu_running:
        # Fill the window with the background color
        window.fill(BLACK)

        # Render and display the title
        title_text = font_title.render("ASTEROIDS", True, WHITE)
        window.blit(
            title_text, (SY // 2 - title_text.get_width() // 2, SX // 4)
        )

        # Render and display each menu option
        for i, option in enumerate(menu_options):
            color = WHITE if i == selected_option else GRAY
            option_text = font_menu.render(option, True, color)
            window.blit(
                option_text,
                (SY // 2 - option_text.get_width() // 2, SX // 2 + i * 60),
            )

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                    select_sfx.play()  # Play selection sound
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                    select_sfx.play()  # Play selection sound
                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()  # Play confirmation sound
                    if selected_option == 0:  # Start game
                        menu_running = False
                        start_game()
                    if selected_option == 1: # Show Settings
                        settings_menu()

                    elif selected_option == 2:  # Show controls
                        show_controls()

                    elif selected_option == 3:  # Show credits
                        show_credits()

                    elif selected_option == 4:  # Exit the game
                        pygame.quit()
                        sys.exit()

        pygame.display.update()  # Update the display

def show_controls():
    """
    Displays the controls screen and handles user interaction to return to the main menu.
    """
    bandera_controles = True
    while bandera_controles:
        # Fill the window with the background color
        window.fill(BLACK)

        # Define the text for the controls screen
        controls_text = [
            "Controles",
            "Movimiento: \u2191 \u2193 \u2190 \u2192",
            "Disparar: \u2423",
            " ",
            "Presiona ESC para volver",
        ]

        # Render and display each line of the controls text
        for i, line in enumerate(controls_text):
            text = font_menu.render(line, True, WHITE)
            window.blit(
                text, (SY // 2 - text.get_width() // 2, SX // 3 + i * 60)
            )

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()  # Play return sound
                    bandera_controles = False

        pygame.display.update()  # Update the display

    main_menu()  # Return to the main menu


def show_credits():
    """
    Displays the credits screen and handles user interaction to return to the main menu.
    """
    bandera_credits = True
    while bandera_credits:
        # Fill the window with the background color
        window.fill(BLACK)

        # Display a large logo (assumes the logo is loaded)
        window.blit(logo_large, (190, -25))

        # Define the text for the credits screen
        credits_text = [
            "Tobias Schmidt",
            "Franco Ferrandi",
            "Tomas Garabenta",
            " ",
            "Presiona ESC para volver",
        ]

        # Render and display each line of the credits text
        for i, line in enumerate(credits_text):
            text = font_menu.render(line, True, WHITE)
            window.blit(
                text, (SY // 2 - text.get_width() // 2, SX // 2 + i * 50)
            )

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()  # Play return sound
                    bandera_credits = False

        pygame.display.update()  # Update the display

    main_menu()  # Return to the main menu

def settings_menu():  
    settings_options = ["Tamaño de la ventana", "Opciones de volumen", "Presiona ESC para volver"]  
    selected_settings_option = 0  
    bandera_settings = True  
    
    while bandera_settings:  
        window.fill(BLACK)  

        for i, option in enumerate(settings_options):  
            color = WHITE if i == selected_settings_option else GRAY  
            option_text = font_menu.render(option, True, color)  
            window.blit(option_text, (SY // 2 - option_text.get_width() // 2, SX // 3 + i * 60))  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                sys.exit()  
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_UP:  
                    selected_settings_option = (selected_settings_option - 1) % len(settings_options)  
                    select_sfx.play()  
                if event.key == pygame.K_DOWN:  
                    selected_settings_option = (selected_settings_option + 1) % len(settings_options)  
                    select_sfx.play()  
                if event.key == pygame.K_RETURN:  
                    clickselect_sfx.play()  
                    if selected_settings_option == 0:  
                        screen_size_settings()  
                    elif selected_settings_option == 1:  
                        volume_settings()  
                    elif selected_settings_option == 2:  
                        returnselect_sfx.play()  
                        bandera_settings = False  
                if event.key == pygame.K_ESCAPE:  
                    returnselect_sfx.play()  
                    bandera_settings = False  

        pygame.display.update()  

def volume_settings():
    global SFX_VOLUME_LEVELS, MUSIC_VOLUME_LEVELS, select_sfx, clickselect_sfx, returnselect_sfx, soundtrack_sfx
    
    volume_options = [
        "Aumentar volumen de efectos",
        "Disminuir volumen de efectos",
        "Aumentar volumen de musica",
        "Disminuir volumen de musica",
        "Presiona ESC para volver"
    ]
    selected_volume_option = 0
    bandera_volumen = True

    while bandera_volumen:
        window.fill(BLACK)

        for i, option in enumerate(volume_options):
            color = WHITE if i == selected_volume_option else GRAY
            option_text = font_menu.render(option, True, color)
            window.blit(option_text, (SX // 2 - option_text.get_width() // 2, SY // 3 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_volume_option = (selected_volume_option - 1) % len(volume_options)
                    select_sfx.play()
                if event.key == pygame.K_DOWN:
                    selected_volume_option = (selected_volume_option + 1) % len(volume_options)
                    select_sfx.play()
                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()
                    if selected_volume_option == 0:  # Increase SFX Volume
                        SFX_VOLUME_LEVELS = min(10, SFX_VOLUME_LEVELS + 1)
                        update_sfx_volume()
                    elif selected_volume_option == 1:  # Decrease SFX Volume
                        SFX_VOLUME_LEVELS = max(0, SFX_VOLUME_LEVELS - 1)
                        update_sfx_volume()
                    elif selected_volume_option == 2:  # Increase Music Volume
                        MUSIC_VOLUME_LEVELS = min(10, MUSIC_VOLUME_LEVELS + 1)
                        update_music_volume()
                    elif selected_volume_option == 3:  # Decrease Music Volume
                        MUSIC_VOLUME_LEVELS = max(0, MUSIC_VOLUME_LEVELS - 1)
                        update_music_volume()
                    elif selected_volume_option == 4:  # Return to settings
                        returnselect_sfx.play()
                        bandera_volumen = False
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()
                    bandera_volumen = False

        pygame.display.update()

    settings_menu()  # Return to the settings menu

def update_sfx_volume():
    global SFX_VOLUME_LEVELS
    select_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    clickselect_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    returnselect_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    shoot_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    rapidshoot_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    asteroidL_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    asteroidM_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    asteroidS_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    hit_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    pickup_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    powerup_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    powerdown_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    dead_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)

def update_music_volume():
    global MUSIC_VOLUME_LEVELS
    soundtrack_sfx.set_volume(MUSIC_VOLUME_LEVELS * 0.1)

def screen_size_settings():
    global SX, SY, window

    screen_size_options = ["1. 720x720", "2. 900x900", "3. 1000x1000", "Presiona ESC para volver"]
    selected_screen_size_option = 0
    screen_size_running = True

    while screen_size_running:
        window.fill(BLACK)

        for i, option in enumerate(screen_size_options):
            color = WHITE if i == selected_screen_size_option else GRAY
            option_text = font_menu.render(option, True, color)
            window.blit(option_text, (SX // 2 - option_text.get_width() // 2, SY // 3 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_screen_size_option = (selected_screen_size_option - 1) % len(screen_size_options)
                    select_sfx.play()
                if event.key == pygame.K_DOWN:
                    selected_screen_size_option = (selected_screen_size_option + 1) % len(screen_size_options)
                    select_sfx.play()
                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()
                    if selected_screen_size_option == 0:
                        SX, SY = 720, 720
                    elif selected_screen_size_option == 1:
                        SX, SY = 900, 900
                    elif selected_screen_size_option == 2:
                        SX, SY = 1000, 1000
                    elif selected_screen_size_option == 3:
                        returnselect_sfx.play()
                        screen_size_running = False
                    window = pygame.display.set_mode((SX, SY))
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()
                    screen_size_running = False

        pygame.display.update()

    settings_menu()  # Return to the settings menu

     

main_menu()  

