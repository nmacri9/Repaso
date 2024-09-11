'''
Medidas:

AB = Diágonal mayor

DC = Diágonal menor

BD y BC = lados menores

AD y AC = lados mayores

El usuario ingresará las medidas  BC, CD y DA.

Detalles de construcción

Debemos tener en cuenta que la estructura del cometa estará dada por un
perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) 
del mismo material para mantener la forma del cometa.

El cometa estará construido con papel de alta resistencia. 
La cola del mismo se construirá con el mismo papel que el cuerpo y 
representará un 10% adicional del necesario para el cuerpo.

Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel 
son necesarios para la construcción en masa de 10 cometas.
Tener en cuenta que los valores de entrada están expresados en Cms.
'''
BC = float(input("Medidas en cm del lado menor del cometa: "))
DA = float(input("Medida en cm del lado mayor del cometa: "))
DC = float(input("Medida en cm de la diagonal menor del cometa: "))

import math


# Convertir de centímetros a metros
BC_M = BC / 100
DC_M = DC / 100
DA_M = DA / 100

# Calcular BC usando el teorema de Pitágoras (DA es la hipotenusa, BC es un cateto)
BC = math.sqrt(DA**2 - BC**2) / 100

# Calcular AC usando el teorema de Pitágoras (DA y DC son los catetos)
DA = math.sqrt(DA**2 + DC**2) / 100

# Longitud total de varillas de plástico
longitud_varillas = (BC_M + DC_M + DA_M + BC + DA) * 2

# Calcular área del cometa
area_cometa = (BC_M * DC_M) / 2

# Calcular cantidad de papel necesaria (incluyendo la cola del 10%)
cantidad_papel = area_cometa * 1.1

# Multiplicar por 10 para obtener el total necesario para 10 cometas
longitud_varillas_total = longitud_varillas * 10
cantidad_papel_total = cantidad_papel * 10


#imprimir resultados
print(f'Para hacer diez cometas necesita {longitud_varillas_total} metros de varillas.')
print(f'{cantidad_papel_total} metros de papel reforzado. ')

