'''
1. Permitir que el usuario ingrese todos los números que desee.
Determinar:
a. La suma acumulada de los números negativos.
b. La suma acumulada de los números positivos.
c. La cantidad de números negativos ingresados.
d. El promedio de los números positivos.
e. el positivo mas grande
f. El porcentaje de números negativos ingresados, 
respecto del total de ingresos.

'''
acumulador_negativos= 0
acumulador_positivos= 0
contador_negativos = 0
promedio = 0
contador_negativos = 0
contador_positivos = 0
contador = 0
maximo = 0

while numero >10000 or numero < -10000 or numero != 0 :
        while True :
                numero = int(input('ingrese un numero: '))
                print(numero)
        
#Suma de numeros positivos
                if numero > 0 :
                        acumulador_positivos = acumulador_positivos + numero
                        contador_positivos = contador_positivos + 1
                        print (contador_positivos)

#d: Promedio num positivos

                if numero > maximo or contador == 0: 
                        maximo = numero
#aum de numeros negativos
        
                elif numero < 0:
                        acumulador_negativos= acumulador_negativos + numero
                        contador_negativos = contador_negativos + 1
                        print (contador_negativos)
                respuesta = input('quiere ingresar mas numeros ingrese (no): ')


                if respuesta == 'no'or respuesta == 'NO':
                        break



promedio = acumulador_positivos / contador_positivos
numeros_ingresados= contador_negativos + contador_positivos
porcentaje = (numeros_ingresados / contador_negativos) / 100
#a_suma de num negativos
print(f'La suma de numeros negativos es {acumulador_negativos}')
#b_suma de num positivos
print(f'la suma de numeros positivos es {acumulador_positivos}')
#c_La cantidad de numeros negativos ingresados
print(f'La cantidad de los numeros negativos es {contador_negativos}')
#d_ Promedio numeros positivos
print(f'El promedio de numeros positivos es: {promedio}')
#f_ porcentaje numeros negativos
print(f'El porcentaje de numeros negativos es: {porcentaje}')