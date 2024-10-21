
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo

def dibujar_rectangulo(canvas, rectangulo):
    x0 = 300
    y0 = 100
    x1 = x0 + rectangulo.ancho
    y1 = y0 + rectangulo.alto
    canvas.create_rectangle(x0, y0, x1, y1, outline="red", fill="lightcoral")

def dibujar_circulo(canvas, circulo):
    x = 100
    y = 100
    r = circulo.radio
    canvas.create_oval(x - r, y - r, x + r, y + r, outline="blue", fill="lightblue")

def dibujar_cuadrado(canvas, lado):
    x0 = 300
    y0 = 300
    x1 = x0 + lado
    y1 = y0 + lado
    canvas.create_rectangle(x0, y0, x1, y1, outline="green", fill="lightgreen")

def dibujar_elipse(canvas, ancho, alto):
    x0 = 100
    y0 = 250
    x1 = x0 + ancho
    y1 = y0 + alto
    canvas.create_oval(x0, y0, x1, y1, outline="yellow", fill="yellow")

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(50)
    rectangulo = Rectangulo(150, 100)
    lado_cuadrado = 100
    ancho_elipse = 150
    alto_elipse = 80
    
    # Dibujar
    dibujar_circulo(canvas, circulo)
    dibujar_rectangulo(canvas, rectangulo)
    dibujar_cuadrado(canvas, lado_cuadrado)
    dibujar_elipse(canvas, ancho_elipse, alto_elipse)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
