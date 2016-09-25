# Ejercicio 2: Realice un programa que permita ingresar los datos de alumnos de una facultad. Por cada alumno se
# ingresa: nombre, apellido, genero, edad, carrera. El ingreso de dato finaliza cuando se ingresa la edad -1. Se solicita
# que informe: a) La cantidad mujeres se inscribieron en la carrera de informática y su promedio de edad. b) La
# cantidad de hombres de entre 17 y 20 años de edad inscriptos en química.

suma = 0
cant_feme = 0
cant_mascu = 0
edad = int(input("Edad: "))
while edad != -1:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    genero = input("Genero: ")
    carrera = input("Carrera: ")
    if genero == "femenino" and carrera =="informatica":
        suma_edad += edad
        cant_feme += 1
    if genero == "masculino" and carrera =="quimica" and (17 < edad < 20):
        cant_mascu += 1
    edad = int(input("Edad: "))

if cant_feme > 0:
    print("Cantidad de mujeres en informatica: ", cant_feme)
    print("Promedio de edades: ", suma_edad/cant_feme)

print("Cantidad de hombres en quimica entre 17 y 20: ", cant_mascu)