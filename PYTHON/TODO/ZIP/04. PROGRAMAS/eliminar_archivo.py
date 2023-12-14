import os


# Ruta al directorio que deseas acceder
directorio = input("Ruta del directorio al archivo: ")

# Ruta al archivo que deseas eliminar
archivo_a_eliminar = "Crear_ejecutable_python.spec"  # Reemplaza con la ruta de tu archivo

# Verificar si el archivo existe antes de intentar eliminarlo
if os.path.exists(archivo_a_eliminar):
    try:
        # Eliminar el archivo
        os.remove(archivo_a_eliminar)
        print(f"El archivo {archivo_a_eliminar} ha sido eliminado exitosamente.")
    except OSError as e:
        print(f"No se pudo eliminar el archivo {archivo_a_eliminar}. Error: {e}")
else:
    print(f"El archivo {archivo_a_eliminar} no existe.")
