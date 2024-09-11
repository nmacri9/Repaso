





contador = 0
suma = 0


while contador < 5:
    
    numero = int(input('ingrese un numero: '))
    
    suma = suma + numero
    contador = contador + 1
promedio = suma / 5
promedio_dos = suma / contador

print(f'la suma de los numeros es: {suma}')
print(f'el promedio de los numeros es: {promedio}')
print(f'el promedio de los numeros es: {promedio_dos}')

