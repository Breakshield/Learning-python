import random

print("===Juego: Adivina el numero===")

# La computadora elige un numero del 1 al 100
numero_secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina el numero (1-100): "))

    if intento < numero_secreto:
        print("Muy bajo. Intenta otra vez.")
    elif intento > numero_secreto:
        print("Muy alto. Intenta otra vez.")
    else:
        print("Correcto! Adivinaste el numero.")
        break # Termina el juego