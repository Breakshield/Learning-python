import random

print("=== Juego: Adivina el numero ===")

while True:  # Para volver a jugar sin cerrar el programa
    print("Modo de juego:")
    print("1. Normal (intentos ilimitados)")
    print("2. Dificil (solo 7 intentos)")

    modo = input("Elige un modo (1 o 2): ")

    # Elegir intentos segun modo
    if modo == "1":
        intentos_max = None  # ilimitados
    elif modo == "2":
        intentos_max = 7
        print("Modo dificil: SOLO 7 INTENTOS!")
    else:
        print("Opcion invalida.")
        continue

    # Numero secreto
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Adivina el numero (1-100): "))
        intentos += 1   # ← ESTE ES EL CORRECTO

        # Mostrar si esta caliente, tibio o frio
        diferencia = abs(intento - numero_secreto)
        if diferencia == 0:
            print("Correcto!")
        elif diferencia <= 5:
            print("Muy caliente!")
        elif diferencia <= 10:
            print("Tibio!")
        else:
            print("Frio")

        # Comparar el intento
        if intento < numero_secreto:
            print("Muy bajo.")
        elif intento > numero_secreto:
            print("Muy alto.")
        else:
            print(f"GANASTE EN {intentos} intentos! ")
            break

        # Revisa si perdio en modo dificil
        if intentos_max is not None and intentos >= intentos_max:
            print(f"Se acabaron los intentos. El numero era {numero_secreto}.")
            break

    #  ← ESTA PARTE DEBE IR AQUI, FUERA DEL WHILE DEL JUEGO
    otra = input("Quieres jugar de nuevo? (S/N): ")
    if otra.lower() != "s":
        print("Gracias por jugar!")
        break
