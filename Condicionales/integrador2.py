cantidad_lamparas = int(input("ingrese la cantidad de lamparas: "))
marca = input("ingrese marca: ")
precio_lampara = 800




if cantidad_lamparas >= 6 :
    porcentaje = 0.5
    
elif cantidad_lamparas == 5:

    if marca == "argentinaluz":
        porcentaje = 0.4
    else:
        porcentaje = 0.3
    
else:
    porcentaje = 0

precio_sin_descuento = cantidad_lamparas * precio_lampara
descuento = precio_sin_descuento * porcentaje
precio_final = precio_sin_descuento - descuento

print(f""" cantidad de lámparas: {cantidad_lamparas}, 
          total a pagar sin descuento: {precio_sin_descuento},
          el descuento obtenido si corresponde: {descuento}, el
          y el total a pagar con descuento: {precio_final}.""")