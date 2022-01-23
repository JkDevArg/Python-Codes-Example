#Adivinar Número

from random import randint

num_aleatorio = randint(0,10)
print(num_aleatorio)

x = -1
while x != num_aleatorio:
    if x != -1:
        print("Num Incorrecto")

    x = input("Ingresa un número: ")
    x = int(x)
    

print("Has acertado el número") 
