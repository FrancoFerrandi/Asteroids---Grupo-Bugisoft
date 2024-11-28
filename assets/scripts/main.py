import pygame
import sys
from game import * 
from spritevalues import * 
from settings import *  
from sfx import * 

# Initialize Pygame and Pygame Mixer
pygame.init()
pygame.mixer.init()

# Load sound effects
select_sfx = pygame.mixer.Sound("assets/sounds/select.wav")


# Set window dimensions
HEIGHT, WIDTH = 720, 720

# Create the game window
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Main Menu")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Menu options and selected option index
menu_options = ["Start", "Controls", "Credits", "Exit Game"]
selected_option = 0

def main_menu():
    """
    Displays the main menu and handles user interaction for navigating through the options.
    """
    global selected_option

    menu_running = True
    while menu_running:
        # Fill the window with the background color
        window.fill(BLACK)

        # Render and display the title
        title_text = font_title.render("ASTEROIDS", True, WHITE)
        window.blit(
            title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4)
        )

        # Render and display each menu option
        for i, option in enumerate(menu_options):
            color = WHITE if i == selected_option else GRAY
            option_text = font_menu.render(option, True, color)
            window.blit(
                option_text,
                (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 + i * 60),
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

                    elif selected_option == 1:  # Show controls
                        show_controls()

                    elif selected_option == 2:  # Show credits
                        show_credits()

                    elif selected_option == 3:  # Exit the game
                        pygame.quit()
                        sys.exit()

        pygame.display.update()  # Update the display

def show_controls():
    """
    Displays the controls screen and handles user interaction to return to the main menu.
    """
    controls_running = True
    while controls_running:
        # Fill the window with the background color
        window.fill(BLACK)

        # Define the text for the controls screen
        controls_text = [
            "Controls",
            "Move: \u2191 \u2193 \u2190 \u2192",
            "Shoot: \u2423",
            "Rotate: A D",
            " ",
            "Press ESC to return",
        ]

        # Render and display each line of the controls text
        for i, line in enumerate(controls_text):
            text = font_menu.render(line, True, WHITE)
            window.blit(
                text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3 + i * 60)
            )

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()  # Play return sound
                    controls_running = False

        pygame.display.update()  # Update the display

    main_menu()  # Return to the main menu


def show_credits():
    """
    Displays the credits screen and handles user interaction to return to the main menu.
    """
    credits_running = True
    while credits_running:
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
            "Press ESC to return",
        ]

        # Render and display each line of the credits text
        for i, line in enumerate(credits_text):
            text = font_menu.render(line, True, WHITE)
            window.blit(
                text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + i * 50)
            )

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()  # Play return sound
                    credits_running = False

        pygame.display.update()  # Update the display

    main_menu()  # Return to the main menu


# Start the main menu
main_menu()
