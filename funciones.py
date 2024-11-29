import pygame
from constantes import (
    ANCHO, 
    ALTO, 
    WHITE,
)

def guardar_jugador(nombre: str, puntos: int, enemigos_eliminados: int) -> None:
    """Guarda los datos del jugador en un archivo."""
    with open("jugadores.txt", "a") as archivo:
        archivo.write(f"{nombre}, Puntos: {puntos}, Naves eliminadas: {enemigos_eliminados}\n")


# Cargar sonidos
def cargar_sonido_bala():
    try:
        sonido_bala = pygame.mixer.Sound('sonidos/sonido_bala.wav')  # Ruta al archivo de sonido
        return sonido_bala
    except pygame.error as e:
        print(f"Error al cargar el sonido de bala: {e}")
        return None



def cargar_fondo(ruta_fondo: str) -> pygame.Surface:
    try:
        # Cargar la imagen del fondo desde la ruta proporcionada
        fondo = pygame.image.load(ruta_fondo)
        # Redimensionar el fondo para que cubra toda la pantalla
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
        return fondo
    except pygame.error as e:
        print(f"Error al cargar el fondo: {e}")
        return pygame.Surface((ANCHO, ALTO))  # Fondo por defecto (negro)


def crear_bala(start_x: int, start_y: int, target_x: int, target_y: int):
    # Calcular dirección
    dx = target_x - start_x
    dy = target_y - start_y
    dist = (dx**2 + dy**2)**0.5
    velocidad = 10
    
    return {
        "surface": pygame.Surface((5, 5)),
        "rectangulo": pygame.Rect(start_x, start_y, 5, 5),
        "dx": dx/dist * velocidad if dist > 0 else 0,
        "dy": dy/dist * velocidad if dist > 0 else 0
    }


def actualizar_bala(bala):
    # Actualiza la posición de la bala en el eje X e Y usando su velocidad
    bala["rectangulo"].x += bala["dx"]
    bala["rectangulo"].y += bala["dy"]
#Verifica si la bala está fuera de los límites de la pantalla
    fuera_de_pantalla = (
        bala["rectangulo"].right < 0 or  # Fuera del lado izquierdo
        bala["rectangulo"].left > ANCHO or  # Fuera del lado derecho
        bala["rectangulo"].bottom < 0 or  # Fuera de la parte superior
        bala["rectangulo"].top > ALTO  # Fuera de la parte inferior
    )

    return fuera_de_pantalla  # Retorna True si la bala debe ser eliminada

def dibujar_stats(ventana, jugador, fuente):
    vida_text = fuente.render(f"Vida: {jugador['vida']}", True, WHITE)
    puntos_text = fuente.render(f"Puntos: {jugador['puntos']}", True, WHITE)
    enemigos_text = fuente.render(f"Eliminados: {jugador['enemigos_eliminados']}", True, WHITE)
    
    ventana.blit(vida_text, (10, 10))
    ventana.blit(puntos_text, (10, 50))
    ventana.blit(enemigos_text, (10, 90))
