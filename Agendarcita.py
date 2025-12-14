
medicos = ["Dr. Perez", "Dra. Gonzalez", "Dr. Ramirez"]

citas = []

def agendar_cita():
    nombre = input("Nombre del paciente: ").strip().title()

    print("Médicos disponibles:")
    for i, medico in enumerate(medicos, start=1):
        print(f"{i}. {medico}")

    opcion_medico = input("Elige un médico (número): ")

    if not opcion_medico.isdigit():
        print("Debes ingresar un número")
        return

    opcion_medico = int(opcion_medico)

    if opcion_medico < 1 or opcion_medico > len(medicos):
        print("Médico inválido")
        return

    medico_elegido = medicos[opcion_medico - 1]

    fecha = input("Fecha de la cita: ")
    hora = input("Hora de la cita: ")

    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    for cita in citas:
        if (
            cita["fecha"] == fecha and
            cita["hora"] == hora and
            cita["medico"] == medico_elegido
        ):
            print("Ese médico ya tiene una cita en ese horario.")
            return

    cita_nueva = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "medico": medico_elegido
    }

    citas.append(cita_nueva)
    print("Cita agendada")


def ver_citas():
    if len(citas) == 0:
        print("No hay citas")
    else:
        for cita in citas:
            print("   Paciente:", cita["nombre"])
            print("   Medico:", cita["medico"])
            print("   Fecha:", cita["fecha"])
            print("   Hora :", cita["hora"])
            print("-" * 30)


def guardar_citas():
    with open("citas.txt", "w") as archivo:
        for cita in citas:
            linea = (
                cita["nombre"] + ";" +
                cita["fecha"] + ";" +
                cita["hora"] + ";" +
                cita["medico"]
            )
            archivo.write(linea + "\n")


def cargar_citas():
    try:
        with open("citas.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                cita = {
                    "nombre": datos[0],
                    "fecha": datos[1],
                    "hora": datos[2],
                    "medico": datos[3]
                }

                citas.append(cita)
    except FileNotFoundError:
        pass

cargar_citas()

def buscar_citas():
    print("\nBuscar citas por:")
    print("1. Paciente")
    print("2. Medico")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre_buscar = input("Nombre del paciente: ").strip().lower()
        encontrado = False

        for cita in citas:
            if cita["nombre"].lower() == nombre_buscar:
                print("   Paciente:", cita["nombre"])
                print("   Médico :", cita["medico"])
                print("   Fecha  :", cita["fecha"])
                print("   Hora   :", cita["hora"])
                print("-" * 30)
                encontrado = True

        if not encontrado:
            print("No se encontraron citas para ese paciente")

    elif opcion == "2":
        print("Médicos disponibles:")
        for medico in medicos:
            print("-", medico)

        medico_buscar = input("Nombre del médico: ").strip().lower()
        encontrado = False

        for cita in citas:
            if cita["medico"].lower() == medico_buscar:
                print("   Paciente:", cita["nombre"])
                print("   Médico :", cita["medico"])
                print("   Fecha  :", cita["fecha"])
                print("   Hora   :", cita["hora"])
                print("-" * 30)
                encontrado = True

        if not encontrado:
            print("No se encontraron citas para ese médico")

    else:
        print("Opción inválida")

def cancelar_cita():
    if len(citas) == 0:
        print("No hay citas para cancelar")
        return

    print("\nCitas agendadas:")
    for i, cita in enumerate(citas, start=1):
        print(f"{i}. {cita['nombre']} | {cita['medico']} | {cita['fecha']} | {cita['hora']}")

    opcion = input("Elige el número de la cita a cancelar: ")

    if not opcion.isdigit():
        print("Debes ingresar un número")
        return

    opcion = int(opcion)

    if opcion < 1 or opcion > len(citas):
        print("Número de cita inválido")
        return

    cita = citas[opcion - 1]

    print("\nVas a cancelar esta cita:")
    print("Paciente:", cita["nombre"])
    print("Médico :", cita["medico"])
    print("Fecha  :", cita["fecha"])
    print("Hora   :", cita["hora"])

    confirmar = input("¿Confirmar cancelación? (s/n): ").lower()

    if confirmar == "s":
        citas.pop(opcion - 1)
        guardar_citas()
        print("Cita cancelada correctamente")
    else:
        print("Cancelación anulada")




while True:
    print("\n=== Centro Hospitalario ===")
    print("1. Agendar cita")
    print("2. Ver citas")
    print("3. Salir")
    print("4. Buscar citas")
    print("5. Cancelar cita")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agendar_cita()
    elif opcion == "2":
        ver_citas()
    elif opcion == "3":
        guardar_citas()
        print("Saliendo del sistema")
        break
    elif opcion == "4":
        buscar_citas()
    elif opcion == "5":
        cancelar_cita()

    else:
        print("Opción inválida")
