# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:30:52 2016
4) Programe una función llamada "listaReducida" que reciba una lista como parámetro, y cree una nueva a partir de ella que no incluya el primer y último elemento y luego la retorne. Tenga en cuenta que no se debe modificar la lista original. Ayuda: investigue el método de las listas .copy() 
@author: emiliano
"""

def listaReducida(lista):
    '''opcion 1'''
    redu = lista.copy()
    redu.pop(0)
    redu.pop(-1)
    return redu

def listaReducida2(lista):
    '''opcion 2, mas simple'''
    return lista[1:-1]

edades = [12, 32, 54, 65, 76, 87, 98, 111]
print(edades)
print(listaReducida(edades))
print(listaReducida2(edades))
