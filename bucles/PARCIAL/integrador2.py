'''
2. De los jugadores participantes en un torneo de ajedrez, se registra:
● nombre
● la edad (mayor de 10 años)
● la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.
Informar:
a. Nombre del jugador con más partidas ganadas.
b. Nombre y edad del jugador con menos partidas ganadas.
c. El promedio de edades de los jugadores.
d. El total de partidas ganadas.
'''
maximo_partidas_ganadas = 0
minimo_partidas_ganadas = 0
bandera_partida_ganada = True

contador_edades = 0
acumulador_edades = 0

acumulador_partidas_ganadas = 0
nombre_menos_partidas = ""

while True :


    nombre = str(input('ingrese el nombre: '))
    

    edad = int(input('ingrese la edad: '))

    while edad < 11:
        
        edad= int(input('Reingrese la edad: '))


    partidas_ganadas = int(input('Ingresar partidas ganadas: '))
    while partidas_ganadas < 0 :
        partidas_ganadas = int(input('Reingrese la contraseña'))
    
    
    
    #A_mas partidas ganadas
    if partidas_ganadas > maximo_partidas_ganadas or bandera_partida_ganada == True:
        nombre_mas_partidas = nombre
        maximo_partidas_ganadas = partidas_ganadas
        

#B nombre y edad del jugador con menos partidas ganadas
    if partidas_ganadas < maximo_partidas_ganadas or bandera_partida_ganada == True:
        nombre_menos_partidas = nombre
        minimo_partidas_ganadas = partidas_ganadas
        edad_menos_partidas = edad
        bandera_partida_ganada = False

#c Promedio edades
    acumulador_edades += edad
    contador_edades += 1

#D total partidas ganadas
    acumulador_partidas_ganadas += partidas_ganadas


    respuesta = input('quiere ingresar mas datos ingrese (no): ')
    if respuesta == 'no'or respuesta == 'NO':
    
            break

#Cpromedio edades
promedio_edades = acumulador_edades / contador_edades


print(f'El nombre del jugador con más partidas ganadas es {nombre_mas_partidas}')
print(f'El nombre del jugador con menos partidas ganadas es {nombre_menos_partidas} y su edad es {edad_menos_partidas}')
print(f'El promedio de edades es {promedio_edades:.2f}')
print(f'El total de partidas ganadas es {acumulador_partidas_ganadas}')





