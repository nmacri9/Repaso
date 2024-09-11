p1= int(input('ingresar precio 1: '))
print(p1)
p2=int(input('ingresar precio 2: '))
print(p2)
p3=int(input('ingresar precio 3: '))
print(p3)
suma=(p1+p2+p3)
porcentaje= 21
incremento = (suma*porcentaje) / 100
precio_final=(suma+incremento)
print('el precio final es de:', precio_final, '.')
