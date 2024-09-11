#1
a = int(input('Cuantos años tenes? : '))

if a == 18: 
    print('Usted tiene 18 años ')

#2
a = int(input('Cuantos años tenes? : '))

if a >= 18:
    print('MAYOR')
else:
    print('MENOR')

#3

a = float(input('Cuanto mide el basquetbolista?: '))

if a >= 1.80:
    print('Puede ser pivot')
else:
    print('No puede ser pivot')

#4

a = int(input('Cual es tu edad?: '))
 
if a >= 13:
    resultado = 'adolescente'

elif a < 17:
    resultado = 'mayor de edad'
else: 
    resultado = 'No es adolescente'

print(a,'es', resultado)

#5
a = int(input('Cual es tu edad?: '))

if a >= 18:
    resultado = 'es mayor de edad'
elif a < 10: 
    resultado = 'es niño/a'
elif a >= 10 and a<=13:
    resultado = 'es pre-adolescente' 
elif a >= 13 and a<=17:
    resultado = 'es adolescente'
else:('usted no puso un número correcto')

print(a, resultado)
