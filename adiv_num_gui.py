# Adivinar Número GUI

from random import randint
from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main.withdraw()

num_aleatorio = randint(0,10)
print(num_aleatorio)

x = -1
while x != num_aleatorio:
    if x != -1:
        messagebox.showinfo("Error", "Num incorrecto")

    x = simpledialog.askstring("Número", "Ingresa un número: ")
    x = int(x)

    if x == num_aleatorio:
        messagebox.showinfo("Exito!", "Número acertado!") 
        exit()

main.mainloop() 
