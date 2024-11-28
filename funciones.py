import pygame
import random
import sys
from constantes import (
    ANCHO, 
    ALTO, 
    FPS,
    WHITE,
    BLACK,
    YELLOW
    
)
# Configuración del juego
puntos_iniciales = 0
fuente_intro = pygame.font.Font(None, 50)
fuente_menu = pygame.font.Font(None, 70)

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

# Fondo de estrellas para la intro
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
    scroll_velocidad = 10.4
    intro_running = True

    # Intentar cargar música de tensión
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
        for i, texto in enumerate(opciones):
            color = (255, 255, 0) if i == seleccion else (100, 100, 100)
            opcion_render = fuente.render(texto, True, color)
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

def cargar_imagen_jugador(jugador, ruta_imagen):
    try:
        # Cargar la imagen desde la ruta proporcionada
        imagen = pygame.image.load(ruta_imagen)
        # Redimensionar la imagen al tamaño del jugador (60x60 en este caso)
        imagen = pygame.transform.scale(imagen, (60, 60))
        jugador["surface"] = imagen  # Asignar la imagen al jugador
    except pygame.error as e:
        print(f"Error al cargar la imagen: {e}")

def cargar_imagen_soldado(soldado, ruta_imagen: str) -> None:
    try:
        # Cargar la imagen del soldado imperial desde la ruta proporcionada
        imagen = pygame.image.load(ruta_imagen)
        # Redimensionar la imagen al tamaño adecuado (30x30 en este caso)
        imagen = pygame.transform.scale(imagen, (45, 45))
        soldado["surface"] = imagen  # Asignar la imagen al soldado imperial
    except pygame.error as e:
        print(f"Error al cargar la imagen del soldado: {e}")
        soldado["surface"] = pygame.Surface((45, 45))  # Crear una superficie por defecto

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

def actualizar_soldado_imperial(soldado):
    if soldado["rectangulo"].x < soldado["objetivo_rectangulo"].x:
        soldado["rectangulo"].x += soldado["velocidad"]
    elif soldado["rectangulo"].x > soldado["objetivo_rectangulo"].x:
        soldado["rectangulo"].x -= soldado["velocidad"]
    if soldado["rectangulo"].y < soldado["objetivo_rectangulo"].y:
        soldado["rectangulo"].y += soldado["velocidad"]
    elif soldado["rectangulo"].y > soldado["objetivo_rectangulo"].y:
        soldado["rectangulo"].y -= soldado["velocidad"]

def actualizar_bala(bala):
    bala["rectangulo"].x += bala["dx"]
    bala["rectangulo"].y += bala["dy"]
    
    # Retorna True si la bala debe ser eliminada
    return (bala["rectangulo"].right < 0 or bala["rectangulo"].left > ANCHO or 
            bala["rectangulo"].bottom < 0 or bala["rectangulo"].top > ALTO)

def dibujar_stats(ventana, jugador, fuente):
    vida_text = fuente.render(f"Vida: {jugador['vida']}", True, WHITE)
    puntos_text = fuente.render(f"Puntos: {jugador['puntos']}", True, WHITE)
    enemigos_text = fuente.render(f"Eliminados: {jugador['enemigos_eliminados']}", True, WHITE)
    
    ventana.blit(vida_text, (10, 10))
    ventana.blit(puntos_text, (10, 50))
    ventana.blit(enemigos_text, (10, 90))
