# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 01:16:04 2016

@author: emiliano
"""
from PIL import Image
img = Image.open('madres.jpg')
ancho, alto = img.size
for y in range(alto):
    for x in range(ancho):
        valor = img.getpixel((x, y))
        img.putpixel((x, y), valor + 100)
img.save('mas_brillo.png')
img.show()