import tkinter as tk

# Función que se ejecutará cuando se haga clic en el botón

def saludar():
    label.config(text="¡Hola, mundo!")

# Crear una ventana principal
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Interfaz Gráfica v0.0.0")


# Crear una etiqueta
label = tk.Label(ventana, text="Presiona el botón para saludar")
label.pack(pady=50)

# Crear un botón
button = tk.Button(ventana, text="Saludar", command=saludar)
button.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
