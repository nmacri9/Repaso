
from import math ceil

#A
toneladas = float(input('Toneladas a transportar: '))
toneladaskg = toneladas * 1000
capacidad_camion= 3500

cantidad_camiones = ( toneladaskg / capacidad_camion) 
cantidad_camiones= int(cantidad_camiones)

if toneladaskg % capacidad_camion != 0:
    cantidad_camiones += 1

print(f'Se utilizaran {cantidad_camiones} camiones')

