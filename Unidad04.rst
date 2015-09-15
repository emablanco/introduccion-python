================================================
Tecnicatura Universitaria en Software Libre
================================================
--------------------------------------
Introducción al Desarrollo de Software
--------------------------------------

:Docente: Emiliano López
:Tutor: Maximiliano Boscovich

.. header:: 
  Introducción al Desarrollo de Software - Unidad 4

.. contents:: Contenidos


.. sectnum::

.. raw:: pdf

   PageBreak oneColumn

.. |date| date::
.. |time| date:: %H:%M

Este documento fue generado el |date| |time|

.. raw:: pdf

   PageBreak oneColumn

Unidad 4: Funciones y archivos
==============================

Funciones
---------

Las funciones son subprogramas que pueden ser invocados para realizar
una tarea específica, siendo capaz de recibir información (datos de
entrada) desde donde son llamados y a su vez de retornar algún valor
(datos de salida).

Cuando una función es invocada, el programa principal transfiere el
control a la función hasta que finalice su ejecución, volviendo luego al
punto desde donde fue llamada.

En los programas desarrollados anteriormente hicimos uso de la función
``len()``, que recibe como información de entrada una secuencia (lista o
una cadena de caracteres por ejemplo) y retorna un valor numérico entero
que representa la cantidad de elementos (o de caracteres). ``len()`` es
una de las tantas funciones prefedinidas por el lenguaje Python en la
biblioteca estándar y, en la presente sección veremos cómo definir
nuestras propias funciones.

El uso de funciones en el desarrollo de programas tiene un conjunto de
ventajas, dentro de las que se destacan:

-  Subdividir un problema complejo en problemas mas simples: divide y
   vencerás.
-  Mejoran la legibilidad del código, los programas modulares son más
   fáciles de mantener y entender.
-  Posibilitan la reusabilidad del código, llamar funciones desde
   distintos programas.

Definición y uso
~~~~~~~~~~~~~~~~

Una función se define anteponiendo la palabra clave ``def`` seguida del
nombre de la función, paréntesis de apertura y cierra y los dos puntos
(:). Luego, el bloque de acciones que la conforman. Veamos la
estructura:

.. code:: python

    def nombre_funcion(argumento1, argumento2, ..., argumentoN):
        accion1
        accion2
        ...
        accionN

En el caso previo la función recibe como entrada argumentos y realiza
una serie de acciones. Las funciones pueden ser definidas en el mismo
programa, con la finalidad de organizar mejor el código. Veamos un
ejemplo de un programa que define y utiliza una función denominada
``muestra_doble()``.

.. code:: python

    # Definición de la función
    def muestra_doble(x):
        '''Imprime en pantalla el doble de x'''
        print(2*x)
     
    # Programa principal
    a = 3.5
    # invoca a la funcion
    muestra_doble(a)
    print('Todo OK')


.. parsed-literal::

    7.0
    Todo OK


Analicemos en detalle la secuencia de ejecución:

-  Desde el programa principal se invoca a la función enviándo la
   variable ``a`` como parámetro
-  La función recibe la entrada haciendo una copia de ``a`` en la
   variable ``x``
-  La función ejecuta sus acciones y vuelve el control al programa
   principal
-  El programa principal continúa la ejecución hasta finalizar

Como vemos, la función no ha retornado valor alguno al programa
principal, modifiquemos la función de manera que en vez de imprimir en
pantalla el doble del valor, lo retorne al programa principal.

.. code:: python

    # Definición de la función
    def calc_doble(x):
        """Retorna el doble de x"""
        return 2*x
     
    # Programa principal
    a = 3.5
    # invoca a la funcion
    doble = calc_doble(a)
    print(doble)


.. parsed-literal::

    7.0


Al igual que en el ejemplo anterior, la función es invocada desde el
programa principal con el parámetro ``a`` y es copiado automáticamente
como ``x`` dentro de la función. Destaquemos las diferencias:

-  El programa principal invoca la función desde una asignación
   (``doble = calc_doble(a)``)
-  Antes de realizarse la asignación, la ejecución pasa el control a la
   función.
-  La función realiza las acciones programadas y al ejecutar la palabra
   reservada ``return`` asigna la operación a su nombre y vuelve el
   control al programa principal
-  El nombre de la función contiene el resultado y es asignado a la
   variable ``doble``
-  Finaliza el programa

Si bien parece trivial, es importante que el nombre de la función sea
acorde a las acciones que realiza e identifique su comportamiento, por
este motivo la función fue renombrada a ``calc_doble``.

El retorno de valores de una función es completamente flexible, se
pueden retornar más de una variable, listas, tuplas, diccionarios o
cualquier combinación de ellas. Veamos un caso de una función que recibe
dos listas de nombres y teléfonos y retorna una agenda en una estructura
de diccionario, donde la primer lista conforma las claves y la segunda
los valores.

.. code:: python

    def arma_agenda(lista_nom, lista_tel):
        '''recibe 2 listas y retorna un diccionario'''
        d = {}
        for nom, tel in zip(lista_nom, lista_tel):
            d[nom] = tel
        return d
    
    # Programa principal
    n = ['Kliksberg', 'Stiglitz', 'Zaffaroni']
    t = ['23444', '54556', '66554']
    agenda = arma_agenda(n,t)
    print(agenda)


.. parsed-literal::

    {'Kliksberg': '23444', 'Stiglitz': '54556', 'Zaffaroni': '66554'}


El lector atento abrá notado que en todas las funciones debajo de su
definición existe un texto encerrado entre comillas triples (como por
ejemplo ``"""Retorna el doble de x"""``). Esto es un comentario que se
utiliza para documentar brevemente, y con nuestras palabras, que es lo
que realiza dicha función. Su uso es opcional, pero es muy recomendable,
dado que puede ser de mucha utilidad tanto para nostros como para otros
desarrolladores.

Variables globales y locales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hemos visto que las funciones reciben un conjunto de valores a través de
sus parámetros, sin embargo no fueron modificados dentro de la función.
La pregunta que surge es: ¿Podemos cambiarlos? ¿Qué sucede si los
modificamos?

Veamos un ejemplo y su comportamiento:

.. code:: python

    def trata_de_cambiar(nombre):
        nombre = 'Luis Alberto Spinetta'
    
    n = 'Norberto Napolitano'
    trata_de_cambiar(n)
    print(n)


.. parsed-literal::

    Norberto Napolitano


Observamos que la variable no fué modificada o al menos no se ve
reflejado desde el programa principal. Esto sucede debido a que la
variable ``n`` es copiada en la variable ``nombre`` y todo cambio que se
realice en el interior de ``trata_de_cambiar`` será local, es decir, su
ámbito de validez se limita a la función, de manera tal que tanto
``Spinetta`` como ``Napolitano`` son irremplazables.

No obstante, existen estructuras de datos que al ser modificadas dentro
la función su cambio se verá reflejado en el programa principal. La
única condición para que sea posible este comportamiento es que la
estructura a ser modificada como argumentos sea *mutable*, tal es el
caso de los diccionarios y listas.

Veamos un caso donde definimos una función que recibe dos argumentos,
una cadena de caracteres y una lista, de tipo *inmutable* y *mutable*
respectivamente.

.. code:: python

    def todo_cambia(musico, listam):
        listam.append(musico)
    
    artistas = []
    
    todo_cambia('Luis Alberto Spinetta', artistas)
    todo_cambia('Chango Spasiuk',artistas)
    todo_cambia('Norberto Napolitano',artistas)
    todo_cambia('Charly García',artistas)
    
    print(artistas)


.. parsed-literal::

    ['Luis Alberto Spinetta', 'Chango Spasiuk', 'Norberto Napolitano', 
    'Charly García']


El primer argumento, ``musico``, es una cadena de caracteres que
contiene el nombre de un artista y el segundo argumento, ``listam``, es
una lista donde se agrega el músico.

Es importante notar que el ejemplo es equivalente al anterior, la
diferencia radica únicamente en que el argumento que es modificado en la
función es la misma lista del programa principal, no una copia,
independientemente que en el programa principal utilice un identificador
diferente al de la función.

Ahora bien, existen casos donde es necesario modificar una variable del
programa principal desde una función sin que sea recibida a través de
sus argumentos. Para realizar este tipo de acciones necesitamos utilizar
variables cuyo ámbito de validez sea tanto el programa principal como la
función, es decir, variables globales.

Veamos un ejemplo de una función que incrementa una variable global
cuando el número que recibe por argumentos es par:

.. code:: python

    def contar(num):
        global pares
        if num % 2 == 0:
            pares = pares + 1
    
    pares = 0
    
    contar(2)
    contar(5)
    contar(8)
    
    print(pares)


.. parsed-literal::

    2


Algunos detalles a destacar sobre variables globales:

-  Se debe anteponer a la variable la palabra reservada ``global``
-  Toda modificación repercutirá en el programa principal

El uso de variables globales es una práctica que generalmente debe ser
evitada. En la mayoría de los casos es preferible utilizar un parámetro
y que la función retorne en su nombre el valor modificado.

Agrupando el código en módulos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hemos visto como organizar mejor el código a través de funciones, sin
embargo, una de las ventajas de utilizar funciones propias es evitar la
reescritura. Carece de sentido tener que reprogramar una misma función
por cada programa y, por otro lado, con el paso del tiempo es muy
probable que no todas las versiones sean idénticas y por ende, su
comportamiento puede diferir.

Para solucionar este tipo de problemas y sacar provecho del uso de
funciones existen los módulos, cuya utilidad es la de contener varias
funciones que realicen algún tipo de tarea afin.

Por ejemplo, una serie de funciones para cálculo matemático sería útil
que estén contenidas en un mismo módulo, otras funciones para
procesamiento de sonido en un módulo destinado a tal fin, o bien, una
serie de funciones destinadas a almacenar todas las funciones relativas
a un determinado proyecto.

Para comprender la implementación veamos un módulo trivial, que contenga
saludos en diferentes idiomas. Almacenamos en el archivo ``saludo.py``
las siguientes funciones:

.. code:: python

    def espanol(nom):
        print('Hola', nom)

    def quechua(nom):
        print('Napaykullayki', nom)
        
    def italiano(nom):
        print('Ciao', nom)

    def guarani(nom):
        '''Buen dia, cómo estas?'''
        print("Mba'éichapa ndepyhareve", nom)

    def aymara(nom):
        '''¿cómo estás?'''
        print('Kamisaraki', nom)
        
    def maya(nom):
        '''¿cómo estás?'''
        print('Biix yanilech?', nom)

Luego, creamos el programa desde donde será importado el módulo e
invocadas las funciones que contiene. Por ejemplo, en ``charlando.py``
hacemos lo siguiente:

.. code:: python

    import saludo

    n = input('Ingrese su nombre: ')
    saludo.italiano(n)
    saludo.guarani(n)

Como observamos, el módulo es importado a través del nombre del archivo
(sin la extensión *.py*) y luego, se invocan las funciones utilizando el
nombre del módulo y la función separado por un punto (.).

De esta manera, tenemos acceso a la totalidad de las funciones definidas
bajo el módulo, pero, para el caso que únicamente se utilice una función
específica, es posible especificarlo en la cláusula import del siguiente
modo:

.. code:: python

    from saludo import italiano, guarani

    n = input('Ingrese su nombre: ')
    italiano(n)
    guarani(n)

De esta manera, es posible invocar solamente las funciones importadas.

La biblioteca estándar
----------------------

Se recomienda la lectura del capítulo *Pequeño paseo por la Biblioteca
Estándar. Parte I* (pag. 72) del Tutorial de Python.

Archivos
--------

Hasta aquí hemos trabajado con información almacenada en estructuras de
datos, ya sea a partir de la lectura interactiva (utilizando la función
``input``) o cargada estáticamente en el mismo código del programa y, la
salida ha sido siempre a través de la impresión en pantalla (utilizando
la función ``print``).

La limitación de este modo de trabajo es que la información no se
almacena de modo persistente. Para resolver este inconveniente veremos
en la presente sección la manera de utilizar información de entrada y
salida para nuestros programas a través de archivos de texto.

Incorporar el uso de archivos a un programa generalmente requiere las
siguientes acciones:

-  Abrir el archivo: la apertura de un achivo se realiza a partir de la
   primitiva ``open`` y consiste en asociar un elemento del programa con
   un archivo en particular.
-  Elegir el modo de apertura: un archivo puede abrirse para lectura
   (r), escritura (w), agregado (a), binario (b), lectura/escritura (+)
-  Leer ó escribir en el archivo
-  Cerrar el archivo

Trabajemos con un archivo de texto, por ejemplo ``archi01.txt``, con el
siguiente contenido:

::

    enero 30
    febrero 60
    marzo 55

Lectura
~~~~~~~

Vamos a realizar la lectura de este archivo e imprimir por pantalla su
contenido. Dos de los métodos más comunes son:

-  readline(): lee de a una línea por vez
-  readlines(): lee todo el contenido del archivo y lo retorna en una
   lista

Veamos como sería el funcionamiento del primer caso:

.. code:: python

    # Apertura del archivo en modo lectura
    f = open('ejemplos/u4/archi01.txt', 'r')
    
    # Lee la primer línea
    r = f.readline()
    print(r)
    
    # Lee la segunda línea
    r = f.readline()
    print(r)
    
    # Cierra el archivo
    f.close()


.. parsed-literal::

    enero 30
    
    febrero 60
    


Probablemente sea más práctico realizar la lectura línea por línea en un
ciclo iterativo hasta que se llegue al final del archivo. Esto se puede
realizar combinando lo anterior con un ciclo repetitivo ``while``:

.. code:: python

    # Apertura del archivo en modo lectura
    f = open('ejemplos/u4/archi01.txt', 'r')
    
    # Lee la primer línea
    r = f.readline()
    while r:
        print(r)
        # lee la sgte
        r = f.readline()
    f.close()


.. parsed-literal::

    enero 30
    
    febrero 60
    
    marzo 55
    


En este caso, la función ``readline`` retornara ``False`` cuando se
llegue al final del archivo, y por lo tanto se saldrá del ciclo
``while``. Otro método más directo y elegante -en general preferido-
para realizar un comportamiento equivalente (agregado desde la versión
de Python 2.2) es iterar sobre los mismos archivos, esto es:

.. code:: python

    # Apertura en modo lectura (por defecto)
    f = open('ejemplos/u4/archi01.txt')
    
    for r in f:
        print(r)
    f.close()


::


    ---------------------------------------------------------------------------

    IOError                                   Traceback (most recent call last)

    <ipython-input-2-048e5e9434f7> in <module>()
          1 # Apertura en modo lectura (por defecto)
    ----> 2 f = open('ejemplos/u4/archi01.txt')
          3 
          4 for r in f:
          5     print(r)


    IOError: [Errno 2] No such file or directory: 'ejemplos/u4/archi01.txt'


El método ``readlines()`` lee el contenido completo del archivo
retornando una lista con su contenido, donde cada elemento corresponde a
un renglón del archivo.

Este método es más directo y suele ser útil para archivos que no son
excesivamente grandes. Veamos un ejemplo:

.. code:: python

    # Apertura del archivo en modo lectura
    f = open('ejemplos/u4/archi01.txt', 'r')
    
    # Lee todo el achivo
    todo = f.readlines()
    
    # 1er linea
    print(todo[0])
    
    # lista con todo el contenido
    print(todo)
    
    f.close()


.. parsed-literal::

    enero 30
    
    ['enero 30\n', 'febrero 60\n', 'marzo 55\n']


Ahora bien, podemos procesar los datos que son leidos del archivo.
Hagamos el cálculo de un promedio con los valores numéricos de cada mes,
para esto debemos extraer de la cadena de caracteres solamente aquellos
valores que siguen a la cadena de caracteres correspondiente al mes.
Para esto haremos uso de la función ``split()``:

.. code:: python

    # Apertura del archivo en modo lectura
    f = open('ejemplos/u4/archi01.txt', 'r')
    
    # Lee todo el achivo
    todo = f.readlines()
    
    # para promedio
    acum = 0
    cont = 0
    
    for r in todo:
        mes, val = r.split()    # separo por espacio
        acum = acum + int(val)  # sumo convirtiendo a entero
        cont = cont + 1         # cuento los valores
        
    f.close()
    promedio = acum/cont
    print('Promedio: ', promedio)


.. parsed-literal::

    Promedio:  48.333333333333336


Escritura
~~~~~~~~~

Para escribir datos en un archivo, inicialmente se lo abre para
escritura, luego se pueden utilizar dos métodos:

-  write(r): escribe el contenido de r en un renglón del archivo
-  writelines(L): escribe el contenido completo de la lista L en el
   archivo

Veamos un ejemplo de ``write``:

.. code:: python

    # Crea archivo en modo escritura
    f = open('ejemplos/u4/archi02.txt', 'w')
    
    # Lee todo el achivo
    r1 = 'nace una flor\n'
    f.write(r1)
    r1 = 'todos los dias\n'
    f.write(r1)
    r1 = 'sale el sol\n'
    f.write(r1)
    
    f.close()

El programa creó el archivo y luego escribió los tres renglones. Se debe
notar que al final de cada cadena se utilizó el caracter especial ``\n``
que se traduce en un salto de línea, sino cada texto se hubiese escrito
a continuación.

Ahora veremos un ejemplo haciendo uso del método ``writelines()``:

.. code:: python

    # Crea archivo en modo escritura
    f = open('ejemplos/u4/archi03.txt', 'w')
    
    # Lee todo el achivo
    L = ['nace una flor\n', 'todos los dias\n', 'sale el sol\n']
    f.writelines(L)
    
    f.close()

Como se observa, al igual que en el método anterior se debe agregar el
caracter especial de retorno de línea al finalizar cada cadena. Se debe
tener en cuenta que de no existir el archivo es creado pero, es borrado
su contenido en caso contrario, por lo que debe prestarte especial
atención para evitar la pérdida de datos involuntaria.

En aquellos casos donde sea necesario agregar contenido a un archivo ya
existente entonces se debe utilizar el modo de apertura ``a``
(proveniente de Append). Veamos un ejemplo en el que se agregan unas
líneas de datos al archivo ``archi01.txt``.

.. code:: python

    # Abre archivo en modo append
    f = open('ejemplos/u4/archi01.txt', 'a')
    
    # Lee todo el achivo
    L = ['abril 33\n', 'mayo 21\n', 'junio 88\n']
    f.writelines(L)
    
    f.close()

Finalmente el archivo quedará con el siguiente contenido:

::

    enero 30
    febrero 60
    marzo 55
    abril 33
    mayo 21
    junio 88

Es muy importante recordar que siempre debemos cerrar el archivo una vez
que hemos trabajado con el mismo (función ``close()``),
independientemente de si lo hemos utilizado para lectura o para
escritura.
