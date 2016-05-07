# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:15:16 2016
2)  Programe una función que reciba como argumento una palabra y retorne otra cadena encriptada. Para encriptarla debe reemplazar una letra con un número según lo siguiente: a->4, b->8, e->3, f->7, t->2, g->9, i->1, o->0. Realice un programa que haga uso de esta función.
@author: emiliano
"""

def encripta(mensaje):
    e = ""
    for letra in mensaje:
        #a->4, b->8, e->3, f->7, t->2, g->9, i->1, o->0
        if letra == 'a':
            e += '4'
        elif letra == 'b':
            e += '8'
        elif letra == 'e':
            e += '3'
        elif letra == 'f':
            e += '7'
        elif letra == 't':
            e += '2'
        elif letra == 'g':
            e += '9'
        elif letra == 'i':
            e += '1'
        elif letra == 'o':
            e += '0'
        else:
            e += letra
    return e

sms = "emiliano"
enc = encripta(sms)
print(enc)