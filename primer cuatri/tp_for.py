"""
 Supongamos que está trabajando en desarrollar el programa de carga de una encuesta.
 1- Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
 2- Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
 3- Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
 encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
 4- Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
 generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
 bien cargados.
 5- Dada la siguiente lista de ingresos horarios:
 [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
 a) Calcular el promedio de ingresos/hora del 20% que más gana.
 b) Calcular el promedio de ingresos/hora de todos los respondentes.
 c) Buscar cuál es el valor que más se repite.
 d) Calcular la media geométrica
"""
suma_ingresos = 0




nombre = str(input ('Ingrese el nombre y apellido del encuestado: '))

salario = int(input('Ingrese el salario mensual: '))

horas_trabajadas = int(input('Ingrese sus horas trabajadas la semana anterior (entre 0 y 120): '))

while horas_trabajadas < 0 or horas_trabajadas > 120:
    horas_trabajadas = int(input("Error: El valor debe estar entre 0 y 120. Intentar de nuevo: "))

ingreso_horario = salario / horas_trabajadas

print (F'Su nombre y apellido es {nombre}, su salario es {salario}, sus horas: {horas_trabajadas} y su ingreso horario es de {ingreso_horario}.')


lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9 , 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

#a Calcular el promedio de ingresos/hora del 20% que más gana
"""
yo arranque asi profe
ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]
maximo_1 = ingresos[0]
for numero in ingresos:
    if numero > maximo_1:
        maximo_1 = numero
maximo_2 = ingresos[0]
for numero in ingresos:
    if numero == maximo_1:
        continue
    if numero > maximo_2:
        maximo_2 = numero
"""





#bCalcular el promedio de ingresos/hora de todos los respondentes.
suma_ingresos = 0
for ingreso in lista_ingresos:
    suma_ingresos += ingreso

# Calculamos el promedio
promedio_ingresos = suma_ingresos / len(lista_ingresos)

# Mostramos el resultado
print("El promedio de ingresos por hora de todos los respondentes es:", promedio_ingresos)