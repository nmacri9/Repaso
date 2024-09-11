password = input ('ingrese su clave: ')
contador_intentos = 0

while password != 'utn2024' and contador_intentos < 1:

    password= input('reingrese la contraseña: ')
    
    contador_intentos += 1
    

if password == 'utn2024':
    print( 'contraseña correcta')
else: print('cntraseña incorrecta.')



