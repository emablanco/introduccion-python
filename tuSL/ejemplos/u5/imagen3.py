# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:48:16 2016

@author: emiliano
"""


from PIL import Image

img = Image.open('hornocal.jpg')
rojo, verde, azul = img.split()
ancho, alto = rojo.size 

for y in range(alto):
    for x in range(ancho):
        valor = rojo.getpixel((x, y))
        rojo.putpixel((x, y), valor + 100)
rojiza = Image.merge('RGB', (rojo, verde, azul))
rojiza.save("rojo_realzado.png")