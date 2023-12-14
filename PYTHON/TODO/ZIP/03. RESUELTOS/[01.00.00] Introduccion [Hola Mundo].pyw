"""
    NOMBRE DEL PROGRAMA:
    - Hola Mundo

    APTITUDES: [Nivel B]
    - CMD
    - Variables
    - In/Out-put
    - Bibliotecas
    - Interfaz Gráfica
    
    DESCRIPCIÓN:
    - Crea un programa que abra un ventana.
        - Establece una dimensión para la ventana.
    - Crea dos botones dentro de la ventana:
        - Botón 1: Saludar
        - Botón 2: Despedir
    - Acción de los botones:
        - Imprimir un mensaje dentro de la ventana.
            - Botón 1: "Hola Mundo"
            - Botón 2: "Adión Mundo"

    AUTOR: Nômino D Lord
    FECHA: 2023/10
"""

import tkinter as tk

# Funciones para las acciones de los botones
def saludar():
    mensaje.config(text="Hola Mundo")

def despedir():
    mensaje.config(text="Adiós Mundo")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Saludo y Despedida")

# Establecer dimensiones de la ventana
ventana.geometry("400x200")

# Etiqueta para mostrar el mensaje
mensaje = tk.Label(ventana, text="", font=("Arial", 20))
mensaje.pack(pady=20)

# Botón para saludar
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=10)

# Botón para despedir
boton_despedir = tk.Button(ventana, text="Despedir", command=despedir)
boton_despedir.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
