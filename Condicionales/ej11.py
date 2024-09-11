#11 y 12


import random
aleatorio = random.randint(1,10)
if aleatorio >= 6:
    print('Promocion directa, la nota es: ', aleatorio)
elif aleatorio >=5 and aleatorio <=4:
    print('Aprobado la nota es: ', aleatorio)
elif aleatorio <=3:
    print('Desaprobado la nota es: ', aleatorio)



print ('//////')

#contador/ variable (no confundir con nombres en variables)
contador = 0   #variable de control

while contador < 10: #por primera vez tiene que ser verdadero
    
    print(contador + 1)
    #variable += 1
    contador = contador + 1 # que en algun momento sea falsa

contador = 10

while contador > 1 :
    
    print(contador - 1)
    #variable += 1
    contador = contador - 1