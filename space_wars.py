import pygame
from constantes import (
    ANCHO, 
    ALTO, 
    FPS, 
    RED,
    BLUE
)
from jugador import (
    cargar_imagen_jugador,
    crear_resistencia,
    actualizar_resistencia
)
from enemigos import (
    cargar_imagen_soldado,
    crear_soldado_imperial,
    actualizar_soldado_imperial
)
from intro import mostrar_intro
from menu import (
    mostrar_menu,
    pedir_datos
)

# Inicializar Pygame  
pygame.init()

from funciones import *

# Configuración inicial
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Star Wars: Resistencia vs Imperio")  # nombre del juego
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)

# Mostrar la introducción
mostrar_intro(ventana)

# Mostrar el menú
opcion_menu = mostrar_menu(ventana)

# Si el jugador elige jugar, pedimos nombre y dificultad
if opcion_menu == "jugar":
    nombre = pedir_datos(ventana)
    print(f"Jugador: {nombre}")  # Puedes usar esta información para ajustar el juego
else:
    pygame.quit()
    exit()  # Terminar el programa si elige salir

# Estado del juego
corriendo = True
juego_terminado = False
tiempo_aparicion = 0
aparicion_enemigo = 1500

# Cargar fondo
fondo = cargar_fondo('imagenes/fondo.png')

# Cargar sonido de bala
sonido_bala = cargar_sonido_bala()

# Crear jugador y listas de objetos
jugador = crear_resistencia(nombre)

# Cargar la imagen del jugador
cargar_imagen_jugador(jugador, 'imagenes/jugador.png')
soldados_imperiales = []
balas = []

while corriendo:
    reloj.tick(FPS)
    tiempo_actual = pygame.time.get_ticks()

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
            if evento.button == 1:  # Clic izquierdo
                mouse_x, mouse_y = pygame.mouse.get_pos()
                nueva_bala = crear_bala(jugador["rectangulo"].centerx, jugador["rectangulo"].centery, 
                                        mouse_x, mouse_y)
                nueva_bala["surface"].fill(BLUE)  # color de la bala
                balas.append(nueva_bala)
                if sonido_bala:
                    sonido_bala.play()  # sonido de la bala

    if not juego_terminado:
        # Spawn soldados imperiales
        if tiempo_actual - tiempo_aparicion > aparicion_enemigo:
            nuevo_soldado = crear_soldado_imperial(jugador["rectangulo"])
            soldados_imperiales.append(nuevo_soldado)
            tiempo_aparicion = tiempo_actual

        # Update jugador
        actualizar_resistencia(jugador)

        # Update soldados imperiales
        for soldado in soldados_imperiales:
            actualizar_soldado_imperial(soldado)

        # Update balas y eliminar las que salen de la pantalla
        balas = [bala for bala in balas if not actualizar_bala(bala)]

        # Colisiones bala-soldado imperial
        for bala in balas[:]:
            for soldado in soldados_imperiales[:]:
                if bala["rectangulo"].colliderect(soldado["rectangulo"]):
                    balas.remove(bala)
                    soldados_imperiales.remove(soldado)
                    jugador["enemigos_eliminados"] += 1
                    jugador["puntos"] += 10
                    break

        # Colisiones jugador-soldado imperial
        for soldado in soldados_imperiales:
            if jugador["rectangulo"].colliderect(soldado["rectangulo"]):
                jugador["vida"] -= 1
                if jugador["vida"] <= 0:
                    juego_terminado = True
                    guardar_jugador(nombre, jugador["puntos"], jugador["enemigos_eliminados"])
                    break

    # Dibujar fondo
    ventana.blit(fondo, (0, 0))

    # Dibujar jugador
    ventana.blit(jugador["surface"], jugador["rectangulo"])

    # Dibujar soldados imperiales
    for soldado in soldados_imperiales:
        ventana.blit(soldado["surface"], soldado["rectangulo"])

    # Dibujar balas
    for bala in balas:
        ventana.blit(bala["surface"], bala["rectangulo"])

    # Mostrar stats
    dibujar_stats(ventana, jugador, fuente)

    # Mostrar game over
    if juego_terminado:
        juego_terminado_text = fuente.render("GAME OVER", True, RED)
        ventana.blit(juego_terminado_text, 
                    (ANCHO//2 - juego_terminado_text.get_rect().width//2, 
                    ALTO//2))

    pygame.display.flip()

pygame.quit()

