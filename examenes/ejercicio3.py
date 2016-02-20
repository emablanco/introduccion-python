# Ejercicio 3)- Un archivo de texto temp.txt contiene información sobre temperaturas
# expresadas en grados centigrados o fareheit, indicado la unidad en un segundo campo
# con la letra C o F respectivamente, por ejemplo:

#40.3 C
#50 F
#43 F
#20 C

# Realice un programa que genere dos nuevos archivos llamado tempC.txt y tempF.txt donde se
# almacene la temperatura en la unidad correspondiente, para el ejemplo previo el archivo resultante sería:
#
# tempC.txt     tempC.txt
# =========     =========
# 40.3 C         104.54 F
# 10 C           50 F
# 6.11 C         43 F
# 20 C           68 F

#Las ecuaciones de conversión son F = (9/5)*C + 32; C = (F - 32)*(5/9)

forig = open("temp.txt")
tempC = open("tempC.txt", 'w')
tempF = open("tempF.txt", 'w')

for i in forig.readlines():
    val, uni = i.split(" ")
    if "C" in uni:
        C = float(val)
        valF = str((9/5)*C + 32)

        tempC.write(val + " C" + "\n")
        tempF.write(valF + " F" + "\n")
    else:
        F = float(val)
        valC = str((F - 32)*(5/9))

        tempC.write(valC + " C" + "\n")
        tempF.write(val + " F" + "\n")

forig.close()
tempC.close()
tempF.close()
