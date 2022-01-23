# Preguntas & Respuestas GUI
from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main.withdraw()

preguntas = [ "¿Cual es la capital de Argentina",
              "¿En que año se creo el primer ordenador?",
              "¿Quien fue la primer persona en pisar la luna? (Nombre completo)",
              "¿En que año fue el atentado del 911?",
              "¿Quien descubrio America?"]

respuesta = [ "Buenos Aires", 
           "1942",
           "Neil Alden Armstrong",
           "2001",
           "Cristóbal Colón"]


puntaje = 0

for i in range(0, len(preguntas)):
    print(preguntas[i])
    p1_respuesta = simpledialog.askstring(preguntas[i], "Respuesta: ")

    if p1_respuesta == respuesta[i]:
        messagebox.showinfo("Correcto", "Correcto")
        puntaje = puntaje + 1
    else:
        messagebox.showinfo("Error!", "Te equivocaste.")

messagebox.showinfo("Puntaje", str(puntaje))
