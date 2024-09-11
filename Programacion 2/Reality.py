nombre1 = input('nombre del primer jugador: ')
nombre2 = input('Nombre segundo jugador: ')
nombre3 = input('nombre tercer jugador: ')
print('/////')
edad1= int(input('Edad primer jugador'))
while edad1 < 25: 
    edad1 = int(input('ingresar la edad nuevamente'))
edad2= int(input('edad segundo jugador: '))
while edad2< 25:
    edad2 = int(input('ingresar edad nuevamente: '))
edad3= int(input('ingresar edad del tercer jugador'))
while edad3< 25:
    edad3 = int(input('ingresar edad nuevamente'))
promedio = (edad1 + edad2 + edad3) / 3

print('/////')
votos_primer_jugador= int(input('Votos del primer jugador'))
while votos_primer_jugador< 0:
    votos_primer_jugador= int(input('Ingresar votos nuevamente'))

votos_segundo_jugador= int(input('Votos del segundo jugador'))
while votos_segundo_jugador < 0:
    votos_segundo_jugador= int(input('Ingresar votos nuevamente'))

votos_tercer_jugador= int(input('Votos del tercer jugador'))
while votos_tercer_jugador < 0:
    votos_tercer_jugador= int(input('Ingresar votos nuevamente'))

suma_votos = votos_primer_jugador + votos_segundo_jugador + votos_tercer_jugador

print('////')

#A
if votos_primer_jugador > (votos_segundo_jugador and votos_tercer_jugador):
    print('El jugador con mas votos es: ', nombre1 )

elif votos_segundo_jugador > (votos_primer_jugador and votos_tercer_jugador):
    print('El jugador con mas votos es: ', nombre2 )

elif votos_tercer_jugador > (votos_primer_jugador and votos_segundo_jugador):
    print('El jugador con mas votos es: ', nombre3)
 #B
if votos_primer_jugador < (votos_segundo_jugador and votos_tercer_jugador):
    print('El jugador con menos votos es: ', nombre1, 'de', edad1, 'años')

elif votos_segundo_jugador < (votos_primer_jugador and votos_tercer_jugador):
    print('El jugador con menos votos es; ', nombre2, 'de', edad2, 'años')

elif votos_tercer_jugador < (votos_primer_jugador and votos_segundo_jugador):
    print('El jugador con menos votos es: ', nombre3, 'de',edad3, 'años')

print('//////')
print('El promedio de edades es: ', promedio)

print('El total de votos emitidos fue de: ', suma_votos )







