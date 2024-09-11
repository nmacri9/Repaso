'''

En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán
pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan
$800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez)
se aplicará el siguiente descuento:
● Si compra 6 o más lámparas bajo consumo tiene un descuento del 50%.
● Si compra 5 lámparas bajo consumo marca ;ArgentinaLuz; se hace un descuento del 40 % y si
es de otra marca el descuento es del 30%.
● Si compra 4 lámparas bajo consumo marca ;ArgentinaLuz; o “FelipeLamparas” se hace un
descuento del 25 % y si es de otra marca el descuento es del 20%.
● Si compra 3 lámparas bajo consumo marca ;ArgentinaLuz; el descuento es del 15%, si es
“FelipeLamparas” se hace un descuento del 10 % y si es de otra marca(Sica) un 5%.
Por otro lado, si el importe final con descuento suma más de $4000 se obtiene un descuento adicional
de 5%.

'''
lamparas_precio = 800
'en caso que sean 6 lamparas'
cantidad_lamparas = int(input('Cuantas lamparas?: ')) 
marca= input('Que marca llevas?: ')


if cantidad_lamparas >=6 :
    porcentaje = 0.5

elif cantidad_lamparas == 5:
    if marca == 'argentinaluz':
        porcentaje = 0.4
    else: 
        porcentaje = 0.3
    

else:
    porcentaje = 0


if cantidad_lamparas == 4:
    if marca == 'argentinaluz' or 'FelipeLamparas':
        porcentaje = 0.25
    else: 
        porcentaje = 0.2

elif cantidad_lamparas == 3:
    if marca == 'argentinaluz':
        porcentaje = 0.15
    elif marca == 'Felipe Lamparas':
        porcentaje  = 0.1
    elif marca == 'sica':
        porcentaje = 0.05


precio_sin_descuento = cantidad_lamparas * lamparas_precio
descuento = precio_sin_descuento * porcentaje
precio_final = precio_sin_descuento - descuento
descuento_adicional = 0.05
monto_descuento_adicional = descuento * descuento_adicional
total_final = descuento - monto_descuento_adicional

if precio_final > 4000:
    monto_descuento_adicional = descuento * descuento_adicional
    total_final = descuento - monto_descuento_adicional
    print('recibiste un 5% adicional')

else:
    descuento_adicional = 0


print(f""" cantidad de lámparas: {cantidad_lamparas}, 
          total a pagar sin descuento: {precio_sin_descuento},
          el descuento obtenido si corresponde: {descuento}, el
          y el total a pagar con descuento: {precio_final}
          en caso de superar los $4000, será {total_final}.""")



