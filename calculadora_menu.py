print("==Calculadora con Menu==")

while True: #Repite el programa hasta que elejas salir
    print("Elige una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingresa el numero de la opcion: ")

    if opcion == "5":
        print("Saliendo... Gracias por usar la calculadora!")
        break # Sale del bucle y termina el programa

    # Pedimos numeros solo si la opcion es valida
    if opcion in ["1","2","3","4"]:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))

        if opcion == "1":
            resultado = num1 + num2
        elif opcion == "2":
            resultado = num1 - num2
        elif opcion == "3":
            resultado = num1 * num2
        elif opcion == "4":
            # Evitar dviidir entre cero
            if num2 == 0:
                print("Error: no puedes dividir entre cero.")
                continue
            resultado = num1 / num2

        print("Resultado:", resultado)

    else:
        print("Opcion no valida. Intente otra vez.")