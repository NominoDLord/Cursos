"""
    NOMBRE DEL PROGRAMA:
    Función recursiva finita

    APTITUDES:
    CMD
    Variables
    Condicionales
    Funciones
    f-string
    Recursividad
    Excepciones

    DESCRIPCIÓN:
    Este programa trata el tema de las excepciones.
    En caso de producirse un error,
    el programa, en lugar de detenerse
    lanzará un aviso al usuario indicando que el
    valor introducido es incorrecto y volvera a
    repetir el proceso de introducción del valor.
    
    AUTOR: Nômino D Lord
    FECHA: 2023/10
"""

def bucle_finito(x):
    y = 0
    x -= 1

    if x < 0:
        print(f"Número de repeticiones: {numero_de_repeticiones}")
        return
    else:
        print("Hola Mundo")

        if y == x:
            print("Número de repeticiones: {}".format(numero_de_repeticiones))
            return
        else:
            bucle_finito(x)

try:
    numero_de_repeticiones = int(input("Introduce el número de repeticiones: "))

    if numero_de_repeticiones < 0:
        print("El valor introducido es un número negativo.\nPor favor, introduzca un número entero positivo.")
    else:
        bucle_finito(numero_de_repeticiones)
        
except Exception:
    print("El valor introducido no es valido.\nPor favor, introduzca un número entero positivo.")