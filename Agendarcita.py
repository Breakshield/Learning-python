citas = []

while True: 
    print("\n=== Centro Hospitalario ===")
    print("1. Agendar cita")
    print("2. Ver citas")
    print("3. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        fecha = input("Fecha de la cita: ")
        hora = input("Hora de la cita: ")

        cita = {
            "nombre": nombre,
            "fecha": fecha,
            "hora": hora
        }

        citas.append(cita)
        print("Cita agendada")

    elif opcion == "2":
        if len(citas) == 0:
            print("No hay citas")
        else: 
            for cita in citas:
                print(
                    "Paciente", cita["nombre"],
                    "| Fecha", cita["fecha"],
                    "| Hora:", cita["hora"]
                )

    elif opcion == "3":
        print("Saliendo del sistema")
        break

    else:
        print("Opcion invalida")
