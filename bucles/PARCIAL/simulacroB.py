"""
Se necesita saber:
1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
cuya edad esté entre 25 y 50 años inclusive.
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados
"""
contador_Dunkin = 0
contador_IKEA = 0
contador_APPLE = 0

contador_masc = 0
contador_fem = 0
contador_otro = 0

acumulador_ikea_fem = 0
contador_dunkin_ikea = 0

bandera_menor_edad  = True
nombre_menor = ""

genero_mas_votos = 0

while True :


    nombre = str(input('ingrese el nombre: '))
    

    edad = int(input('ingrese la edad ( no menor a 18 ): '))

    while edad < 18:
        
        edad= int(input('Reingrese la edad (no menor a 18 ): '))

    situacion_laboral = input('Esta empleado? (si-no): ')

    while situacion_laboral != 'si' and situacion_laboral != 'no':
        situacion_laboral = input ('De nuevo, esta empleado? (si-no): ')

    genero = input('Ingrese su genero (Masculino- Femenino- Otro): ')

    while genero != 'Masculino' and genero != 'Femenino' and genero != 'Otro':

        genero = input('Reingrese su genero:')

    voto = input( 'Cual es su voto? (APPLE,DUNKIN, IKEA): ')

    while voto != 'APPLE' and voto != 'DUNKIN' and voto != 'IKEA':

        voto = input('Reingrese su voto:')

#1 Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
# cuya edad esté entre 25 y 50 años inclusive.
    if situacion_laboral == "no" and (edad > 24 and edad < 51) and voto== "DUNKIN" or voto== "IKEA" :
            contador_dunkin_ikea+=1

#3. Porcentaje de votos de cada género.
    if genero  == 'Masculino':
        contador_masc += 1
#2 Nombre y voto del encuestado de género Masculino con menor edad.
        if bandera_menor_edad == True:
            bandera_menor_edad = False
            nombre_menor = nombre
            voto_menor = voto
            menor_edad = edad
        elif edad < menor_edad:
            nombre_menor = nombre
            voto_menor = voto
            menor_edad = edad

    elif genero == 'Femenino':
        contador_fem += 1
        if genero == 'IKEA':
            acumulador_ikea_fem += edad

    else: 
        contador_otro += 1

    respuesta = input('quiere ingresar mas datos ingrese (no): ')
    if respuesta == 'no'or respuesta == 'NO':
    
            break

#1
print(F'La Cantidad de encuestados desempleados de dunkin o ikea entre 25 y 50 años es {contador_dunkin_ikea}')

#2
if nombre_menor == "":
    print ('No se ingresaron hombres')
else: 
    print(f'Nombre y voto del encuestado de genero masculino con menor edad {nombre_menor} / {voto_menor}')

#3 
total_votos = (contador_masc + contador_fem + contador_otro)
porcentaje_fem= contador_fem / total_votos * 100
porcentaje_masc= contador_masc / total_votos * 100
porcentaje_otro= contador_otro / total_votos * 100

print(f'El porcentaje de Masc es {porcentaje_masc}%, el de fem es {porcentaje_fem}%, el de otro es {porcentaje_otro}%')


if contador_fem != 0:
    promedio_fem_ikea = acumulador_ikea_fem / contador_fem
    print (f'El promedio de edad es {promedio_fem_ikea}')
else: 
    print('No se ingresaron mujeres')

#5 5. Determinar cuál fue el género que tuvo menos encuestados
    if contador_fem > contador_masc and contador_fem > contador_otro:
        genero_mas_votos = 'Femenino'
    elif contador_masc > contador_fem and contador_masc > contador_otro:
        genero_mas_votos = 'Masculino'
    else: 
        genero_mas_votos = 'Otro'

print(f'El genero que mas encuestados tuvo fue {genero_mas_votos}')