# Visualización del Recorrido del Caballo en Ajedrez

Este programa visualiza una solución para el problema del "Recorrido del Caballo" utilizando Python y Tkinter. El problema del Recorrido del Caballo es un desafío clásico de ajedrez donde el caballo debe visitar cada casilla del tablero exactamente una vez. Este programa muestra un tablero de ajedrez de 8x8 y simula los movimientos del caballo, destacando cada jugada en tiempo real.

## Características

- **Tablero de ajedrez visual**: Se genera un tablero de ajedrez de 8x8 utilizando la librería Tkinter para mostrar visualmente los movimientos del caballo.
- **Recorrido del caballo**: El programa resuelve el problema utilizando un enfoque heurístico, eligiendo los movimientos válidos del caballo.
- **Animación de movimientos**: A medida que el caballo se mueve por el tablero, las casillas se actualizan con el número de jugada y un sonido se reproduce para cada movimiento.
- **Coordenadas visibles**: Las filas y columnas del tablero tienen coordenadas alfabéticas y numéricas para facilitar la visualización.

## Requisitos

- **Python 3.x**: El programa está escrito en Python.
- **Librerías necesarias**: 
  - `tkinter`: Para la interfaz gráfica.
  - `time`: Para manejar los intervalos entre movimientos.
  - `winsound`: Para reproducir un sonido con cada movimiento del caballo (solo en Windows).

## Cómo ejecutar

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Instala las dependencias si no están ya instaladas:
   ```bash
   pip install tk
   ```
3. Guarda el código en un archivo Python (por ejemplo, `caballo_ajedrez.py`).
4. Ejecuta el script:
   ```bash
   python caballo_ajedrez.py
   ```

## Explicación del Código

1. **Funciones principales**:
   - `solve_knight_tour(n, start_x, start_y)`: Resuelve el problema del recorrido del caballo utilizando una heurística que prioriza los movimientos con menos opciones futuras.
   - `matrix_to_vector(matrix)`: Convierte la matriz de solución en un vector para facilitar la animación.
   - `fill_cells(root, cells_to_fill, vector_solution, index, a)`: Llena las casillas del tablero de ajedrez con los números de las jugadas del caballo, paso a paso.
   - `create_chess_board(root, size)`: Crea visualmente el tablero de ajedrez con Tkinter y muestra las coordenadas.
   - `play_tick_sound()`: Reproduce un sonido cuando el caballo se mueve (solo en Windows).

2. **Interfaz gráfica**:
   - Se utiliza la librería Tkinter para crear el tablero de ajedrez y actualizar las jugadas en tiempo real.

3. **Solución del recorrido**:
   - El programa utiliza una matriz para representar el tablero de ajedrez y resuelve el recorrido del caballo a partir de una casilla inicial, siguiendo un enfoque de "divide y vencerás" para minimizar los posibles caminos futuros.

## Notas adicionales

- **Personalización**: Puedes cambiar el tamaño del tablero modificando la variable `tamanoTablero` en la función `main`.
- **Compatibilidad**: El sonido está disponible solo en sistemas Windows, pero el programa puede ejecutarse en otros sistemas operativos eliminando o comentando la línea `winsound.Beep`.

Este programa es ideal para aquellos interesados en la visualización de algoritmos y la resolución de problemas clásicos de ajedrez.
