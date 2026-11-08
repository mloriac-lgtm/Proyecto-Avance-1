# ==============================================================================
# Archivo: ejercicio6_viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Roberto Ulate
# Fecha: 08/11/2026 Versión: 1.0
# Descripción: Simula día a día el viaje hacia el destino validando recursos
#              disponibles antes de cada consumo, sin utilizar break ni funciones.
# ==============================================================================

# Declaración de constantes de consumo diario fijo
CONSUMO_COMBUSTIBLE = 8
CONSUMO_ENERGIA = 5

# Entrada de datos
dias_viaje = int(input("Ingrese la cantidad de días del viaje: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de variables de control y contadores
dia_actual = 1
viaje_activo = True

# Ciclo para simular el paso de los días
while viaje_activo and dia_actual <= dias_viaje:
    # Cálculo del consumo diario dependiente de los tripulantes
    consumo_oxigeno_diario = 2 * tripulantes
    consumo_provisiones_diario = 1 * tripulantes

    # 1. Verificar antes del consumo si todos los recursos alcanzan
    if combustible >= CONSUMO_COMBUSTIBLE and oxigeno >= consumo_oxigeno_diario and energia >= CONSUMO_ENERGIA and provisiones >= consumo_provisiones_diario:
        # 2. Descontar consumo y actualizar estado
        combustible = combustible - CONSUMO_COMBUSTIBLE
        oxigeno = oxigeno - consumo_oxigeno_diario
        energia = energia - CONSUMO_ENERGIA
        provisiones = provisiones - consumo_provisiones_diario

        print("Día", dia_actual, "| Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
        
        # Incrementar contador de días
        dia_actual = dia_actual + 1
    else:
        # 3. Si algún recurso no alcanza, se detiene el viaje sin descontar el día
        viaje_activo = False

# Salidas obligatorias según el resultado del viaje
if dia_actual > dias_viaje:
    print()
    print("La nave llegó al destino en", dias_viaje, "días.")
    print("Combustible restante:", combustible, "unidades")
    print("Oxígeno restante:", oxigeno, "unidades")
    print("Energía restante:", energia, "unidades")
    print("Provisiones restantes:", provisiones, "unidades")
else:
    print()
    print("Viaje interrumpido en el día", dia_actual, ".")
    
    # Verificación de recursos insuficientes en orden estricto: combustible, oxígeno, energía, provisiones
    consumo_oxigeno_diario = 2 * tripulantes
    consumo_provisiones_diario = 1 * tripulantes

    if combustible < CONSUMO_COMBUSTIBLE:
        print("Recurso insuficiente: combustible")
    if oxigeno < consumo_oxigeno_diario:
        print("Recurso insuficiente: oxigeno")
    if energia < CONSUMO_ENERGIA:
        print("Recurso insuficiente: energia")
    if provisiones < consumo_provisiones_diario:
        print("Recurso insuficiente: provisiones")
        
    dias_completados = dia_actual - 1
    print("Días completados:", dias_completados)