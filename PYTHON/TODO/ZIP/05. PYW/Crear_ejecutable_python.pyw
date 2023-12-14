## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##                                                                      ##
##      AUTOR: Nômino D Lord                                            ##
##      FECHA: 2023/--                                                  ##
##                                                                      ##
##      NOMBRE DEL PROGRAMA:                                            ##
##      - Crear ejecutable python                                       ##
##                                                                      ##
##      DESCRIPCIÓN:                                                    ##
##      - Crear un ejecutable a partir de un archivo .py/.pyw           ##
##      - usando la biblioteca 'pyinstaller' en un entorno gráfico.     ##
##      - Al finalizar el empaquetado se elimina el archivo '.spec'     ##
##      - y la carpeta 'build' creadas durante el proceso.              ##
##                                                                      ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

import tkinter as tk
from tkinter import filedialog
import subprocess
import shutil
import os

## FUNCIONES DEL PROGRAMA

# Función para seleccionar el archivo .py
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Python", "*.py *.pyw")])
    if archivo:
        archivo_elegido.set(archivo)

# Función para ejecutar PyInstaller
def ejecutar_pyinstaller():
    archivo = archivo_elegido.get()
    if archivo and os.path.isfile(archivo):
        try:
            cmd = f'pyinstaller --onefile "{archivo}"'
            subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            mensaje.set("Acción finalizada")
            
            # Eliminar la carpeta 'build' y su contenido
            build_path = os.path.join(os.path.dirname(archivo), 'build')
            if os.path.exists(build_path):
                try:
                    shutil.rmtree(build_path)
                except Exception as e:
                    mensaje.set(f"Error al eliminar la carpeta 'build': {str(e)}")

            # Eliminar el archivo '.spec'
            spec_file = archivo.replace('.py', '.spec')
            if os.path.exists(spec_file):
                try:
                    os.remove(spec_file)
                except Exception as e:
                    mensaje.set(f"Error al eliminar el archivo '.spec': {str(e)}")
        except Exception as e:
            mensaje.set(f"Error: {str(e)}")
    else:
        mensaje.set("Selecciona un archivo Python válido")


## DISEÑO DE VENTANA PRINCIPAL

# Crear ventana
ventana = tk.Tk()
ventana.title("Ejecutar PyInstaller")
ventana.geometry("600x300")

archivo_elegido = tk.StringVar()
mensaje = tk.StringVar()

# Botón para seleccionar archivo
boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=10)

# Campo de texto para mostrar el archivo seleccionado
etiqueta_archivo = tk.Label(ventana, textvariable=archivo_elegido)
etiqueta_archivo.pack()

# Botón para ejecutar PyInstaller
boton_ejecutar = tk.Button(ventana, text="Ejecutar PyInstaller", command=ejecutar_pyinstaller)
boton_ejecutar.pack(pady=10)

# Etiqueta para mostrar mensajes
etiqueta_mensaje = tk.Label(ventana, textvariable=mensaje, fg="blue")
etiqueta_mensaje.pack()

ventana.mainloop()
