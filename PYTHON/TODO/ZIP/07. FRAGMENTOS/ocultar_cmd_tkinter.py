# Ocultar CMD al ejecutar ventana tkinter

import tkinter as tk
import subprocess

# Función para ejecutar tu programa Python
def ejecutar_programa():
    # Reemplaza 'tu_programa.py' con el nombre de tu archivo Python
    archivo_programa = 'tu_programa.py'
    subprocess.Popen(['cmd', '/c', 'python', archivo_programa])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejecutar Programa Python")
ventana.geometry("300x100")

# Botón para ejecutar el programa
boton_ejecutar = tk.Button(ventana, text="Ejecutar Programa", command=ejecutar_programa)
boton_ejecutar.pack(pady=20)

ventana.mainloop()
