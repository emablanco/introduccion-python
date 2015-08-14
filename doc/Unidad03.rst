
Estructuras de datos y control de flujo
=======================================

Si un programa no fuera más que una lista de órdenes a ejecutar de forma
secuencial, una por una, no tendría mucha utilidad. Es por ello que en
la mayoría de los lenguajes de programación existen lo que se denominan
estructuras de control. Estas estructuras permiten que, ante
determinadas condiciones, un programa se comporte de diferentes maneras.

Supongamos por ejemplo que queremos hacer un programa que nos pregunte
ciertas cosas, y en base a esto determine si nos conviene ir al trabajo
en bicicleta o en auto. Este programa prodría considerar inicialmente la
temperatura ambiente, la hora y la distancia. Estos indicadores
(variables), determinarán si el programa se debe comportar de una forma
u de otra para de este modo recomendarnos una cosa (el uso de la
bicicleta) u otra (el auto).

Estructuras condicionales
-------------------------

La primer estructura de control que veremos son los condicionales, los
cuales nos permiten comprobar condiciones y hacer que ejecute un
fragmento de código u otro, dependiendo de esta condición. Aquí es donde
cobra su importancia el tipo booleano que aprendimos en la sección
anterior sobre los tipos básicos.

Sentencia if
~~~~~~~~~~~~

La forma más simple de un estamento condicional es un ***if*** (del
inglés si) seguido de la condición a evaluar, dos puntos (:) y en la
siguiente línea e indentado, el código a ejecutar en caso de que se
cumpla dicha condición. Por ejemplo, si consideramos lo anterior, y
hacemos que el programa por ahora solo considere la temperatura,
podríamos hacer lo siguiente:

.. code:: python

    if (temperatura >= 10) and (temperatura < 30):
        print('Deberías ser amable con el medio ambiente e ir en bicicleta')

Esta sentencia se lee como: si (if) temperatura es menor o igual a 10, y
temperatura es menor a 30, entonces ejecutar: print('Deberías ser amable
con el medio ambiente e ir en bicicleta'). Estas sentencias solo se
ejecutarán si se cumple la condición de que la variable temperatura
contenga un valor que este entre 10 y 29, para el caso donde temperatura
sea menor a 10 o mayor a 29, el programa no hará nada.

Una cuestión muy importante es asegurarnos de que el código esta
indentado tal cual se ha hecho en el ejemplo, es decir, aseguraros de
pulsar Tabulación en la línea que esta debajo de los 2 puntos (:), dado
que esta es la forma de Python de saber que nuestra intención es que las
sentencias que están indentadas, se ejecute sólo en el caso de que se
cumpla la condición.

Sentencia if..else
~~~~~~~~~~~~~~~~~~

Nuestro interés inicial era que el programa nos dijera si podemos ir en
auto o en bicicleta, y el ejemplo anterior solo nos dice algo cuando
podemos ir en bici, pero no dice o hace nada cuando la condición no se
cumple. Para estos casos existe un condicional llamado \ ***else***\ 
(del inglés si no), que se usa conjuntamente con if y que sirve para
ejecutar ciertas instrucciones en caso de que la condición de la
sentencia if no se cumpla. Por ejemplo:

.. code:: python

    if (temperatura >= 10) and (temperatura < 30):
        print('Deberías ser amable con el medio ambiente e ir en bicicleta')
    else:
        print('La temperatura no es agradable, te recomiendo ir en auto.')

Esto se lee como *si temperatura es mayor o igual a 10 y temperatura es
menor que 30, entonces mostrar el mensaje 'Deberías ser amable con el
medio ambiente e ir en bicicleta', sino mostrar el mensaje 'La
temperatura no es agradable, te recomiendo ir en auto.'*. Siempre se
ejecutará una opción u otra, dependiendo del valor de la variable
temperatura. Por lo que en este punto podemos decir que el código se
bifurca en dos caminos diferentes dependiendo de una condición (que en
este caso es el valor de la variable temperatura).

En este caso también tenemos que prestar atención a la indentación
utilizada. La sentencia *else* se escribe al mismo nivel que la
sentencia *if*, y las sentencias que se deben ejecutar en caso de no se
cumpla la condición if, deben ir indentadas también.

Una versión más completa del programa podría ser la siguiente:

.. code:: python

    temperatura = input('Ingrese la temperatura en ºC:')
    
    if (temperatura >= 10) and (temperatura < 30):
        print('Deberías ser amable con el medio ambiente e ir en bicicleta')
    else:
        print('La temperatura no es agradable, le recomiendo ir en auto')
        
    print('Que tenga buen día!')


.. parsed-literal::

    Ingrese la temperatura en ºC:21


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-286b3e307026> in <module>()
          1 temperatura = input('Ingrese la temperatura en ºC:')
          2 
    ----> 3 if (temperatura >= 10) and (temperatura < 30):
          4     print('Deberías ser amable con el medio ambiente e ir en bicicleta')
          5 else:


    TypeError: unorderable types: str() >= int()


En este caso consultamos por la temperatura, pidiendole al usuario que
la ingrese por teclado (para esto utilizamos la función *input* que
vimos en la Unidad 1). Luego mostramos en patalla lo que corresponda
según el valor ingresado, y por último mostramos el mensaje 'Que tenga
buen día!'. Es importante mencionar que la última sentencia siempre se
ejecutará, la bifurcación se produce solamente entre las sentencias que
estan dentro del if y el else, lo restante se seguirá ejecutando de
manera secuencial.

Estructuras anidadas
~~~~~~~~~~~~~~~~~~~~

Supongamos ahora que también queremos considerar la distancia que se
debe recorrer. En este caso deberíamos preguntar por la distancia, pero
también por la temperatura. Para que en los casos donde la temperatura
sea agradable, la distancia no sea demasiado larga como para ir en
bicicleta.

Para estos casos, se pueden utilizar estructuras anidadas, es decir, en
el bloque de código que se ejecutará en caso de cumplirse o no una
determina condición, podemos poner una nueva estructura de control, por
ejemplo un nuevo *if*.

Reescribamos el código anterior para que considere esta nueva condición,
y veamos como usar estructuras anidadas:

.. code:: python

    temperatura = input('Ingrese la temperatura en ºC:')
    distancia = input('Ingrese la distancia a recorrer en km:')
    
    if (temperatura >= 10) and (temperatura < 30):
        if (distancia <= 15):
            print('Deberías ser amable con el medio ambiente e ir en bicicleta')
        else:
            print('El clima es agradable, pero la distancia es muy larga. Le recomiendo ir en auto')
            
    else:
        print('La temperatura no es agradable, le recomiendo ir en auto.')
        
    print('Que tenga buen día!')

En este caso si se cumple la condición de que la variable temperatura
contiene un valor entre 10 y 29, se pasa a considerar el valor de la
variable distancia; si esta es menor o igual a 15, se muestra el mensaje
*'Deberías ser amable con el medio ambiente e ir en bicicleta'*, en caso
contrario, se muestra el mensaje *'El clima es agradable, pero la
distancia es muy larga. Le recomiendo ir en auto'*. Por otro lado, si el
valor de la variable temperatura no esta entre 10 y 29, se seguirá
mostrando el mensaje *'La temperatura no es agradable, le recomiendo ir
en auto'*. Lo mismo sucede con la última sentencia, la cual mostrará el
mensaje *'Que tenga buen día!'* independientemente del valor de las
variables *temperatura* y *distancia*

Estructuras repetitivas
-----------------------

Estructura repetitiva *while*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estructura repetitiva *for*
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estructura de datos *listas* y *diccionarios*
---------------------------------------------

Listas
~~~~~~

Diccionarios
~~~~~~~~~~~~

Manipulando textos con strings
------------------------------
