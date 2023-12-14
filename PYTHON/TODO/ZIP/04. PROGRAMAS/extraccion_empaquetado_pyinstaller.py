# Desempaquetado de archivos .exe
# creados a partir de pyinstaller

import subprocess

# Ruta al archivo .exe creado con PyInstaller
archivo_exe = input("Directorio: ")  # Reemplaza con la ruta de tu archivo .exe

# Comando para ejecutar la herramienta de extracción
comando_extraccion = f"python -m pyinstaller_extractor {archivo_exe}"

# Ejecutar el comando de extracción
try:
    resultado = subprocess.run(comando_extraccion, shell=True, check=True, text=True)
    print("Extracción completada exitosamente.")
except subprocess.CalledProcessError as e:
    print(f"Error durante la extracción: {e}")
except Exception as ex:
    print(f"Error inesperado: {ex}")
