#  Misión Órbita 
## María Fernada Loría Campos
## Roberto Ulaten Antonieta
## Sofia Cabas Madrigal 

## Ejercicio 1: Cálculo de recursos necesarios para una misión 
Antes de autorizar una misión, la agencia necesita determinar aproximadamente cuántos 
recursos serán necesarios para realizar el viaje.  
Datos solicitados: 
• Nombre de la misión. 
• Cantidad de tripulantes. 
• Cantidad de días estimados para legar al destino. 
Cálculos requeridos: 
● Combustible de ida: por cada día de viaje se consumen 8 unidades de combustible. 
Combustible de ida = días de viaje × 8 
● Combustible de regreso: el viaje de regreso tiene la misma duración que el de ida y 
consume también 8 unidades por día.  
Combustible de regreso = días de viaje × 8 
Combustible total requerido = combustible de ida + combustible de regreso + 10 
● Reserva: toda misión debe transportar 10 unidades adicionales de combustible para 
emergencias. 
● Oxígeno: cada tripulante consume 2 unidades de oxígeno por día durante el viaje de 
ida y regreso. Además, se agregan 5 unidades de emergencia. 
Oxígeno requerido = días de viaje × 2 × 2 × tripulantes + 5 
● Energía: la nave consume 5 unidades de energía por día durante el viaje de ida y 
regreso, además de 10 unidades para las operaciones de exploración. 
Energía requerida = días de viaje × 5 × 2 + 10 
● Provisiones: cada tripulante consume 1 unidad de provisiones por día durante el viaje 
de ida y regreso. Además, se agregan 3 unidades adicionales. 
Provisiones requeridas = días de viaje × tripulantes × 2 + 3 
Salida esperada (ejemplo): 
Misión: Explorador I 
Tripulantes: 3 
Duración estimada hasta el destino: 5 días 
Combustible para llegar: 40 unidades 
Combustible para regresar: 40 unidades 
Reserva de combustible: 10 unidades 
Combustible total requerido: 90 unidades 
Oxígeno requerido: 65 unidades 
Energía requerida: 60 unidades 
Provisiones requeridas: 33 unidades 

## Ejercicio 2: Verificación de combustible 
La agencia necesita verificar si una nave posee suficiente combustible antes de continuar con 
la preparación de la misión. Este ejercicio debe utilizar una estructura condicional simple. 
Datos solicitados: 
• Cantidad de combustible disponible. 
• Cantidad de combustible requerida para el viaje de ida. 
• Cantidad de combustible requerida para el viaje de regreso. 
Cálculos requeridos: 
● El combustible total requerido para completar la misión incluye el viaje de ida, el viaje 
de regreso y una reserva de emergencia de 10 unidades. 
● Combustible total requerido = combustible de ida + combustible de regreso + 10 
● Combustible adicional = combustible disponible − combustible total requerido 
● Regla de advertencia: Si el combustible adicional es menor que 10 unidades, mostrar: 
“Advertencia: el margen adicional de combustible es bajo.” 
Salidas obligatorias:  
El programa debe mostrar siempre: combustible disponible, combustible requerido para legar, 
combustible requerido para regresar, reserva de emergencia y combustible total requerido. 

## Ejercicio 3: Verificación del soporte para la tripulación 
Antes de autorizar la misión, es necesario verificar si existen suficientes recursos para mantener 
a toda la tripulación durante el viaje.  
Datos solicitados: 
• Cantidad de oxígeno disponible. 
• Cantidad de oxígeno requerido. 
• Cantidad de provisiones disponibles. 
• Cantidad de provisiones requeridas. 
Regla de decisión:  
La misión podrá brindar soporte adecuado a la tripulación únicamente cuando el oxígeno 
disponible sea mayor o igual que el requerido y las provisiones disponibles sean mayores o 
iguales que las requeridas. 
• Si ambas condiciones se cumplen: “La nave posee recursos suficientes para la 
tripulación.” 
• En caso contrario: “La nave no posee recursos suficientes para la tripulación.” 
Este ejercicio debe utilizar una estructura condicional doble (if/else) y no debe indicar cuál 
recurso específico presenta el problema. 

## Ejercicio 4: Autorización inicial de lanzamiento 
La agencia necesita realizar una verificación general antes de permitir el lanzamiento. Se 
debe utilizar una estructura condicional doble sin condicionales anidadas. 
Datos solicitados: 
• Combustible disponible. 
• Combustible requerido para legar al destino. 
• Combustible requerido para regresar. 
• Oxígeno disponible y oxígeno requerido. 
• Energía disponible y energía requerida. 
• Provisiones disponibles y provisiones requeridas. 
Cálculo requerido:  
● Combustible total requerido = combustible de ida + combustible de regreso + 10 
● Regla de autorización: La misión únicamente podrá ser autorizada cuando se cumplan 
todas las condiciones siguientes: 
◦ El combustible disponible es mayor o igual que el combustible total requerido. 
◦ El oxígeno disponible es mayor o igual que el requerido. 
◦ La energía disponible es mayor o igual que la requerida. 
◦ Las provisiones disponibles son mayores o iguales que las requeridas. 
Esto significa que una misión no deberá autorizarse si solamente existe combustible para 
llegar al destino: desde el inicio debe existir combustible suficiente para el viaje de regreso y la 
reserva establecida. 
• Si se cumple la condición: “Lanzamiento autorizado.” 
• En caso contrario: “Lanzamiento no autorizado. La misión debe ser revisada.” 
En este ejercicio todavía no deberá indicarse cuál recurso provocó el rechazo.