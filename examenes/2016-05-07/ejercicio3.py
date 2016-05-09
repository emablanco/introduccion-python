# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:24:42 2016
3) Realice un programa que permita calcular el monto acumulado luego de hacer un depósito a plazo fijo. El programa permite ingresar una cantidad de pesos, una tasa de interés anual y un número de meses. El programa debe mostrar por pantalla en cuanto se habrá convertido el capital inicial transcurridos ese período de tiempo (expresado en meses). Tenga en cuenta que la unidad de medida no es años sino meses. Por ejemplo, 
        - Capital inicial: $ 1000
        - Tasa anual (%): 12
        - Período en meses: 3 
        - Capital acumulado: 1030 (1000 iniciales + 30 de intereses)
@author: emiliano
"""

capital_inicial = int(input("Ingrese el capital incial[valor entero]: $"))
tasa = float(input("Ingrese la tasa de interes anual: %"))
n = int(input("Ingrese la cantidad de meses del plazo fijo:"))

interes_anual = capital_inicial*tasa/100
interes_mensual = interes_anual/12
capital_acumulado = capital_inicial + n*interes_mensual

print("Capital acumulado: ", capital_acumulado)

