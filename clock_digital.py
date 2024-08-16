import random
import tkinter as tk
import datetime


def actualizar_hora():
    hora = datetime.datetime.now()
    hora_formatted = hora.strftime("%H:%M:%S")

    # Actualizamos el texto del label
    actualizer_color(hora_formatted)
    ventana.after(1000, actualizar_hora)  # Llamamos a la función cada 1000 ms (1 segundo)


def actualizer_color(hora_formatted):
    colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "white"]
    color_choice = random.choice(colors)
    label.config(text=hora_formatted, background=color_choice)
    marco1.config(background=color_choice)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reloj")

# Crear el label
marco1 = tk.Frame(ventana, width=200, height=100, bd=9, relief="solid", bg="blue")
marco1.pack()

label = tk.Label(marco1, font=("Arial", 40), bg="green", fg="black")
label.pack(pady=20)

# Iniciar la actualización de la hora
actualizar_hora()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
