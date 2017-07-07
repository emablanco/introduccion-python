# -*- coding: utf-8 -*-
"""
@author: emiliano
Juego el ahorcado: el usuario ingresa letras para adivinar una palabra secreta
  - gana: cuando adivina la palabra
  - pierde: cuando supera la cantidad de intentos
  - muestra: guiones bajos en las letras que faltan, letras acertadas en su lugar
"""
MAX_INTENTOS = 10
intentos = 0
secreta = "tupac"
lacertadas = []

while True:
    letra_nueva = input("Ingrese letra: ")
    intentos = intentos + 1
    
    if letra_nueva in secreta:
        lacertadas.append(letra_nueva)

    palabra_formada = ""
    for letra in secreta:
        if letra in lacertadas:
            palabra_formada = palabra_formada + letra
        else:
            palabra_formada = palabra_formada + "_ "
    print(palabra_formada)
    
    if palabra_formada == secreta:
        gano = True
        break
    
    if intentos == MAX_INTENTOS:
        gano = False
        break
if gano:
    print("Ganaste!!")
else:
    print("Perdiste!!")    