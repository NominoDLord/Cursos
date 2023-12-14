from PIL import Image
import hashlib

def image_hash(image_path):
    image = Image.open(image_path)
    image_hash = hashlib.md5(image.tobytes()).hexdigest()
    return image_hash

def compare_images(image_path1, image_path2):
    hash1 = image_hash(image_path1)
    hash2 = image_hash(image_path2)

    similarity = sum(c1 == c2 for c1, c2 in zip(hash1, hash2)) / len(hash1)
    return similarity

# Ejemplo de uso:
image_path1 = "C:/Users/Ferran/Pictures/Screenshots/Captura_01.png"
image_path2 = "C:/Users/Ferran/Pictures/Screenshots/Captura_03.png"

similarity_score = compare_images(image_path1, image_path2)

if similarity_score > 0.9:  # Ajusta este umbral según tus necesidades
    print("Las imágenes son iguales.")
else:
    print("Las imágenes son diferentes.")

########################################################################################################################

# from PIL import Image
# import imagehash

# def comparar_imagenes(imagen1, imagen2, umbral=5):
    # hash_imagen1 = imagehash.average_hash(Image.open(imagen1))
    # hash_imagen2 = imagehash.average_hash(Image.open(imagen2))

    # diferencia = hash_imagen1 - hash_imagen2

    # if diferencia < umbral:
        # return True  # Imágenes parecidas o iguales
    # else:
        # return False  # Imágenes diferentes

# if __name__ == "__main__":
    # ruta_imagen1 = "C:/Users/Ferran/Pictures/Screenshots/Captura_01.png"  # Reemplaza con la ruta de tu primera imagen
    # ruta_imagen2 = "C:/Users/Ferran/Pictures/Screenshots/Captura_02.png"  # Reemplaza con la ruta de tu segunda imagen

    # if comparar_imagenes(ruta_imagen1, ruta_imagen2):
        # print("Verdadero: Las imágenes son iguales o tienen un parecido alto.")
    # else:
        # print("Falso: Las imágenes son diferentes.")

########################################################################################################################

# from PIL import Image

# def comparar_imagenes(imagen1, imagen2):
    # # Abre las imágenes
    # img1 = Image.open(imagen1)
    # img2 = Image.open(imagen2)

    # # Convierte las imágenes a escala de grises (opcional)
    # img1 = img1.convert('L')
    # img2 = img2.convert('L')

    # # Obtiene los datos de píxeles
    # pixeles1 = list(img1.getdata())
    # pixeles2 = list(img2.getdata())

    # # Compara los datos de píxeles
    # if pixeles1 == pixeles2:
        # print("Las imágenes son idénticas.")
    # else:
        # print("Las imágenes son diferentes.")

# # Rutas de las imágenes que deseas comparar
# imagen_path1 = "ruta_de_la_imagen1.jpg"
# imagen_path2 = "ruta_de_la_imagen2.jpg"

# # Llama a la función de comparación
# comparar_imagenes(imagen_path1, imagen_path2)

########################################################################################################################