#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:37:51 2017

@author: emiliano
"""

import random
from datetime import datetime

archi = open("queloscumplas.txt", 'w')

inicio = datetime(1981, 3, 28)
final =  datetime(2017, 10, 7)

for i in range(1000):
    archi.write(str(inicio + (final - inicio) * random.random()).split(".")[0])
    archi.write("\n")
archi.close()
