# Ejercicio 2)- Almacene en una *lista* el nombre y apellido de N personas que
# son ingresados por teclado. Inicialmente se solicita la cantidad de personas
# a ser ingresadas y posteriormente los nombres y apellidos separados
# con coma (por ej: Marcos Daniel, Bertolino Iruretagoyena).

# Luego, el programa debe mostrar por pantalla de lo siguiente:
# a- la lista original,
# b- ordenada alfabeticamente,
# c- en sentido inverso,
# d- en mayúsculas el apellido.
#
# Para la impresión de a, b y c debe implementar una función llamada *imprimir* que reciba la lista
# y la muestre en pantalla de a una persona por renglón.

def imprimir(lista):
    for persona in lista:
        print(persona)
    print()

n = int(input("Cantidad de personas: "))
lista = []

for i in range(n):
    nom_ape = input("Ingrese nombre y apellido: ")
    lista.append(nom_ape)

print("Original")
print("--------------")
imprimir(lista)

print("Ordenada")
print("--------------")
lista.sort()
imprimir(lista)

print("Inversa")
print("--------------")
lista.reverse()
imprimir(lista)

print("Mayuscula apellido")
print("--------------")

for i in lista:
    nom, ape = i.split(",")
    print(nom,ape.upper())
