1. ¿Cuáles de las siguientes primitivas de control utilizaría para leer repetidamente por tecaldo?

[ ] for
[ ] if
[ ] is

2. Escriba un programa que permita ingresar 5 numeros por teclado y muestre la suma de ellos

3. Marque en el siguiente programa las funciones invocadas que no forman parte de la biblioteca estándar de python

    mensaje = input("Ingrese mensaje")
    mensaje_cifrado = cifrar(mensaje)
    print("El mensaje cifrado es: {}".format(mensaje_cifrado))
    if mensaje == descifrar(mensaje_cifrado):
        print("Mensaje descifrado OK")
    else:
        print("Error al descifrar")
        
4. Si el siguiente fragmento de código se ejecuta sin error, ¿de qué tipo de dato es la variable M?

    print(M + " veces")
   
5. ¿Qué resultado produce la sentencia siguiente?

    num = 4
    print(str(num)*num)

6. Escriba el programa que daría la siguiente salida utilizando un ciclo for:
    
        1
        22
        333
        4444
        55555
        
7. ¿Qué estructura de control utilizaría para bifurcar la ejecución de un programa?

    [ ] secuencial
    [ ] condicional
    [ ] repetitiva
    
8. Marque en el siguiente programa la estructura condicional y repetitiva

    cant = int(input("Ingrese valor: "))
    if cant % 2 == 0:
        cant += 1
    for i in range(cant):
        if i % 2 ==0:
            print(i)
            
9. Programe un ciclo iterativo para mostrar cada una de las siguientes secuencias:

    a. 1, 2, 3, 4, 5
    b. 5, 4, 3, 2, 1
    c. 2, 4, 6, 8, 10

10. Dadas las siguientes secuencias

    a. 5, 10, 15, 20, 25, 30
    b. 1, 5, 10, 15, 25, 30
    c. 0, 5, 10, 15, 20, 33
    
    indique con que fragmento de código se corresponden
    
    for i in range(0,30,5):  | for i in range(1,33, 2):  | i=5
        print(i)             |     print(i)              | while i<=30:
                             |                           |    print(i)
                             |                           |    i += 5

11. Suponga que un programa denominado sonido.py contiene 2 funciones
    denominadas filtrarRuido y agregarRuido.
    Si desde su programa, que se encuentra almacenado en el mismo directorio, 
    quisiera hacer uso de estas funciones, ¿cómo deberían importarse? 
    
12. Programe dos funciones que reciben una lista de números y para el caso de
    filtrarRuido debe restar un valor fijo, y en agregarRuido debe sumarlo, ambas 
    deben retornar la lista modificada.
                                                         
13. El programa almacenado en el archivo ej13.py debe escribir en un archivo mil números
    aleatorios entre el 20 y el 100. Sin embargo, tiene un error por el cual no funciona.
    
    a. Explique qué significa el error que da el programa al ser ejecutado
    b. Modifique el programa de manera tal que funcione correctamente

14. El juego "La Generala" consiste en tirar cinco dados y establecer el puntaje de
    la jugada. De las posibles, la escalera se da cuando suceden algunas de las 
    tres secuencias: 1-2-3-4-5, 2-3-4-5-6 y 3-4-5-6-1. 
    Realice un programa que tire los 5 dados al azar y determine si se produjo 
    una escalera.
