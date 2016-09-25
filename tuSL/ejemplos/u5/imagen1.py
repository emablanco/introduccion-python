# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:48:16 2016

@author: emiliano
"""

from PIL import Image             # de PIL importa el objeto Image
img = Image.open("hornocal.jpg")  # Método open
ancho, alto = img.size            # Atributos:
print("Ancho: ", ancho)
print("Alto: ", alto)
print("Cantidad de píxeles: ", ancho*alto)