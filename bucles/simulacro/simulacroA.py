"""
para la bandera definir la primer variable con ""
Se necesita saber:
1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
cuya edad esté entre 25 y 50 años inclusive.
2. Nombreyvotodelencuestado degéneroMasculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados
"""
contador_DUNKIN_IKEA = 0

acumulador_femenino_ikea = 0
contador_femenino= 0
contador_masculino = 0
contador_otro = 0

minimo_edad = 0
bandera_menor_Edad = True
nombre_menor = ""

while True :


    nombre = str(input('ingrese el nombre: '))
    

    edad = int(input('ingrese la edad ( no menor a 18 ): '))

    while edad < 18:
        
        edad= int(input('Reingrese la edad (no menor a 18 ): '))

    situacion_laboral = input('Esta empleado? (si-no)')

    while situacion_laboral != 'si' and situacion_laboral != 'no':
        situacion_laboral = input ('De nuevo, esta empleado? (si-no)')

    genero = input('Ingrese su genero (Masculino- Femenino- Otro): ')

    while genero != 'Masculino' and genero != 'Femenino' and genero != 'Otro':

        genero = input('Reingrese su genero:')

    voto = input( 'Cual es su voto? (APPLE,DUNKIN, IKEA): ')

    while voto != 'APPLE' and voto != 'DUNKIN' and voto != 'IKEA':

        voto = input('Reingrese su voto:')

#1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
# cuya edad esté entre 25 y 50 años inclusive.
    if situacion_laboral == 'no' and (edad > 24 and edad < 51) and (voto == 'DUNKIN' or voto == 'IKEA'):
        contador_DUNKIN_IKEA += 1

#2. Nombreyvotodelencuestado degéneroMasculino con menor edad.
    if genero == 'Masculino':
        contador_masculino += 1
        if edad < minimo_edad or bandera_menor_Edad == True:
            nombre_menor = nombre
            edad_menor = edad
            voto_menor = voto
            bandera_menor_Edad = False

    elif genero == 'Femenino':
        contador_femenino += 1
#4. Promedio de edad de los encuestados de género Femenino que votaron IKEA.
        if voto == 'IKEA':
            acumulador_femenino_ikea += edad
    else: 
        contador_otro += 1


    respuesta = input('quiere ingresar mas datos ingrese (no): ')
    if respuesta == 'no'or respuesta == 'NO':

            break


print(F'1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,cuya edad esté entre 25 y 50 años inclusive es {contador_DUNKIN_IKEA}')

#2 #2. Nombreyvotodelencuestado degéneroMasculino con menor edad.
if nombre_menor == "":
    print ('No se ingresaron hombres.')
else:
    print(f' Nombre y voto del encuestado de género Masculino con menor edad.')

#3 3. Porcentaje de votos de cada género.
total_votos  = ( contador_femenino + contador_masculino + contador_otro )

porcentaje_masc = ( contador_masculino / total_votos ) * 100
porcentaje_fem = ( contador_femenino / total_votos ) * 100
porcentaje_otro = ( contador_otro / total_votos ) * 100

print(f'El porcentaje M es {porcentaje_masc}%, el porcentaje F es {porcentaje_fem}%, y el porcentaje O es {porcentaje_otro}%.')

#4 4. Promedio de edad de los encuestados de género Femenino que votaron IKEA.
if contador_femenino != 0:
    promedio_f_ikea = acumulador_femenino_ikea/ contador_femenino 
    print(f'El promedio de mujeres que voto IKEA es {promedio_f_ikea}')
else: 
    ('No se ingresaron mujeres.')

#5. Determinar cuál fue el género que tuvo más encuestados
if contador_femenino > contador_masculino and contador_femenino > contador_otro:
    genero_mas_votado = 'Femenino'
elif contador_masculino > contador_femenino and contador_masculino > contador_otro:
    genero_mas_votado = 'Masculino'
else:
    genero_mas_votado = 'Otro'
print(f'El genero mas votado es {genero_mas_votado}')
