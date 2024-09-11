acumular_numero= 0
contador = 0
suma_positivos = 0
producto_negativos = 1
contador_negativos= 0



while True :
    numero = int(input('ingrese un numero: '))
    print(numero)
#Suma de numeros positivos
    if numero > 0:
        suma_positivos += numero
#Producto de numeros negativos
    elif numero < 0:
        producto_negativos *= numero
        contador_negativos =+1
    respuesta = input('quiere ingresar mas numeros ingrese (no): ')

    if respuesta == 'no'or respuesta == 'NO':
        break

if contador_negativos == 0:
    producto_negativos = 0

#Suma de numeros positivos
print(f'la suma total de los num positivos es {suma_positivos}')
#Producto de numeros negativos
print(f'El producto de los negativos es: {producto_negativos}')