# Ejercicio 3: Se ingresan por teclado una serie de 5 valores de temperaturas pronosticados para una semana. Se solicita
# que los almacene en una lista y utilice una función que retorne el tipo de alerta a emitir según lo siguiente:
# - Verde: en ningún día de los siguientes cinco consecutivos, sea superada las temperatura de 30 °C.
# - Amarillo: que 1 o 2 de los siguientes cinco días consecutivos, sea superada la temperatura de 30 °C
# - Naranja: se espera que 3 o 4 de los cinco días consecutivos se supere la temperatura de 30 °C
# - Rojo: cuando se espera que en cada uno de los cinco días se supere los 30 °C.

def get_alerta(temp):
    cant_temp30 = 0
    for t in temp:
        if t > 30:
            cant_temp30 += 1
    if cant_temp30 == 0:
        alerta = "verde"
    elif  cant_temp30 == 1 or cant_temp30 == 2:
        alerta = "amarillo"
    elif  cant_temp30 == 3 or cant_temp30 == 4:
        alerta = "naranja"
    elif cant_temp30 == 5:
        alerta = "rojo"
    return alerta

temp = []
for i in range(5):
    temp.append(int(input("Temperatura " + str(i+1) + ": ")))

print("El alerta para la semana es: ", get_alerta(temp))

