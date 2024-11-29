import pygame

from constantes import (
    ANCHO, 
    ALTO, 
)
puntos_iniciales = 0

def cargar_imagen_jugador(jugador, ruta_imagen):
    try:
        # Cargar la imagen desde la ruta proporcionada
        imagen = pygame.image.load(ruta_imagen)
        # Redimensionar la imagen al tamaño del jugador (60x60 en este caso)
        imagen = pygame.transform.scale(imagen, (60, 60))
        jugador["surface"] = imagen  # Asignar la imagen al jugador
    except pygame.error as e:
        print(f"Error al cargar la imagen: {e}")

def crear_resistencia(nombre):
    return {
        "surface": pygame.Surface((40, 40)),
        "rectangulo": pygame.Rect(ANCHO // 4, ALTO // 2, 40, 40),
        "velocidad": 5,
        "nombre": "Resistente",
        "vida": 120,
        "puntos": puntos_iniciales,
        "enemigos_eliminados": 0
    }

def actualizar_resistencia(jugador):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and jugador["rectangulo"].left > 0:
        jugador["rectangulo"].x -= jugador["velocidad"]
    if keys[pygame.K_d] and jugador["rectangulo"].right < ANCHO:
        jugador["rectangulo"].x += jugador["velocidad"]
    if keys[pygame.K_w] and jugador["rectangulo"].top > 0:
        jugador["rectangulo"].y -= jugador["velocidad"]
    if keys[pygame.K_s] and jugador["rectangulo"].bottom < ALTO:
        jugador["rectangulo"].y += jugador["velocidad"]
