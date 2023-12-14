# Ocultar CMD al ejecutar programa general y comprobar que el SO es Windows

import subprocess
import os

# Ruta al archivo .py que deseas ejecutar
archivo_programa = 'tu_programa.py'

# Comprueba si el sistema operativo es Windows
if os.name == 'nt':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # Ejecuta el programa ocultando la ventana CMD
    proceso = subprocess.Popen(['python', archivo_programa], startupinfo=startupinfo)
else:
    # Si no estás en Windows, simplemente ejecuta el programa
    proceso = subprocess.Popen(['python', archivo_programa])

# Espera a que el programa se complete
proceso.wait()
