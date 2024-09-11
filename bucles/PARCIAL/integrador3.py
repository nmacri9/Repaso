'''
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar
la carga y validación de datos para luego mostrarlos por pantalla.
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.


'''

contador = 0

while contador < 10:

    apellido = input ('Ingresar apellido, Macri, Gonzalez, Lopez: ')
    print (apellido)
    
    while apellido != 'Macri' and apellido != 'Gonzalez' and apellido != 'Lopez':
        
        apellido =input ('Ingresar apellido nuevamente, Macri, Gonzalez, Lopez: ')
    contador = contador + 1

while contador < 10:
    
    edad = int(input('Colocar su edad: '))
    
    while edad < 18 or edad > 90:
        edad = int(input('Volver a colocar su edad: '))
    
    contador += 1
    print(edad)



while contador < 10: 
    
    estado_civil = input('Cual es su estado civil?: ')

    while estado_civil != 'Soltero' and estado_civil != 'Casado' and estado_civil != 'Divorciado' and estado_civil != 'Viudo':
        estado_civil = input('ingresar su estado civil nuevamente. ') 
    
    contador += 1
    print(estado_civil)


while contador < 10:

    legajo = int(input('ingrese su numero de legajo:  '))

    while legajo < 1000 or  legajo > 9999:
        legajo = input('Reingrese su legajo: ')
    contador += 1 
    print (legajo)

