'''

una concesionaria nos pide un programa que nos permita cargar los datos de sus ventas:
las ventas son indeterminadas.

nombre del cliente:
edad(debe ser mayor)
marca del vehiculo (renault,fiat,bmw)
cantidad de puertas (2,4)
apellido del vendedor (Zapata,Quiroz,Simino)

se necesita saber:

A-Cantidad de vehiculos de 2 puertas que sean de la marca renault
B-nombre del cliente mas joven
C-porcentaje cada marca de auto sobre el total
D-promedio de edades de los clientes que compraron 4 puertas
E-nombre del cliente mas viejo que compro fiat
F-total de autos vendidos de la marca BMW
G_ Apellido del vendedor que menos vendió

'''
contador_renault_2_puertas = 0

contador_bmw = 0
contador_fiat = 0
contador_renault = 0

promedio_edad_4_puertas = 0
contador_edades = 0
suma_edades = 0

minimo_edad = 0
maximo_edad = 0
bandera_nombre_mas_joven = True
bandera_nombre_cliente_mas_viejo = True

contador_Zapata = 0
contador_Quiroz = 0
contador_Simino = 0

vendedor_menos_vendio = 0

while True :


    nombre = str(input('ingrese el nombre: '))
    

    edad = int(input('ingrese la edad: '))

    while edad < 18:
        
        edad=int(input('Reingrese la edad: '))

    marca = input('ingrese la marca del vehiculo (renault,fiat,bmw): ')

    while marca != 'renault' and marca != 'fiat' and marca != 'bmw':

        marca = input('Reingrese la marca del vehiculo: ')

    puertas = int(input('ingrese la cantidad de puertas (2 o 4): '))

    while puertas != 2 and puertas != 4:
        puertas = int(input('Reingrese la cantidad de puertas (2 o 4): '))

    apellido_vendedor = input('ingrese el apellido del vendedor (Zapata,Quiroz,Simino): ')

    while apellido_vendedor != 'Zapata' and apellido_vendedor != 'Quiroz' and apellido_vendedor != 'Simino':

        apellido_vendedor = input('Reingrese el apellido del vendedor (Zapata,Quiroz,Simino): ')

#C porcentaje cantidad marca sobre el total
    if marca == 'renault':
        contador_renault += 1
        #A cantidad de renault 2 puertas
        if puertas == 2:
            contador_renault_2_puertas += 1
    #C Porcentaje cada marca sobre el total
    elif marca == 'bmw':
        contador_bmw += 1
    else:
        #E nombre cliente de fiat mas viejo
        if edad < maximo_edad or bandera_nombre_cliente_mas_viejo == True:
            cliente_mas_viejo = nombre
            maximo_edad = edad
            contador_fiat += 1

#B Nombre cliente mas joven
    if edad < minimo_edad or bandera_nombre_mas_joven == True:
        mas_joven = nombre
        minimo_edad = edad

        bandera_nombre_mas_joven = False

#D Promedio edad de los clientes 
    if puertas == 4:
        suma_edades = edad
        contador_edades += 1

# Vendedor que menos vendió
    if apellido_vendedor == 'Quiroz':
        contador_Quiroz += 1
    elif apellido_vendedor == 'Zapata':
        contador_Zapata += 1
    else :
        contador_Simino += 1


    respuesta = input('quiere ingresar mas datos ingrese (no): ')
    if respuesta == 'no'or respuesta == 'NO':
    
            break


#C como sacar porcentaje?
total_ventas = (contador_renault + contador_bmw + contador_fiat)

porcentaje_renault = (contador_renault / total_ventas) * 100
porcentaje_fiat = (contador_fiat / total_ventas) * 100 
porcentaje_bmw = (contador_bmw / total_ventas) * 100 
#D Como sacar promedio de edades? 
promedio_edad_4_puertas = suma_edades / contador_edades

#Vendedor que menos vendio

if contador_Simino < contador_Zapata and contador_Simino < contador_Quiroz:
    vendedor_menos_vendio = 'Simino'
elif contador_Quiroz  < contador_Zapata and contador_Quiroz< contador_Simino:
    vendedor_menos_vendio = 'Quiroz'
else: 
    vendedor_menos_vendio = 'Zapata'





print(f'La cantidad de renault 2 puertas es {contador_renault_2_puertas}')
print(f'El nombre del cliente mas joven es {mas_joven}')
print(f'El porcentaje sobre las ventas de bmw es {porcentaje_bmw:.2f}%') 
print(f' El porcentaje de fiat es {porcentaje_fiat:.2f}% ')
print(f' El porcentaje de renault es {porcentaje_renault:.2f}%.')
print(f'El promedio de edad de los clientes que compraron 4 puertas es de {promedio_edad_4_puertas}.')
print(f'El nombre del cliente mas viejo de fiat es {cliente_mas_viejo}')
print(f'El total de autos vendidos por bmw es {contador_bmw}')