# Star Wars: Resistencia vs Imperio

## Descripción

"Star Wars: Resistencia vs Imperio" es un juego de acción en 2D donde el jugador toma el control de un miembro de la Resistencia en una galaxia lejana, luchando contra las fuerzas del Imperio. El objetivo del juego es eliminar soldados imperiales mientras se evita el daño y se acumulan puntos.

## Características

- **Introducción**: Una historia envolvente inspirada en el universo de Star Wars, con texto desplazable y música de fondo.
- **Menú Principal**: El jugador puede elegir entre "Jugar" o "Salir". También se le pide que ingrese su nombre al comenzar.
- **Jugador Controlable**: El jugador controla un personaje de la Resistencia que puede moverse y disparar balas.
- **Enemigos**: Los soldados imperiales aparecen aleatoriamente en la pantalla y persiguen al jugador. El jugador puede dispararles para eliminarlos.
- **Puntos**: Cada enemigo eliminado otorga puntos, y se muestra un conteo de enemigos eliminados, vida restante y puntos en pantalla.
- **Game Over**: Si el jugador choca con un soldado imperial, pierde vida. El juego termina cuando la vida llega a 0.

## Requisitos

- Python 3.x
- Pygame (Instalar con `pip install pygame`)

## Instalación

1. Clona o descarga el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/Star-Wars-Resistencia-vs-Imperio.git
    ```
   
2. Instala las dependencias necesarias:
    ```bash
    pip install pygame
    ```

3. Coloca los archivos de imagen y sonido en las carpetas correspondientes:
    - **Imágenes**: `imagenes/jugador.png`, `imagenes/soldado_imperial.png`, `imagenes/fondo.png`.
    - **Sonidos**: `sonidos/intromusic.mp3`, `sonidos/sonido_bala.wav`.

4. Ejecuta el juego:
    ```bash
    python juego.py
    ```

## Controles

- **Movimiento del jugador**:  
  Usa las teclas **W**, **A**, **S**, **D** para mover al jugador en la pantalla.
- **Disparar**:  
  Haz clic con el botón izquierdo del ratón para disparar balas hacia el cursor del ratón.

## Notas

- El juego guarda el puntaje y el número de enemigos eliminados en un archivo de texto (`jugadores.txt`) al final de cada partida.
- Asegúrate de tener todos los archivos de recursos (imágenes y sonidos) en las carpetas correctas.

## Licencia

Este proyecto es de código abierto y se puede usar y modificar libremente bajo la licencia MIT.

## Autor

Desarrollado por [Tu Nombre] - [Tu perfil o enlace a tu repositorio]
