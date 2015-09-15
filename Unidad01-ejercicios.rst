
Unidad 1: Ejercicios
--------------------

1- Realice un programa que permita al usuario ingresar una temperatura
en grados centígrados y que muestre su equivalente en grados fahrenheit.

::

    Ingrese temperatura en °C: 33.8
    Conversión a Fahrenheit: 92.84

2- Realice un programa que permita al usuario ingresar su nombre y que
luego lo muestre repetido en pantalla tantas vees como cantidad de
letras posea el nombre.

3- Ingrese el nombre y edad de dos personas en variables separadas
(nom1, edad1, nom2, edad2). Luego, intercambie la edad y muestre el
resultado en pantalla. Indague de qué manera puede intercambiar el
contenido de variables en Python.

4- La simple tarea de realizar la cocción de un huevo pasado por agua
tiene sus secretos. Con la ecuación a continuación se puede conocer el
tiempo en alcanzar el punto exacto. Programe la ecuación para valores de
bla bla bla

5- Lea por teclado el valor del cuenta kilómetros de un automovil,
posteriormente, permita ingresar el nuevo valor luego de realizar un
viaje y muestre en pantalla los kilómetros recorridos, así como también
ese valor en metros, centímetros, yardas y pies.

6- Las benévolas companías telefónicas cobran la tarifa de cada llamada
del siguiente modo: un valor fijo de $0.80 cuando se establece la
llamada, luego, fracciona por tiempo, donde el primer minuto tiene un
valor de $1.30 y los subsiguientes de $1.45. Realice un programa que
permita ingresar la duración de una llamada y que muestre luego el costo
total de la misma, a la que se le debe agregar un porcentaje del 20%
correspondiente a impuestos.

7- Un atleta realiza sus entrenamientos para una maratón (42.195km) y
desea conocer su velocidad promedio. Desarrolle un programa donde se
ingrese el tiempo transcurrido en tres variables diferentes: horas,
minutos y segundos. Luego, muestre la velocidad promedio en km/h y
km/seg.

8- En el siguiente programa se calcula la diferencia de tiempo entre dos
marcas de tiempo. Analice el código del programa y explique las acciones
que se llevan a cabo. Luego, modifiquelo para que las dos marcas de
tiempo sean ingresadas por un usuario.

.. code:: python

    # dos marcas de tiempo
    hora1,min1,seg1 = 14, 58,59 
    hora2,min2,seg2 = 16, 0, 0
    
    # conversión del tiempo a segundos
    t1s = hora1*60*60 + min1*60 + seg1
    t2s = hora2*60*60 + min2*60 + seg2
    
    # diferencia
    t = abs(t1s-t2s)
    
    # cálculos de hora, minuto y segundos
    h = t//3600
    m = (t-h*3600)//60
    s = t-h*3600-m*60
    
    # impresión en pantalla
    print ('Diferencia de tiempo:', h, 'hs', m, 'min',s, 'seg')
