
acumular_numero= 0
contador = 0

while True :
    numero = int(input('ingrese un numero: '))
    print(numero)

    acumular_numero = acumular_numero + numero

    contador += 1

    respuesta = input('quiere ingresar mas numeros ingrese (no): ')

    if respuesta == 'no'or respuesta == 'NO':
        break


promedio = acumular_numero / contador
print(f'la suma total es {acumular_numero}')
print(f'el promedio es {promedio}')