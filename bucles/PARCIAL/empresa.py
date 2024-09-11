"""Una empresa internacional está realizando un estudio de mercado para decidir cuál será la nueva plataforma de entretenimiento que se lanzará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Hulu, Vix+ o CODA.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:

Nombre
Edad (no menor a 18)
Tiene suscripción a algún servicio de streaming (sí-no)
Género (Masculino - Femenino - No binario - Otro)
Voto (Hulu, Vix+, CODA)
Se solicita realizar las siguientes búsquedas:

1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu. 
2. Nombre, género y edad del encuestado de menor edad que votó por Hulu. 
3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA. 
4. Determinar el promedio de edad de los encuestados que votaron por Vix+. 
5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos. 
"""

contador_masculino_hulu = 0

contador_hulu = 0
contador_vix = 0
contador_coda = 0

minimo_edad_hulu = 0
bandera_edad_Hulu = True

contador_mayores_25_coda = 0

contador_promedio_edad_vix = 0
acumulador_promedio_edad_vix = 0


while True:

    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad (debe ser mayor de 18 años): "))
    while edad < 18:
        edad = int(input("Error. Debe ser mayor de 18 años, reingrese su edad: "))

    suscripcion_streaming = input("Tiene alguna suscripción activa a algún servicio de streaming?: ")
    while suscripcion_streaming != "si" and suscripcion_streaming != "no":
        suscripcion_streaming = input("Error. Debe indicar si posee o no una suscripción activa. Reingrese su respuesta nuevamente: ")

    genero = input("Ingrese su género (masculino, femenino, no binario, otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "no binario" and genero != "otro":
        genero (input("Error. Debe ingresar una de las opciones mencionadas, reingrese su género nuevamente: "))
    
    voto = input("Ingrese su voto (Hulu, Vix+ o CODA): ")
    while voto != "Hulu" and voto != "Vix+" and voto != "CODA":
        voto = input("Error. Debe ingresar una de las opciones mencionadas, reingrese su voto nuevamente por favor: ")


    # 2) Nombre, género y edad del encuestado de menor edad que votó por Hulu.
    if voto == "Hulu":
        if edad < minimo_edad_hulu or bandera_edad_Hulu == True:
            nombre_hulu = nombre
            genero_hulu = genero
            minimo_edad_hulu = edad
            bandera_edad_hulu = False
        contador_hulu = contador_hulu + 1
        # 1) Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu.
        if genero == "masculino" and ((edad >= 18 and edad <= 25) or (edad >=36 and edad <= 49 and voto == "Hulu")):
            contador_masculino_hulu = contador_masculino_hulu + 1


    elif voto == "Vix+":
        # 4) Determinar el promedio de edad de los encuestados que votaron por Vix+.
        if voto == "Vix+":
            contador_promedio_edad_vix = contador_promedio_edad_vix + 1
            acumulador_promedio_edad_vix = acumulador_promedio_edad_vix + edad
        contador_vix = contador_vix + 1


    else:
        # 3) Porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
        if edad > 25:
            contador_mayores_25_coda = contador_mayores_25_coda + 1
        contador_coda = contador_coda + 1 



    respuesta = input("Desea ingresar a otro encuestado?: ")
    if respuesta == "No" or respuesta == "no":
        break


# 3) Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
total_votos = contador_hulu + contador_vix + contador_coda
porcentaje_mayores_25_coda = (contador_mayores_25_coda / total_votos) * 100

# 4) Determinar el promedio de edad de los encuestados que votaron por Vix+.
promedio_edad_vix = acumulador_promedio_edad_vix / contador_promedio_edad_vix

# 5) Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.
if contador_hulu > contador_vix and contador_hulu > contador_coda:
    ganador_votos = "Hulu"
elif contador_vix > contador_coda:
    ganador_votos = "Vix+"
else:
    ganador_votos = "CODA"


print(f"""
1) Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu: {contador_masculino_hulu}
2) Nombre, género y edad del encuestado de menor edad que votó por Hulu: {nombre_hulu}, {genero_hulu}, de {minimo_edad_hulu} años
3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA: {porcentaje_mayores_25_coda}%
4. Determinar el promedio de edad de los encuestados que votaron por Vix+: {promedio_edad_vix} años
5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos. 
Votos para Hulu: {contador_hulu}
Votos para Vix+: {contador_vix}
Votos para CODA: {contador_coda}
La franquicia con más votos es: {ganador_votos}
""")