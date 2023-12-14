# Abrir una ventana y seleccionar un archivo
# usando biblio.



import tkinter as tk
from tkinter import filedialog

# Crear una ventana raíz (main window)
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Mostrar un cuadro de diálogo "Abrir archivo" y obtener la ruta del archivo seleccionado
archivo_seleccionado = filedialog.askopenfilename()

# Comprobar si el usuario seleccionó un archivo
if archivo_seleccionado:
    print(f"Archivo seleccionado: {archivo_seleccionado}")
else:
    print("Ningún archivo seleccionado")

# Cerrar la ventana raíz (main window)
root.destroy()
