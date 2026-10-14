# ============================================================ 
# Archivo: caso3avance1.py 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6 
# Integrantes: Sofia Cabas 1, Maria Loria 2, Roberto Ulate 3
# Fecha: 13/10/2026    
# Ejercicio: #3    
# Descripción: Verifica si la nave cuenta con suficientes recursos de oxígeno y provisiones para la tripulación. 
# ============================================================ 


# Datos de Entrada
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))


# Procesamiento
# Se evalúa que ambos recursos cumplan con lo requerido.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    resultado = "La nave posee recursos suficientes para la tripulación."
else:
    resultado = "La nave no posee recursos suficientes para la tripulación."


# Datos de Salida
print(resultado)
