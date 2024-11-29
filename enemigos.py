import pygame
import random
from constantes import (
    ANCHO, 
    ALTO, 
)

def cargar_imagen_soldado(soldado, ruta_imagen: str) -> None:
    try:
        # Cargar la imagen del soldado imperial desde la ruta proporcionada
        imagen = pygame.image.load(ruta_imagen)
        # Redimensionar la imagen al tamaño adecuado (30x30 en este caso)
        imagen = pygame.transform.scale(imagen, (45, 45))
        soldado["surface"] = imagen  # Asignar la imagen al soldado imperial
    except pygame.error as e:
        print(f"Error al cargar la imagen del soldado: {e}")
        soldado["surface"] = pygame.Surface((45, 45)) 

def crear_soldado_imperial(jugador_rect):
    # Elegir un lado aleatorio para el spawn
    side = random.choice(['arriba', 'derecha', 'abajo', 'izquierda'])
    if side == 'arriba':
        x = random.randint(0, ANCHO)
        y = -30
    elif side == 'derecha':
        x = ANCHO + 30
        y = random.randint(0, ALTO)
    elif side == 'abajo':
        x = random.randint(0, ANCHO)
        y = ALTO + 30
    else:  # izquierda
        x = -30
        y = random.randint(0, ALTO)
    
    soldado = {
        "surface": pygame.Surface((30, 30)),
        "rectangulo": pygame.Rect(x, y, 30, 30),
        "velocidad": 6,
        "health": 100,
        "objetivo_rectangulo": jugador_rect
    }
    
    # Cargar la imagen del soldado imperial
    cargar_imagen_soldado(soldado, 'imagenes/soldado_imperial.png')  # Asegúrate de tener la imagen en la carpeta correcta
    return soldado

def actualizar_soldado_imperial(soldado):
    if soldado["rectangulo"].x < soldado["objetivo_rectangulo"].x:
        soldado["rectangulo"].x += soldado["velocidad"]
    elif soldado["rectangulo"].x > soldado["objetivo_rectangulo"].x:
        soldado["rectangulo"].x -= soldado["velocidad"]
    if soldado["rectangulo"].y < soldado["objetivo_rectangulo"].y:
        soldado["rectangulo"].y += soldado["velocidad"]
    elif soldado["rectangulo"].y > soldado["objetivo_rectangulo"].y:
        soldado["rectangulo"].y -= soldado["velocidad"]