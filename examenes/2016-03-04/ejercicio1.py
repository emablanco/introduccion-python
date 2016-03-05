# Ejercicio 1: Un hospital estudia la inflamación de los pacientes que han sido sometidos
# a un nuevo tratamieto para la artritis y necesitan analizar los resultados obtenidos.
# Los datos son almacenados en un archivo donde cada renglón contiene información de un
# único paciente, las columnas representan los días sucesivos y los valores numéricos
# representan el nivel de inflamación. Una muestra de las primeras filas del archivo se
# observan a continuación:
#
# 0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
# 0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
# 0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
# 0,0,2,0,4,2,2,1,6,7,10,7,9,13,8,8,15,10,10,7,17,4,4,7,6,15,6,4,9,11,3,5,6,3,3,4,2,3,2,1
# 0,1,1,3,3,1,3,5,2,4,4,7,6,5,3,10,8,10,6,17,9,14,9,7,13,9,12,6,7,7,9,6,3,2,2,4,2,0,1,1
#
# Se solicita que realice un programa que lea el contenido del archivo tratamiento.txt y
# muestre por pantalla la inflamación promedio y máxima de cada paciente.

pacientes = open('tratamiento.txt').readlines()

for p in pacientes:
    plista = p.split(',')
    suma = 0
    cant = 0
    maxima = -1
    for val in plista:
        suma += int(val)
        cant +=1
        if int(val) > maxima:
            maxima = int(val)
    promedio = suma/cant
    print("Inflamación promedio: ", promedio)
    print("Inflamación maxima: ", maxima)
    print()
