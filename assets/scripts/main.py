import pygame
import sys
from juego import *
from spritevalues import *
from settings import *
from sfx import *
pygame.init()
pygame.mixer.init()

select_sfx = pygame.mixer.Sound("assets/sounds/select.wav")

ALTO, ANCHO = 720, 720 

ventana = pygame.display.set_mode((ALTO, ANCHO))
pygame.display.set_caption("Menu principal")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (100, 100, 100)

opciones_menu = ["Comenzar ", "Controles", "Créditos", "Salir del juego"]
opcion_elegida = 0

def menu_principal():
    global opcion_elegida

    bandera_menu = True
    while bandera_menu:
        ventana.fill(NEGRO)
        texto_titulo = fuente_titulo.render("ASTEROIDS", True, BLANCO)
        ventana.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))

        for i, option in enumerate(opciones_menu):
            color = BLANCO if i == opcion_elegida else GRIS
            text = fuente_menu.render(option, True, color)
            ventana.blit(text, (ANCHO // 2 - text.get_width() // 2, ALTO // 2 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opcion_elegida = (opcion_elegida - 1) % len(opciones_menu)
                    select_sfx.play()
                if event.key == pygame.K_DOWN:
                    opcion_elegida = (opcion_elegida + 1) % len(opciones_menu)
                    select_sfx.play()
                if event.key == pygame.K_RETURN:
                    select_sfx.play()
                    if opcion_elegida == 0:  # Comenzar juego
                        bandera_menu = False
                        comenzar_juego()
                        
                    elif opcion_elegida == 1:  # Controles
                        mostrar_controles()
                    elif opcion_elegida == 2:  # Créditos
                        mostrar_creditos()
                    elif opcion_elegida == 3:  # Salir del juego
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

def mostrar_controles():
    bandera_controles = True
    while bandera_controles:
        ventana.fill(NEGRO)

        texto_controles = [
            "Controles",
            "Movimiento: \u2191 \u2193 \u2190 \u2192",
            "Disparar: \u2423",
            "Rotar: A D",
            " ",
            "Presione ESC para volver"
        ]
        for i, line in enumerate(texto_controles):
            text = fuente_menu.render(line, True, BLANCO)
            ventana.blit(text, (ANCHO // 2 - text.get_width() // 2, ALTO // 3 + i * 60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bandera_controles = False

        pygame.display.update()
    menu_principal()

def mostrar_creditos():
    bandera_creditos = True
    while bandera_creditos:
        ventana.fill(NEGRO)
        ventana.blit(logo_grande, (190,-25))
        texto_creditos = [
            "Tobias Schmidt",
            "Franco Ferrandi",
            "Tomas Garabenta",
            " ",
            "Presione ESC para volver"
        ]
        for i, line in enumerate(texto_creditos):
            text = fuente_menu.render(line, True, BLANCO)
            ventana.blit(text, (ANCHO // 2 - text.get_width() // 2, ALTO // 2 + i * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bandera_creditos = False

        pygame.display.update()
    menu_principal()

menu_principal()
