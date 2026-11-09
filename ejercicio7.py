# ============================================================
# Archivo: ejercicio7viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Sofía Cabas, María Fernanda Loria, Roberto Ulate
# Fecha: 8/11/2026       Versión: 1.0
# Descripción: Administrar los recursos y las actividades científicas realizadas durante la exploración.
# ============================================================

# Declaración de constantes

OPCION_ANALIZAR = 1
OPCION_RECOLECTAR = 2
OPCION_OBSERVACION = 3
OPCION_FINALIZAR = 4 

ENERGIA_ANALIZAR = 8
ENERGIA_RECOLECTAR = 12
ENERGIA_OBSERVACION = 5

PROVISIONES_ANALIZAR = 0
PROVISIONES_RECOLECTAR = 2
PROVISIONES_OBSERVACION = 0

PUNTOS_ANALIZAR = 10
PUNTOS_RECOLECTAR = 20
PUNTOS_OBSERVACION = 8

# Datos de entrada

energia_disponible = int(input("Ingrese la cantidad de energía disponible al llegar al destino: "))

provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles al llegar al destino: "))

# Contadores 

puntos_cientificos = 0

actividades_realizadas = 0

muestras_recolectadas = 0

# Variable de control

exploracion_activa = True

# Procesamientos

# Ciclo de actividades

while exploracion_activa == True:
    
    print("\n--- Actividades de exploración científica ---")
    
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    selecion_actividad = int(input("Selecione una actividad (1,2,3,4): "))

# Contador de actividades
    
    actividad_seleccionada = 0

# La actividad escogida

    if selecion_actividad == OPCION_ANALIZAR:
       
       nombre_actividad = "Analizar terreno"
       consumo_energia = ENERGIA_ANALIZAR
       consumo_provisiones = PROVISIONES_ANALIZAR
       puntos_actividad = PUNTOS_ANALIZAR

       actividad_seleccionada = 1

    elif selecion_actividad == OPCION_RECOLECTAR:
        
        nombre_actividad = "Recolectar muestra"
        consumo_energia = ENERGIA_RECOLECTAR
        consumo_provisiones = PROVISIONES_RECOLECTAR
        puntos_actividad = PUNTOS_RECOLECTAR

        actividad_seleccionada = 1

    elif selecion_actividad == OPCION_OBSERVACION:
        
        nombre_actividad = "Realizar observación"
        consumo_energia = ENERGIA_OBSERVACION
        consumo_provisiones = PROVISIONES_OBSERVACION
        puntos_actividad = PUNTOS_OBSERVACION

        actividad_seleccionada = 1

    elif selecion_actividad == OPCION_FINALIZAR:

        print("Exploración finalizada por la tripulación.")
        exploracion_activa = False

    else: 

        print("Opción no valida. Debe ingresar: 1, 2, 3 o 4")

# Verificar recursos y realizar actividad
   
    if actividad_seleccionada == 1:

        if energia_disponible >= consumo_energia and provisiones_disponibles >= consumo_provisiones:

# Procesos aritméticos
          
          energia_disponible = energia_disponible - consumo_energia
          provisiones_disponibles = provisiones_disponibles - consumo_provisiones
          actividades_realizadas += 1
          puntos_cientificos = puntos_cientificos + puntos_actividad

          if selecion_actividad == OPCION_RECOLECTAR:

                muestras_recolectadas += 1

          print("Actividad realizada:", nombre_actividad,"." , "Puntos obtenidos", puntos_actividad)

        else:
            print("Recursos insuficiente para realizar la actividad. La exploración finaliza")
            exploracion_activa = False

# Salidas de resultados

print("Actividades realizadas:", actividades_realizadas)
print("Muestras recoloctadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible, "unidades")
print("Provisiones restantes:", provisiones_disponibles, "unidades")

       
    