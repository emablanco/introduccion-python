# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:31:53 2016

@author: emiliano
"""

from PIL import Image
img = Image.open('madres.jpg')
ancho, alto = img.size 
for y in range(alto):
  for x in range(ancho):
    pixel = img.getpixel((x, y))
    print(x, ',', y, ':', pixel)
  print()