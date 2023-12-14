import os

# Ruta al directorio que deseas acceder
directorio = "/ruta/a/tu/directorio"  # Reemplaza con la ruta de tu directorio

# Verificar si el directorio existe
if os.path.exists(directorio) and os.path.isdir(directorio):
    # Listar los archivos en el directorio
    archivos = os.listdir(directorio)

    # Mostrar los archivos en el directorio
    print(f"Archivos en el directorio '{directorio}':")
    for archivo in archivos:
        print(archivo)
else:
    print(f"El directorio '{directorio}' no existe o no es válido.")
