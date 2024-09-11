a = int(input('Cual es tu edad?: '))

if a >= 18:
    resultado = 'es mayor de edad'
elif a < 10: 
    resultado = 'es niño/a'
elif a >= 10 and a < 13:
    resultado = 'es pre-adolescente' 
elif a >= 13 and a<=17:
    resultado = 'es adolescente'
else:('usted no puso un número correcto')

print(a, resultado)