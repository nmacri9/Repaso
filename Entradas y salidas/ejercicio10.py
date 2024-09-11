importe= float(input('ingresar su sueldo: '))
descuento= float(input('ingrese su descuento: '))

aumento= (importe * descuento) / 100
nuevo_importe = importe - aumento
print(f'tu nuevo importe es {nuevo_importe}')
#entregado