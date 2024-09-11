'''
Solicitarle al usuario el ingreso de un color primario. Validar que el mismo sea Rojo, Verde o Azul.
'''

mensaje = 'ingrese un color primario (Rojo,Verde o Azul): '

color = input ( mensaje )

while color != 'Rojo' and color != 'Azul' and color != 'Verde':

    mensaje = input('Incorrecto, ingrese un color primario:')


