#7 
""" 
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
= 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1- (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
"""

def calcular_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    resultado_exportaciones = valor_exportaciones* (1- (retenciones / 100))
    return resultado_nacional , resultado_exportaciones
#No cumplia con los objetivos/pasos de una funcion, por ej, calculO y no calculAR

final = calcular_impuestos(500 , 400)
print (final)