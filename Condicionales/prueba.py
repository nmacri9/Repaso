
'en caso que sean 6 lamparas'
cantidad_lamparas = int(input('Cuantas lamparas?: ')) 
marca= input('Que marca llevas?: ')
lamparas_precio = 800
total_final = descuento - monto_descuento_adicional


precio_sin_descuento = cantidad_lamparas * lamparas_precio
descuento = precio_sin_descuento * porcentaje
precio_final = precio_sin_descuento - descuento
descuento_adicional = 0.5


if total_final > 4000:
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


