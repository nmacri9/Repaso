"""
Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden
atender 15 mascotas), para esto hay que considerar los siguientes datos y
encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:
● Edad(Validar entre 1 y 20 años)
● Tipo: (Validar “gato”, “perro”, “hámster”)
● Peso:(Másde0kg)
● Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
● Vacuna antirrábica (validar “si”, ”no”)
TemaB
1.Cantidad de perros o gatos, sin vacuna antirrábica, que pesan entre 10 y 20 kg,
2. El tipo de mascota másingresada con parásitos.
3. Edad y diagnóstico de la mascota más joven que se presentaron con una
infección.
4. Porcentaje de mascotas de cada tipo.
5. Promedio de pesos de mascotas con parásitos

"""
minimo_edad = 0
bandera_mascota_joven = 0
diagnostico_mascota_joven = ""

cantidad_mascota_parasito = 0
contador_parasitos = 0
peso_total_parasitos = 0
contador_gato = 0
contador_perro = 0
contador_hamster = 0

contador_mascotas = 0
contador_gatos_y_perros = 0

contador_parasitos_gato = 0
contador_parasitos_perro = 0
contador_parasitos_hamster = 0

while contador_mascotas < 15: 

    edad = int(input('Edad entre 1 y 20 años: '))

    while edad < 1 or edad > 20:
        edad= int(input('Edad invalida (entre 1 y 20 años)'))

    tipo = input('Ingrese su tipo (“gato”, “perro”, “hámster”): ')

    while tipo != 'gato' and tipo != 'perro' and tipo != 'hamster':

        tipo = input('Reingrese su tipo:')

    peso = float(input('Ingresar su peso (mayor de 0kg): '))
    while peso < 1:
        peso = float(input('Reingresar peso nuevamente'))

    diagnostico = input('Ingrese su diagnostico (“problemas digestivos”, “parásitos”, “infección”): ')

    while diagnostico != 'problemas digestivos' and diagnostico != 'parasitos' and diagnostico != 'infeccion':

        diagnostico = input('Reingrese su diagnostico:')

    vacuna = input('Tiene vacuna antirrabica? (si-no)')
    while vacuna != 'si' and vacuna != 'no':
        vacuna = input('Tiene vacuna? (si-no)')

    contador_mascotas = contador_mascotas + 1

#1.Cantidad de perros o gatos, sin vacuna antirrábica, que pesan entre 10 y 20 kg.

    if vacuna == 'no' and (tipo == 'perro' or tipo == 'gato') and (peso > 10 and peso < 20):
        contador_gatos_y_perros += 1

#3. Edad y diagnóstico de la mascota más joven que se presentaron con una infección.
    if diagnostico == 'infeccion':
        if edad < minimo_edad or bandera_mascota_joven == True:
            diagnostico_mascota_joven = diagnostico
            edad_mascota_joven = edad
            bandera_menor_Edad = False
#2 El tipo de mascota más ingresada con parásitos.
    elif diagnostico == 'parasitos':
        if tipo == 'gato':
            contador_parasitos_gato += 1
        elif tipo == 'perro':
            contador_parasitos_perro += 1
        else:
            contador_parasitos_hamster += 1
        contador_parasitos += 1


#4. Porcentaje de mascotas de cada tipo.
if tipo == 'perro':
        contador_perro += 1
elif tipo == 'gato':
        contador_gato += 1
else:
        contador_hamster += 1

#1
if contador_gatos_y_perros != 0:
    print (F'1_ La cantidad de perros y gatos sin vacuna y mayor a 10kg es {contador_gatos_y_perros}')
else: 
    print('No se ingresaron perros y gatos sin vacuna y mayor a 10kg')
#2
if contador_parasitos_hamster > contador_parasitos_gato and contador_parasitos_hamster > contador_parasitos_perro:
    tipo_con_mas_parasitos = 'hamster'
elif contador_parasitos_gato > contador_parasitos_hamster and contador_parasitos_gato > contador_parasitos_perro:
    tipo_con_mas_parasitos = 'gato'
else:
    tipo_con_mas_parasitos = 'perro'

    print(f'2_El tipo de mascota con mas parasitos es {tipo_con_mas_parasitos}')
#3
if (diagnostico_mascota_joven) == "":
    print('No se ingresaron mascotas con infeccion.')
else:
    print(f'3_ Edad y diagnóstico de la mascota más joven que se presentaron con una infección. {diagnostico_mascota_joven} / {edad_mascota_joven}')

#4
total_votos  = ( contador_gato + contador_perro + contador_hamster )

porcentaje_perro = ( contador_perro / total_votos ) * 100
porcentaje_gato = ( contador_gato / total_votos ) * 100
porcentaje_hamster = ( contador_hamster / total_votos ) * 100

print(f'4_El porcentaje de P es {porcentaje_perro}%, de G es {porcentaje_gato}% y de H es {porcentaje_hamster}')

#5. Promedio de pesos de mascotas con parásitos
if contador_parasitos != 0:
    promedio_pesos_parasitos = peso_total_parasitos / contador_parasitos 
    print(f'5_El promedio de pesos de mascotas con parasitos es {promedio_pesos_parasitos}')
else:
    print('5_No se ingresaron mascotas con parasitos.')