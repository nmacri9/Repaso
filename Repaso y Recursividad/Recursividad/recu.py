def calcular_potencia (base: int = 2 , exponente : int = 2):
    if exponente == 0:
        return 1    
    else:
        return (base * exponente) 

resultado = calcular_potencia()
resultado2 = calcular_potencia(3)
resultado3 = calcular_potencia(4,5)
print(f'La potencia del numero es: {resultado}.')
print(f'La potencia del numero es: {resultado2}.')
print(f'La potencia del numero es: {resultado3}.')
