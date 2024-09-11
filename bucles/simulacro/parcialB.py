'''

UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
franquicia que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● nombre
● edad(nomenora18)
● estáempleado(si-no)
● género(Masculino- Femenino- Otro)
● voto(APPLE,DUNKIN, IKEA)

Se necesita saber:
1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
edad no supere los 36 años.
2. Nombre y  voto del encuestado de género Femenino con mayor edad.
3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
4. Edad promedio de cada género.
5. Determinar cuál fue el género que tuvo menos encuestados
'''
maximo_edad = 0
contador_edad_masculino = 0
contador_edad_femenino = 0
contador_edad_otro = 0
suma_edades_masc = 0
suma_edades_fem = 0
suma_edades_otro = 0

contador_otro_Dunkin = 0

contador_APPLE = 0
contador_IKEA = 0
contador_DUNKIN = 0

contador_emp_men_36_IKEA = 0
contador_emp_men_36_APPLE = 0

contador_femenino = 0
contador_masculino = 0
contador_otro = 0

bandera_fem_mayor_edad = True
cliente_f_mas_viejo = ""


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

#1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
#edad no supere los 36 años.
    if voto == 'IKEA':
        if edad < 37 and situacion_laboral == 'si':
            contador_emp_men_36_IKEA += 1
        contador_IKEA += 1
    
    elif voto == 'APPLE':
        if edad < 37 and situacion_laboral == 'si':
            contador_emp_men_36_APPLE += 1
        contador_APPLE += 1

    else: 
        contador_DUNKIN += 1

#4 4. Edad promedio de cada género.
    if genero == 'Otro':
        contador_otro += 1
        suma_edades_otro += edad
        contador_edad_otro += 1
        if voto == 'DUNKIN':
            contador_otro_Dunkin += 1
#2. Nombre y  voto del encuestado de género Femenino con mayor edad.
    elif genero == 'Femenino':
        contador_femenino +=1
        if edad > maximo_edad or bandera_fem_mayor_edad == True:
            cliente_f_mas_viejo = nombre
            voto_fem = voto
            edad_fem = edad
            bandera_fem_mayor_edad=False
    else:
        contador_edad_masculino += 1
        suma_edades_masc += edad
        contador_masculino += 1


    respuesta = input('quiere ingresar mas datos ingrese (no): ')
    if respuesta == 'no'or respuesta == 'NO':
    
            break

#11. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
#edad no supere los 36 años.
total_votos_36_AÑOS = contador_emp_men_36_APPLE + contador_emp_men_36_IKEA

#3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
total_Votos = (contador_DUNKIN + contador_APPLE + contador_IKEA)
porcentaje_o_Dunkin = (contador_otro_Dunkin /total_Votos) * 100

#4 promedio cada genero
if contador_edad_masculino != 0:
    promedio_edad_masc = ( suma_edades_masc / contador_edad_masculino )
    print(f'El promedio de edad masculino es de {promedio_edad_masc}')
else: print ('No hay nadie del gen masculino)')

if contador_edad_femenino != 0:
    promedio_edad_fem = ( suma_edades_fem / contador_edad_femenino )
    print(f'El promedio de edad femenino es de {promedio_edad_fem}')
else: print ('No hay nadie del gen femenino')

if contador_edad_otro != 0:
    promedio_edad_otro = ( suma_edades_otro / contador_edad_otro )
    print(f'El promedio de edad otro genero es de {promedio_edad_otro}')
else : print ('No hay nadie del genero otro ')


#5 5. Determinar cuál fue el género que tuvo menos encuestados
if contador_femenino < contador_masculino and contador_femenino < contador_otro:
    genero_menos_votos = 'Femenino'
elif contador_masculino < contador_femenino and contador_masculino < contador_otro:
    genero_menos_votos = 'Masculino'
else: 
    genero_menos_votos = 'Otro'

#2. Nombre y  voto del encuestado de género Femenino con mayor edad
print(f'EL total de menores de 36 que votaron apple o ikea es : {total_votos_36_AÑOS}')

if (cliente_f_mas_viejo == ""):
    print ('no se ingresaron femeninos')
else:
    print(f'El nombre del encuestado femenino mas grande es {cliente_f_mas_viejo} y voto a {voto_fem}')
print(f'El porcentaje de encuestados de otro genero que votaron DUNKIN es: {porcentaje_o_Dunkin:.2f}%')
print(f'El genero que menos votos tuvo es {genero_menos_votos}')
