edad= int(input('ingresar edad: '))
nacion = str(input('donde nacio?: '))

if edad >= 16 and nacion == 'argentina':
    print( 'ud puede votar')
elif edad >=18 and nacion != 'Argentina': 
    print('Usted puede votar')
else: print('ud no puede votar')