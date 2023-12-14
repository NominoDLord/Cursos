import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensiones del tablero
filas = 50
columnas = 50

# Función para inicializar el tablero con células vivas o muertas de manera aleatoria
def inicializar_tablero(filas, columnas):
    tablero = np.zeros((filas, columnas))
    for i in range(filas):
        for j in range(columnas):
            tablero[i][j] = random.randint(0, 1)
    return tablero

# Función para calcular el siguiente estado del tablero según las reglas del Juego de la Vida
def siguiente_estado(tablero):
    nuevo_tablero = tablero.copy()
    for i in range(filas):
        for j in range(columnas):
            vecinos = tablero[max(0, i - 1):min(i + 2, filas), max(0, j - 1):min(j + 2, columnas)]
            suma_vecinos = int(np.sum(vecinos)) - int(tablero[i][j])
            if tablero[i][j] == 1 and (suma_vecinos < 2 or suma_vecinos > 3):
                nuevo_tablero[i][j] = 0
            elif tablero[i][j] == 0 and suma_vecinos == 3:
                nuevo_tablero[i][j] = 1
    return nuevo_tablero

# Función para actualizar el tablero en cada iteración
def actualizar_tablero(frameNum, img, tablero):
    nuevo_tablero = siguiente_estado(tablero)
    img.set_data(nuevo_tablero)
    tablero[:] = nuevo_tablero
    return img

# Crear el tablero inicial y la figura para la animación
tablero = inicializar_tablero(filas, columnas)
fig, ax = plt.subplots()
img = ax.imshow(tablero, interpolation='nearest')
ani = animation.FuncAnimation(fig, actualizar_tablero, fargs=(img, tablero), frames=50, interval=50)

plt.show()