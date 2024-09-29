import tkinter as tk

ventana = tk.Tk()
ventana.title("Interfaces gráficas de usuario.")
ventana.geometry("400x300")
#creo una etiqueta con tk.label
etiqueta = tk.Label(ventana, text="Bienvenidos.")
# Posiciona la etiqueta dentro de la ventana
etiqueta.pack()
etiqueta2 = tk.Label(ventana, text="Emanuel voltolini, Agustín Soto, Santino Zalazar")
etiqueta2.pack()
etiqueta3 = tk.Label(ventana, text="5ºD POO COLEGIO DE LA DIVINA MISERICORDIA")
etiqueta3.pack()
ventana.mainloop()

import tkinter as tk
import random as rd

class Adivinanza:
    def __init__(self, ventana):
        self.numero_secreto = rd.randint(1, 10)
        self.ventana = ventana
        self.posible_numero = tk.Entry(ventana)
        self.posible_numero.pack(pady=20)
        self.boton = tk.Button(ventana, text="Adivina", command=self.chequear_adivinanza)
        self.boton.pack(pady=10)
        self.label = tk.Label(ventana, text="")
        self.label.pack(pady=20)

    def chequear_adivinanza(self):
        adivinanza = self.posible_numero.get()
        if int(adivinanza) == self.numero_secreto:
            self.label.config(text="¡Felicitaciones, acertaste el número!")
        else:
            self.label.config(text="Ups... vuelve a intentarlo")

ventana = tk.Tk()
ventana.title("Juego de adivinanza")
ventana.geometry("300x200")
juego = Adivinanza(ventana)
ventana.mainloop()