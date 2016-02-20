# Ejercicio 1). Realice un programa que permita ingresar por teclado las calificaciones y nombres
# de un curso hasta que se ingrese un valor negativo. Muestre un mensaje en pantalla que
# indique el promedio del curso y el alumno con la mejor calificación.

cant = 0
prom = 0

nota_mayor = 0
nom_mayor = ""

nota = float(input("Ingrese nota: "))
while (nota > 0):
    nombre = input("Ingrese nombre: ")
    cant += 1
    prom += nota
    # mayor calificacion
    if (nota > nota_mayor):
        nom_mayor = nombre
        nota_mayor = nota
    nota = float(input("Ingrese nota: "))

prom = prom/cant
print("Promedio: ", prom)
print("Alumno con mejor nota: ", nom_mayor)