# Preguntas y Respuestas

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
    p1_respuesta = input("Respuesta: ")

    if p1_respuesta == respuesta[i]:
        print("Correcto") 
        puntaje = puntaje + 1
    else:
        print("Incorrecto")

print(f"Puntaje Final: {puntaje} ")
