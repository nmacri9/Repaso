#1
par= 0
num = 1

while num <= 10:
    if num %2==0 :
        par += num
    num += +1
print('La suma de estos es: ', par, '.')


#2
contra = input('introduzca la contraseña')

while contra != 'utn750' :
    contra= input('contraseña incorrecta, intentar otra vez.')
print('contraseña aceptada')

#3 
while num < 0 or num > 9: 
    num = int(input('Numero no aceptado. Por favor ingrese otro numero: '))
print('numero', num, 'aceptado')

#4
letra = input("Ingrese una letra: ")

while letra != "U" and letra != "T" and letra != "N":
    letra = input("Letra no aceptada. Ingrese otra letra: ")
print("Letra aceptada")

#5
num1 = float(input("Ingrese 5 numeros: "))
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())

print(num1, "+", num1, "+", num1, "+", num1, "+", num1, "=", (num1+num2+num3+num4+num5))
print("Promedio de los numeros ingresados:", (num1+num2+num3+num4+num5) / 5)



