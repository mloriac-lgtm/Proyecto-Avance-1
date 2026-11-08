# ==============================================================================
# Archivo: ejercicio5_destino.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Roberto Ulate
# Fecha: 08/11/2026 Versión: 1.0
# Descripción: Selecciona el destino de la misión, calcula recursos requeridos
#              mediante condicionales múltiples y anidadas, y autoriza el lanzamiento.
# ==============================================================================

# Declaración de constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos iniciales
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
opcion_destino = int(input("Seleccione el destino (1: Luna, 2: Marte, 3: Europa): "))

# 1. Validación de la opción de destino
if opcion_destino < 1 or opcion_destino > 3:
    print("Opción de destino no válida. La misión no puede planificarse.")
else:
    # 2. Duración del viaje según la opción (Condicional múltiple)
    if opcion_destino == 1:
        nombre_destino = "Luna"
        dias_viaje = 3
    elif opcion_destino == 2:
        nombre_destino = "Marte"
        dias_viaje = 5
    else:
        nombre_destino = "Europa"
        dias_viaje = 7

    # Solicitud de recursos disponibles (solo si la opción es válida)
    combustible_disponible = int(input("Ingrese el combustible disponible: "))
    oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
    energia_disponible = int(input("Ingrese la energía disponible: "))
    provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

    # 3. Cálculo de recursos requeridos
    combustible_ida = dias_viaje * 8
    combustible_regreso = dias_viaje * 8
    combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = dias_viaje * 2 * 2 * tripulantes + 5
    energia_requerida = dias_viaje * 5 * 2 + 10
    provisiones_requeridas = dias_viaje * tripulantes * 2 + 3

    # Salidas obligatorias: Resumen de la misión
    print()
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)
    print("Combustible disponible:", combustible_disponible, "| requerido:", combustible_total_requerido, "unidades")
    print("Oxígeno disponible:", oxigeno_disponible, "| requerido:", oxigeno_requerido, "unidades")
    print("Energía disponible:", energia_disponible, "| requerida:", energia_requerida, "unidades")
    print("Provisiones disponibles:", provisiones_disponibles, "| requeridas:", provisiones_requeridas, "unidades")

    # 4. Autorización de la misión (Condicional anidada)
    if combustible_disponible >= combustible_total_requerido and oxigeno_disponible >= oxigeno_requerido and energia_disponible >= energia_requerida and provisiones_disponibles >= provisiones_requeridas:
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")