import random

numero_secreto=random.randint(1,100)
cant_intentos=0
cant_maxinte_intentos=5
adivinado=False

print("Bienvenido al juego de adivinar el número secreto!")

while not adivinado:
    if not cant_intentos < cant_maxinte_intentos:
        print("Game Over, has superado el número máximo de intentos")
        break
        


    entrada= input("Introduce un numero del 1 al 99: ") 
    numero= int(entrada)
    if numero == numero_secreto:
        print("¿Felicitaciones, has adivinado el número secreto!")
        adivinado=True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
 
    cant_intentos+=1
