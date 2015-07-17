
Tipos básicos
=============

Como vimos en la Unidad 1, las variables pueden contener diferentes
tipos de datos, y al ser distintos, son tratados de manera diferente por
Python (por ejemplo no podemos sumar un número con una letra).

Hemos visto 2 de los 3 tipos básicos que utiliza python, los cuales se
dividen en: \* **Números** \* **Cadenas de texto** \* **Booleanos**

Números
-------

Los números como vimos pueden ser enteros, reales (también denominados
de coma flotante) ó complejos. ### Enteros Los números enteros son
aquellos números positivos o negativos que no tienen decimales (además
del cero). En Python se pueden representar mediante el tipo int (de
integer, entero) o el tipo long (largo). La única diferencia es que el
tipo long permite almacenar números más grandes. Por ejemplo:

.. code:: python

    a = 4
    type(a)




.. parsed-literal::

    int



.. code:: python

    b = 28L
    type(b)




.. parsed-literal::

    long



Reales
~~~~~~

Los números reales son los que tienen decimales. En Python se expresan
mediante el tipo float.

Para representar un número real en Python se escribe primero la parte
entera, seguido de un punto y por último la parte decimal. Por ejemplo:

.. code:: python

    real = 6.2231

También se puede utilizar notación científica, y añadir una e (de
exponente) para indicar un exponente en base 10. Por ejemplo:

.. code:: python

    real = 0.6e-3


Lo que sería equivalente a 0.6 x 10-3 = 0.6 x 0.001 = 0.0006

.. code:: python

    real = 8.21
    type(real)




.. parsed-literal::

    float



Complejos
~~~~~~~~~

Los números complejos son aquellos que tienen parte imaginaria. Si no
conocías de su existencia, es más que probable que nunca lo vayas a
necesitar, de hecho la mayor parte de los lenguajes de programación
carecen de este tipo, aunque sea muy utilizado por ingenieros y
científicos en general.

En el caso de que necesites utilizar números complejos, debes saber que
son llamados complex en Python, y que se representan de la siguiente
forma:

.. code:: python

    c= 4 + 5j
    type(c)




.. parsed-literal::

    complex



Cadenas de texto
----------------

Tal como hemos visto en la unidad anterior, las cadenas (string en
inglés ó str) no son más que texto encerrado entre comillas simples
(‘cadena’), dobles (“cadena”) ó triples('''Cadenas multilíneas'''). Por
ejemplo:

.. code:: python

    a = 'El futuro mostrará los resultados y juzgará a cada uno de acuerdo a sus logros (Nikola Tesla)'
    type(a)




.. parsed-literal::

    str



.. code:: python

    b = "En realidad no me preocupa que quieran robar mis ideas, me preocupa que ellos no las tengan (Nikola Tesla)"
    type(b)




.. parsed-literal::

    str



.. code:: python

    c = '''Un instrumento de poco costo y no más grande que un reloj, permitirá a su portador escuchar en 
    cualquier parte, ya sea en el mar o en la tierra, música, canciones o un discurso de un líder político, 
    dictado en cualquier otro sitio distante. Del mismo modo, cualquier dibujo o impresión podrá ser 
    transferida de un lugar a otro (Nikola Tesla, ~ año 1891).
    '''
    type(c)




.. parsed-literal::

    str



Booleanos
---------

Por último, nos queda el tipo básico booleano. Una variable de tipo
booleano sólo puede tener dos valores: True (cierto) y False (falso).
Estos valores son especialmente importantes para las expresiones
condicionales y los bucles, como veremos más adelante. Pero veamos
algunos ejemplos:

.. code:: python

    a = True
    type(a)




.. parsed-literal::

    bool



.. code:: python

    b = False
    type(b)




.. parsed-literal::

    bool



.. code:: python

    c = 10 > 2
    print c


.. parsed-literal::

    True


En este último ejemplo vemos algo particular, hemos asignado a la
variable **c** el resultado de una expresión lógica (10 > 2). Python en
este caso opera con la misma y asigna a la variable **c** el resultado
de dicha operación, la cual en este caso es verdadera (True), dado que
10 es mayor que 2. Al tratarse se una operación lógica, el resultado
siempre será de tipo booleando (bool), es decir, será verdadero o será
falso.

.. code:: python

    type(c)




.. parsed-literal::

    bool



Operadores relacionales
~~~~~~~~~~~~~~~~~~~~~~~

Como vimos en el ejemplo anterior, los valores booleanos son además el
resultado de expresiones que utilizan operadores relacionales
(comparaciones entre valores).

Estos operadores, siempre se utilizan de la siguiente manera:

operando\_A (operador) operando\_B

Por ejemplo:

.. code:: python

    10 > 4




.. parsed-literal::

    True



En este caso el operando A es 10 y el B es 4, el resultado de aplicar el
operador ">" a los operandos A y B en este caso es True (cierto) dado
qeu 10 es mayor que 4.

La lista completa de operadores que podemos utilizar en python es:

+------------+-------------------------+-----------+-------------+
| Operador   | Descripción             | Ejemplo   | Resultado   |
+============+=========================+===========+=============+
| ==         | ¿son iguales a y b?     | 5 == 3    | False       |
+------------+-------------------------+-----------+-------------+
| !=         | ¿son distintos a y b?   | 5 != 3    | True        |
+------------+-------------------------+-----------+-------------+
| <          | ¿es a menor que b?      | 5 < 3     | False       |
+------------+-------------------------+-----------+-------------+
| >          | ¿es a mayor que b?      | 5 > 3     | True        |
+------------+-------------------------+-----------+-------------+

Veamos otro ejemplo, ahora con cadenas de texto:

.. code:: python

    d = "Una cosa" == "Otra cosa"
    print d


.. parsed-literal::

    False


En este caso el operador == se utiliza para comparar si son iguales los
operandos. Esta comparación se hace caracter a caracter, por lo que al
ser diferentes las cadenas, el resultado es False. Lo siquiente también
es False

.. code:: python

    d = "Una cosa" == "una cosa"
    print d


.. parsed-literal::

    False


Solo cuando ambas cadenas son iguales, la comparación devuelve verdadero

.. code:: python

    d = "Una cosa" == "Una cosa"
    print d


.. parsed-literal::

    True


El tipo como hemos visto, es booleano:

.. code:: python

    type(d)




.. parsed-literal::

    bool



También podemos comparar números, expresiones algebráicas y expresiones
lógicas.

.. code:: python

    resultado = 24 > 3*7
    print resultado


.. parsed-literal::

    True


.. code:: python

    resultado = False == True
    print resultado


.. parsed-literal::

    False


.. code:: python

    a = 2*8
    b = 3*8
    resultado = (a < b)
    print resultado


.. parsed-literal::

    True


En Python, una expresión que es cierta tiene el valor 1, y una expresión
que es falsa tiene el valor 0.

.. code:: python

    a = True
    resultado = a == 1
    print resultado


.. parsed-literal::

    True


.. code:: python

    b = False
    resultado = b == 0
    print resultado


.. parsed-literal::

    True


Operadores lógicos
~~~~~~~~~~~~~~~~~~

Además de los operadores relacionales, tenemos los operadores lógicos.
Existen 3 tipos de operadores lógicos: ****and (y), or (ó), y not
(no)****. Por ejemplo:

*x > 0 **and** x < 10*

es verdadero sólo si *x* es mayor que 0 ***y*** menor que 10.

*n%2 == 0 **or** n %3 == 0*

es verdadero si cualquiera de las condiciones es verdadera, o sea, si el
número es divisible por 2 o por 3. O sea, podemos leer la línea anterior
como *n divido 2 es igual a 0 ***ó*** n dividido 3 es igual a 0*.

Finalmente, el operador **not** niega una expresión booleana, de forma
que

****not***\ (x > y)* es cierto si *(x > y)* es falso, o sea, si x es
menor o igual que y.

En resumen tenemos los siguientes operadores lógicos

+------------+---------------------+----------------------+-------------+
| Operador   | Descripción         | Ejemplo              | Resultado   |
+============+=====================+======================+=============+
| **and**    | ¿se cumple a y b?   | True **and** False   | False       |
+------------+---------------------+----------------------+-------------+
| **or**     | ¿se cumple a o b?   | True **or** False    | True        |
+------------+---------------------+----------------------+-------------+
| **not**    | No a                | **not** True         | False       |
+------------+---------------------+----------------------+-------------+

Veamos algunos ejemplos

.. code:: python

    a = 9
    b = 16
    c = 6
    resultado = (a < b) and (a > c)
    print resultado


.. parsed-literal::

    True


En este caso, como ambas operaciones devuelven True (verdadero), el
resultado es verdadero.

.. code:: python

    a = 9
    b = 16
    c = 6
    resultado = (a < b) and (a < c)
    print resultado


.. parsed-literal::

    False


Por el contrario, si una de las condiciones devuelve False, el resultado
será False.

Veamos algunos ejemplos con el operador ***or***

.. code:: python

    a = 9
    b = 16
    c = 6
    resultado = (a < b) or (a < c)
    print resultado


.. parsed-literal::

    True


En este caso la primer operación es verdadera y la segunda es falsa,
pero como estamos utilizando el operador ***or***, la variable resultado
tendrá como valor True.

Por último, veamos un ejemplo con el operador ***not***

.. code:: python

    a = 9
    b = 16
    resultado = not(a > b)
    print resultado


.. parsed-literal::

    True


En este ejemplo *a* es menor que *b*, por lo que la expresión es falsa.
Sin embargo al utilizarse el operador ***not*** estamos cambiando el
resultado por su opuesto (en este caso True). La expresión podría leer
como "no es cierto que a es mayor que b", lo cual es una expresión
cierta, y por lo tanto el valor correspondiente es True.

Veamos un ejemplo un poco mas complicado

.. code:: python

    a = 9
    b = 16
    resultado = (not(a > b)) and (not(b < c))
    print resultado


.. parsed-literal::

    True


Desglocemos un poco este ejemplo:

En este caso la expresión (a > b) es falsa, al igual que (b < c), por lo
que podríamos ver a lo anterior como

.. code:: python

    resultado = (not(False)) and (not(False))

Dijimos que el operador ***not*** cambia el resultado de una expresión
booleana por su opuesto, por lo que si seguimos desarrollando esta línea
tenemos:

.. code:: python

    resultado = (True) and (True)

Como ambas expresiones son verdaderas, el valor de la variable
*resultado* será *True*.

Se debe tener un especial cuidado con el orden en que se utilizan los
operadores. Para asegurarnos de que estamos aplicando los operadores a
una expresión particular, siempre es recomendable utilizar paréntesis
para demarcar la expresión sobre la que deseamos operar.

Estructuras de control
======================

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

Condicionales
-------------

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

Repeticiones
------------

while
~~~~~

Ejercicios
----------

1) Modifique el código de la sección "Estructuras anidadas", para que la
   distancia se pregunte solamente en caso de que la temperatura sea
   agradable para ir en bicicleta.

.. code:: python

    for i in range(1,10):
        if i%2==0:
            print(i,"es par")
        else:
            print(i, "es impar")


.. parsed-literal::

    (1, 'es impar')
    (2, 'es par')
    (3, 'es impar')
    (4, 'es par')
    (5, 'es impar')
    (6, 'es par')
    (7, 'es impar')
    (8, 'es par')
    (9, 'es impar')


Referencias utilizadas en esta unidad:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ***Python para todos***, Raúl González Duque,
   http://mundogeek.net/tutorial-python

