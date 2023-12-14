import pyautogui
import time

def mover_raton_a(posicion_x, posicion_y, duracion):
    # Obtiene la posición actual del ratón
    inicio_x, inicio_y = pyautogui.position()

    # Calcula la distancia a recorrer en cada eje
    distancia_x = posicion_x - inicio_x
    distancia_y = posicion_y - inicio_y

    # Calcula la velocidad del ratón (distancia / tiempo)
    velocidad_x = distancia_x / duracion
    velocidad_y = distancia_y / duracion

    # Mueve el ratón hacia la posición deseada
    tiempo_inicio = time.time()
    tiempo_transcurrido = 0

    while tiempo_transcurrido < duracion:
        tiempo_transcurrido = time.time() - tiempo_inicio
        nueva_posicion_x = inicio_x + velocidad_x * tiempo_transcurrido
        nueva_posicion_y = inicio_y + velocidad_y * tiempo_transcurrido
        pyautogui.moveTo(nueva_posicion_x, nueva_posicion_y)
        time.sleep(0.001)  # Pequeño retraso para evitar movimientos bruscos

    # Asegura que el ratón esté en la posición final exacta
    pyautogui.moveTo(posicion_x, posicion_y)

# Ejemplo de uso: mover el ratón a la posición (500, 500) en 2 segundos
mover_raton_a(300, 300, 3)
mover_raton_a(600, 300, 3)
mover_raton_a(600, 600, 2)
mover_raton_a(300, 600, 2)