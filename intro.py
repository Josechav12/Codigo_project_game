import pygame 
import sys
import random 
from constantes import (
    ANCHO, 
    ALTO, 
    FPS,
    BLACK,
    YELLOW
)
# Configuración del juego
pygame.init()
fuente_intro = pygame.font.Font(None, 50)

# Texto de la intro
intro_text = [
    "Hace mucho tiempo,",
    "en una galaxia muy, muy lejana...",
    "",
    "Star Wars",
    "La Resistencia",
    "",
    "El imperio oscuro ha tomado el control",
    "de la galaxia. Un grupo de valientes",
    "héroes se alzan para combatir la opresión.",
    "",
    "Tu misión: eliminar a los soldados imperiales",
    "y liberar la galaxia."
]

estrellas = [(pygame.Vector2(x, y), random.randint(1, 3)) for x, y in
        [(random.randint(0, ANCHO), random.randint(0, ALTO)) for _ in range(100)]]


def dibujar_estrellas(ventana, estrellas) -> None:
    """Dibuja un fondo de estrellas en movimiento."""
    for estrella, size in estrellas:
        pygame.draw.circle(ventana, YELLOW, estrella, size)
        estrella.y += size * 0.1
        if estrella.y > ALTO:
            estrella.y = 0

def mostrar_intro(ventana: pygame.Surface) -> None:
    """Muestra la intro animada antes de iniciar el juego."""
    reloj = pygame.time.Clock()
    text_y = ALTO  # Comienza fuera de la pantalla
    scroll_velocidad = 1.4
    intro_running = True

    # Intentar cargar música de intro 
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("sonidos/intromusic.mp3")  # Ruta al archivo de música
        pygame.mixer.music.play(-1)  # Reproducir en bucle
    except pygame.error as e:
        print(f"No se pudo cargar la música: {e}")

    while intro_running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ventana.fill(BLACK)
        dibujar_estrellas(ventana, estrellas)

        # Dibujar texto
        for i, linea in enumerate(intro_text):
            text_surface = fuente_intro.render(linea, True, YELLOW)
            text_rect = text_surface.get_rect(center=(ANCHO // 2, text_y + i * 50))
            text_rect.y -= i * 10  # Da perspectiva
            ventana.blit(text_surface, text_rect)

        # Desplazar texto hacia arriba
        text_y -= scroll_velocidad

        # Salir de la intro cuando el texto termina
        if text_y + len(intro_text) * 50 < 0:
            intro_running = False

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.mixer.music.stop()  # Detener música después de la intro
