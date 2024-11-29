import pygame
import sys
from constantes import (
    ANCHO, 
    ALTO, 
    FPS,
    BLACK,
    YELLOW,
    GRIS
)
from jugador import crear_resistencia

fuente_menu = pygame.font.Font(None, 70)

def mostrar_menu(ventana: pygame.Surface) -> str:
    """Muestra el menú principal."""
    fuente = pygame.font.Font(None, 50)
    menu_running = True  # Inicialización de la variable

    opciones = ["Jugar", "Salir"]
    seleccion = 0

    while menu_running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[seleccion] == "Jugar":
                        return "jugar"
                    elif opciones[seleccion] == "Salir":
                        return "salir"

        # Dibujar el menú
        ventana.fill((0, 0, 0))  # Fondo negro
        titulo_texto = fuente_menu.render("¡Bienvenidos!", True, YELLOW)
        titulo_rect = titulo_texto.get_rect(center=(ventana.get_width() // 2, 100))
        ventana.blit(titulo_texto, titulo_rect)
        for i, texto in enumerate(opciones):  # itera en las opciones "jugar" - "salir"
            if i == seleccion:
                color = YELLOW  
            else:
                color = GRIS 
            opcion_render = fuente.render(texto, True, color)
                # Aquí usarías opcion_render para dibujar el texto en la pantalla
            ventana.blit(opcion_render, 
                        (ventana.get_width() // 2 - opcion_render.get_width() // 2, 
                         ventana.get_height() // 2 + i * 60))
            ventana.blit(opcion_render, 
                        (ventana.get_width() // 2 - opcion_render.get_width() // 2, 
                         ventana.get_height() // 2 + i * 60))

        pygame.display.flip()

def pedir_datos(ventana: pygame.Surface) -> str:
    """Pide el nombre del jugador"""
    reloj = pygame.time.Clock()
    input_text = ""
    fuente_input = pygame.font.Font(None, 50)

    while True:
        ventana.fill(BLACK)

        prompt = fuente_input.render("Ingresa tu nombre:", True, YELLOW)
        prompt_rect = prompt.get_rect(center=(ANCHO // 2, ALTO // 4))
        ventana.blit(prompt, prompt_rect)

        input_surface = fuente_input.render(input_text, True, YELLOW)
        input_rect = input_surface.get_rect(center=(ANCHO // 2, ALTO // 2))
        ventana.blit(input_surface, input_rect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and input_text:
                    nombre = input_text
                    jugador = crear_resistencia(nombre)
                    return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += evento.unicode

        pygame.display.flip()
        reloj.tick(FPS)