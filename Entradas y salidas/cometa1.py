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

lado_menor = input("Medida en CM del lado menor del cometa: ")
lado_mayor = input("Medida en CM del lado mayor del cometa: ")
diagonal_menor = input("Medida en CM del diagonal menor del cometa: ")

lado_menor = float(lado_menor)
lado_mayor = float(lado_mayor)
diagonal_menor = float(diagonal_menor)

diagonal_mayor_uno = ((lado_mayor ** 2) - ((diagonal_menor / 2) ** 2)) ** 0.5
diagonal_mayor_dos = ((lado_menor ** 2) - ((diagonal_menor / 2) ** 2)) ** 0.5
diagonal_mayor = diagonal_mayor_uno + diagonal_mayor_dos

varillas = float((lado_menor * 2 + lado_mayor * 2 + diagonal_mayor + diagonal_menor) / 100)
superficie_cometa = (diagonal_mayor_uno * (diagonal_menor / 2)) + (diagonal_mayor_dos * (diagonal_menor / 2))
superficie_cola = superficie_cometa * 0.1
total_papel = float((superficie_cometa + superficie_cola) / 10000)

varillas_diez = varillas * 10
total_papel_diez = total_papel * 10

print(f"Se necesitan {varillas_diez:.2f} Mts de varillas para la estructura y\n{total_papel_diez:.2f} Mts2 de Papel para construir 10 cometas.")
