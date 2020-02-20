import random

archi = open("miarchivito.txt", 'w')
valores = list(range(20,101))
for i in range(1000):
    valor = random.choice(valores)
    archi.write(valor)
    archi.write("\n")
archi.close()



