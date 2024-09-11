'''
Ingresar 10 números enteros. Determinar el máximo y el mínimo.
contador = x veces se va a poner x cosa
while= no se sabe cuantas veces se va a poner x cosa

bandera =  como los buzones de eeuu, 
bandera_del_primer_numero = True

if numero > maximo or bandera_del_primer numero = True
if numero < minimo or bandera_del_primer_numero = False (cambia el valor al final y para que no repita la bandera otra vez)
'''

contador = 0
maximo = 0
minimo = 0


while contador < 10:
    
    numero = int(input('Colocar un numero entero: ')) 
    print(numero)

    if numero > maximo or contador == 0: 
        maximo = numero
    
    if numero < minimo or contador == 0:
            minimo = numero

    contador +=1
    

print(f'el minimo es {minimo} y el maximo es {maximo}')


