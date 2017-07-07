# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:34:15 2017

@author: emiliano
 
Descripcion: el apostador debe elegir 6 números al azar los que van 
    del 00 al 45. Se extraen seis bolillas para el Sorteo Tradicional Primer
    sorteo y se controla si hubo aciertos. 
    El valor del juego es de $4, $5,50 o $ 7.
    Que es mejor:
    - cambiar los números cada día?
    - siempre apostar a los mismos números?
    - jugar a los que menos salieron?
"""
import random

cant_jugadores = 1000000
porcentaje_reparte = 50
valor = 5.50
pozo = cant_jugadores * valor * porcentaje_reparte/100.0

gano = False
dia = 1
mi_jugada = sorted(random.sample(range(46),6))

while not gano:    
    bolillas = sorted(random.sample(range(46),6))
    if mi_jugada == bolillas:
        print("Gano el día", dia, "con los números:", mi_jugada)
        gano = True
    dia += 1

gaste = dia*valor
gane = pozo
print("Años jugando: $", dia/365)
print("Gasté: $", gaste)
print("Gané: $", gane)
print("PN =", gane-gaste)
            
