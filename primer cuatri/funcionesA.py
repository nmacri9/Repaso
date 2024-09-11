#1_Crear una función que muestre por pantalla el número que recibe como parámetro.
def mostrar_numero(numero):
    print(f"El número es: {numero}")

mostrar_numero (5)

# 2- Crear una función que permita determinar si un número es par o no.
def verificar (numero):
    #determinar si un número es par o no.
    if (numero) % 2 == 0:
        print ("True")
    else: 
        print('False')
verificar (11)

#3 Especializarpara que valide el número en un rango determinado
# pasado por parámetro “desde”-“hasta”.
def mostrar_numero(numero):
    if numero > 10 and numero < 60:
        print(f"El número entre 10 y 60 es: {numero}")
    else: 
        print('El numero ingresado no corresponde')
mostrar_numero (30)

#4 Realizar un programa en donde se puedan utilizar los prototipos de
# la función Restar en sus 4 combinaciones.
#A
def restar (numero_a: int , numero_b: int = 4) -> int:
    #resta en  restar1(int, int)->int
    resultado = int(numero_a - numero_b)

    return resultado
diferencia = restar (10)
#B
def restar (numero_a , numero_b = 4) -> int:
    #resta en  restar1(int, int)->int
    resultado = int(numero_a - numero_b)

    return resultado
diferencia = restar (12)
#C
def restar (numero_a: int , numero_b: int = 4):
    #resta en  restar1(int, int)->int
    resultado = int(numero_a - numero_b)

    return resultado
diferencia = restar (13)
#D
def restar (numero_a, numero_b = 4):
    #resta en  restar1(int, int)->int
    resultado = int(numero_a - numero_b)

    return resultado
diferencia = restar (10)

#5 
def descontar(numero):
    descuento = numero * 0.05
    return numero - descuento

numero1 = int(input("Ingrese un número entre 10 y 100: "))
if numero1 >= 10 and numero1 <= 100:
    numero_con_descuento = descontar(numero1)

print(f'El numero con 5% de descuento es {numero_con_descuento}')

#6 
def realizarOperacion (numero1 , numero2):
    if operacion == 's':
        return numero1 + numero2
    elif operacion == 'r':
        return numero1 - numero2
    else:
        return None

numero1 = int(input("Ingrese un número entre 10 y 100: "))
numero2 = int(input("Ingrese un número entre 10 y 100: "))

if numero1 and numero2 >= 10 and numero1 and numero2 <= 100:
    operacion = str(input('Ingresar operacion deseada (s o r): '))
else:
    print('Error, elegir un numero entre 10 y 100: ')

resultado = realizarOperacion(numero1, numero2)
if operacion == 's':
            print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif operacion == 'r':
            print(f"La resta de {numero1} y {numero2} es: {resultado}")
else:
        print("Operación inválida. Debe ingresar 's' para sumar o 'r' para restar.")