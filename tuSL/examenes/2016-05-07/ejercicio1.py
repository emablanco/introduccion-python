# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:13:13 2016
1) En un archivo de texto se tiene información sobre los pasajeros del titanic. Por cada línea del archivo se encuentran separado por comas los siguientes 5 datos:
Nombre y apellido, edad, género (M/F), tipo de pasaje (1 , 2 o 3),  sobrevivió (0 o 1) y un campo mas de control.

Se le solicita que lea este archivo e informe en pantalla lo siguiente:
- Cantidad de sobrevivientes
- Porcentaje de sobrevivientes de cada género
- Cantidad de menores que sobrevivieron
@author: emiliano
"""

titanic = open("titanic.txt")

vivieronMas = 0
vivieronFem = 0
vivieronMen = 0

for p in titanic:
    nomyape, edad, genero, pasaje, vivio, x = p.split(",")
    # ojo, al leer
    if vivio == "1":
        if genero == "F":
            vivieronFem += 1
        else:
            vivieronMas += 1
        if int(edad) < 18:
            vivieronMen += 1
          
total = vivieronFem + vivieronMas
porcentajeFem = 100*vivieronFem/total
porcentajeMas = 100-porcentajeFem

print("Cantidad de sobrevivientes: ", total)
print("Porcentaje de mujeres: ", porcentajeFem)
print("Porcentaje de varones: ", porcentajeMas)
print("Cantidad de menores: ", vivieronMen)
