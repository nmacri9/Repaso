from os import system
system("cls")
"""
Se necesita saber:
1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
cuya edad esté entre 25 y 50 años inclusive.
2. Nombreyvotodelencuestado degéneroMasculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados
"""



respuesta="si"
contador_dunkin_ikea=0
flag_menos_votados=True
contador_f=0
contador_o=0
contador_m=0
contador_gral=0
acumulador_f_Edad=0
nombre_menos_votado=""


while respuesta=="si":
    nombre=input("Ingrese su nombre: ")

    edad= int(input("Ingrese su edad: "))
    while edad < 18:
        print("Edad invalida")
        edad= int(input("reingrese su edad: "))

    empleado= input("Esta empleado (si/no): ")
    while empleado !="si" and empleado !="no":
        print("respuesta invalida")
        empleado= input("Esta empleado (si/no): ")

    genero= input("Ingrese su genero: ")
    while genero !="m" and genero !="f" and genero !="o":
        print("Genero invalido")
        genero= input("reingrese su genero: ")

    voto= input("Ingrese su voto en mayuscula (APPLE, DUNKIN, IKEA): ")
    while voto !="APPLE" and voto !="DUNKIN" and voto !="IKEA": 
        print("voto ingresado invalido")
        voto= input("reingrese su voto en mayuscula (APPLE, DUNKIN, IKEA): ")

    if empleado=="no" and (edad > 24 and edad < 51) and voto=="DUNKIN" or voto=="IKEA" :
            contador_dunkin_ikea+=1


    if genero=="m":
        contador_m+=1
        if flag_menos_votados==True:
            flag_menos_votados=False
            nombre_menos_votado= nombre
            voto_menos_votado= voto
            edad_menos_votado= edad

        elif edad < edad_menos_votado:
            nombre_menos_votado=nombre
            voto_menos_votado=voto
            edad_menos_votado=edad


    elif genero=="f":
        contador_f+=1
        if voto=="IKEA":
            acumulador_f_Edad+=edad



    else:
        contador_o+=1

    contador_gral+=1

    respuesta= input("Desea seguir ingresando datos (si/no): ")


porcentaje_f= contador_f * 100 / contador_gral
porcentaje_m= contador_m * 100 / contador_gral
porcentaje_o= contador_o * 100 / contador_gral

if (nombre_menos_votado == ""):
    print("no se ingresaron hombres")
else:
    print(f"Nombre y voto del encuestado de género Masculino con menor edad: {nombre_menos_votado} || {voto_menos_votado}")

if contador_f !=0:
    promedio_f_ikea= acumulador_f_Edad / contador_f 
    print(f"Promedio de edad de los encuestados de género Femenino que votaron IKEA: {promedio_f_ikea}")
else:
    print("No se ingresaron mujeres")

print(f"Cantidad de encuestados desempleados de 25 a 50 años que votaron por DUNKIN o IKEA: {contador_dunkin_ikea}")

print(f"Porcentaje de votos de m {porcentaje_m} porcentaje f {porcentaje_f} porcentaje otro {porcentaje_o} ")

mas_encuestado="o"
if (contador_f > contador_m and contador_f > contador_o):
    mas_encuestado="f"
elif contador_m > contador_o:
    mas_encuestado="m"
print(f"El genero mas encuestado fue {mas_encuestado}")