sueldo= float(input('Cual es su sueldo?: '))
civil = input('Cual es su estado civil?: ')
hijos= (input('Tiene hijos?: '))

if sueldo <= 2200000 and civil == 'casado' and hijos == 'si':
    print('Usted no pagara impuesto a las ganancias.')
elif sueldo < 2200000:
    print('usted no pagara el impuesto')
else: print('Usted pagara el impuesto')

