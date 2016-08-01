--------------------------------------
Introducción al Desarrollo de Software
--------------------------------------

:Autor: Emiliano López - elopez@fich.unl.edu.ar
:Colaborador: Maximiliano Boscovich - maximiliano@boscovich.com.ar
:Fecha: |date| |time| - [`última versión disponible <https://gitlab.com/emilopez/dev01>`__]

.. header:: 
    Introducción al Desarrollo de Software

.. footer::
    ###Page### / ###Total###

.. contents:: Contenidos


.. sectnum::

.. raw:: pdf

   PageBreak oneColumn

.. |date| date:: %d/%m/%Y
.. |time| date:: %H:%M


.. raw:: pdf

   PageBreak oneColumn

**LICENCIA CC BY-SA 4.0**

.. figure:: img/LICENCIA-CC.png
   :alt: 
   :width: 300 px

Introducción al desarrollo de software por Emiliano López se distribuye bajo una **Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional**.

A continuación una traducción de la licencia que podría diferir de la `original <http://creativecommons.org/licenses/by-sa/4.0/>`__:

**Usted es libre para:**

- Compartir - copiar y redistribuir el material en cualquier medio o formato
- Adaptar - remezclar, transformar y crear a partir del material    

Para cualquier propósito, incluso comercialmente

El licenciante no puede revocar estas libertades en tanto usted siga los términos de la licencia

**Bajo los siguientes términos:**

- Atribución - Usted debe darle crédito a esta obra de manera adecuada (ver \*), proporcionando un enlace a la licencia, e indicando si se han realizado cambios (ver \**). Puede hacerlo en cualquier forma razonable, pero no de forma tal que sugiera que usted o su uso tienen el apoyo del licenciante.

- Compartir Igual - Si usted mezcla, transforma o crea nuevo material a partir de esta obra, usted podrá distribuir su contribución siempre que utilice la misma licencia que la obra original. 

\* Si se suministran, usted debe dar el nombre del creador y de las partes atribuidas, un aviso de derechos de autor, una nota de licencia, un aviso legal, y un enlace al material. Las licencias CC anteriores a la versión 4.0 requieren que usted provea el título del material si se incluye, y pueden tener otras ligeras diferencias.

\** En 4.0, debe indicar si ha modificado el material y mantener una indicación de las modificaciones anteriores

.. raw:: pdf

   PageBreak oneColumn

Unidad 5: Introducción a la Programación Orientada a Objetos
============================================================

Python es un lenguaje de Programación Orientado a Objetos (POO), lo que significa que puede manipular construcciones llamadas objetos. Se puede pensar en un objeto como una única estructura que contiene tanto datos como funciones, solo que las funciones en este contexto son llamadas *métodos*. La Programación Orientada a Objetos introduce terminología, y una gran parte es simplemente darle un nuevo nombre a lo que ya estuvimos usando.

Si bien Python nos provee un gran número de tipos y estructuras ya definidas (int, float, str, dict, list, etc.), en muchas situaciones resultarán insuficientes, por lo que será necesario crear nuestros propios tipos que almacenen la información relevante para el problema a resolver y contengan las funciones para operar con esa información.

Supongamos un programa que gestiona jugadores de fútbol de un club, independientemente de los detalles de implementación, contar con un tipo de dato ``Jugador`` que permita cargar sus datos y contar con funcionalidades asociadas nos brinda la posibilidad de tener un código mas legible y organizado. 

Por ejemplo, para cargar los datos de un nuevo jugador el código podría ser del siguiente modo:

.. code:: python

    pipa = Jugador('Lucas Alario', '8-10-1992', 'Delantero')
    pipa.agregar_club('Colon')
    pipa.agregar_club('River')
    print("Club Actual: ", pipa.club_actual())
    print("Edad: ", pipa.calcular_edad())

Del fragmento de código previo podemos destacar:

-  Al identificador *pipa* se le asigna un objeto de *tipo de dato* ``Jugador`` que contiene tres atributos: nombre, fecha de nacimiento y posición. 

-  Además, este objeto tiene tres métodos asociados: ``agregar_club()``, ``club_actual()`` y ``calcular_edad()``.


Atributos y métodos
-------------------

El modo de declarar este nuevo tipo ``Jugador`` con sus atributos y métodos se lleva a cabo definiendo una **clase**, a continuación veamos el modo de implementarla:

.. code:: python

    from datetime import date
    import dateutil

    class Jugador():
        """Clase Jugador"""
        def __init__(self, nombre=None, fecha_nac=None, posicion=None):
            '''define los atributos que se pasan al crearlo'''
            self.nombre = nombre
            self.fecha_nac = fecha_nac
            self.posicion = posicion
            self.clubes = []
            
        def agregar_club(self, club):
            '''agrega club a la lista de clubes'''
            self.clubes.append(club)
        
        def club_actual(self):
            '''retorna el club actual'''
            return self.clubes[-1]
    
        def calcular_edad(self):
            '''retorna la edad del jugador'''
            d, m, a = self.fecha_nac.split("-")
            fecha_nac = date(int(a), int(m), int(d))
            edad = dateutil.relativedelta.relativedelta(date.today(), fecha_nac)
            return edad.years



La clase anterior define la estructura de aquellos objetos que sean de tipo ``Jugador()``. De los cuatro métodos que se observan, hay uno que merece especial atención, que comienza y termina con dos guiones bajos:

-   ``__init__``: este método se denomina constructor, ya que está directamente asociado a la declaración e inicialización de un objeto. Esto es, en la el fragmento de código ``pipa = Jugador('Lucas Alario', '8-10-1992', 'Delantero')`` se lo invoca implícitamente (automáticamente). 

    Los argumentos se corresponden con ``nombre``, ``fecha_nac`` y ``posicion``. El primer argumento, ``self``, hace referencia al mismo objeto y es utilizado para definir sus atributos dentro del constructor.

Los métodos restantes son funciones asociadas al objeto:

-  ``agregar_club()``: agrega un club donde jugó
-  ``club_actual()``: retorna el último club
-  ``calcular_edad()``: calcula la edad y la retorna

Los datos relativos al club se cargan en una lista almacenada en el atributo ``clubes``. El uso de métodos para modificar atributos es denominado **encapsulamiento**. 

.. Note::

    Es común encontrar métodos cuyos nombres empiecen con la palabra *set*, en aquellos casos donde se realizan modificaciones sobre los atributos del objeto, y métodos cuyos nombres comienzan con la palabra *get* para retornan propiedades de los objetos. Si bien es una convención opcional es recomendable llamarlos de este modo.

Almacenando las clases en módulos
---------------------------------

Las clases pueden ser almacenadas en archivos diferentes, del mismo modo que las funciones han sido almacenadas en módulos. El código correspondiente a la clase ``Jugador`` puede ser almacenado en un archivo ``futbol.py`` para luego ser importado desde otro programa. Para este ejemplo su uso sería del siguiente modo:

.. code:: python

    from futbol import Jugador
    jug = Jugador('Lucas Alario', '8-10-1992', 'Delantero')

Métodos especiales
------------------

Así como el constructor ``__init__``, existen otros métodos especiales que al están definidos en la clase serán invocados en forma automática. A continuación veremos los mas comunes.

Impresión
~~~~~~~~~

Si está definido el método ``__str__`` dentro de la clase, entonces será invocado automáticamente cada vez que se utilice la función ``print()`` con el objeto como argumento. Veamos la implementación:

.. code:: python

    def __str__(self):
        salida = self.nombre
        salida += '\n' + '='*len(self.nombre) + '\n'
        salida += 'Edad: ' + str(self.calcular_edad()) + '\n'
        salida += 'Posición: ' + self.posicion + '\n'
        return salida

Luego, al imprimir directamente el objeto en pantalla haciendo ``print(pipa)`` obtendremos lo siguiente:

::

    Lucas Alario
    ============
    Edad: 23
    Posición: Delantero

Esto es equivalente a invocar el método especial haciendo ``pipa.__str__()``, aunque no es recomendable ejecutar directamente los métodos especiales.


Comparación
~~~~~~~~~~~

Para resolver las comparaciones entre jugadores, será necesario definir algunos métodos especiales que permiten comparar objetos. En particular, cuando se quiere que los objetos puedan ser ordenados, los métodos que se debe definir son:

-  ``__lt__`` menor que,
-  ``__le__`` menor o igual,
-  ``__eq__`` igual,
-  ``__ne__`` distinto,
-  ``__gt__`` mayor que,
-  ``__ge__`` mayor o igual

Para dos objetos x, y:

-  ``x < y`` llama a ``x.__lt__(y)``,
-  ``x <= y`` llama a ``x.__le__(y)``,
-  ``x == y`` llama a ``x.__eq__(y)``,
-  ``x != y`` llama a ``x.__ne__(y)``,
-  ``x > y`` llama a ``x.__gt__(y)``,
-  ``x >= y`` llama a ``x.__ge__(y)``.

Para el ejemplo que estamos desarrollando, solamente programaremos el método ``__lt__``, ya que al no ser un jugador menor que otro, nos retorna el complemento. 

En la comparación formatearemos la fecha en el formato *aaaammmdd* ya que al convertirla a un entero podremos comprarla como un simple número, donde uno mas grande significa que el jugador es mas joven y, mas adulto, en caso contrario.

La implementación sería:

.. code:: python

    def __lt__(self, otro):
        '''retorna True si self es menor a otro'''
        return (self.calcular_edad() > otro.calcular_edad())

Luego, lo usamos:

.. code:: python

    d10s = Jugador('El Diego', '30-10-1960', 'Enganche')
    print(pipa > d10s)

Algebraicos
~~~~~~~~~~~

Existen métodos especiales para todos los operadores matemáticos, de modo que al operar dos objetos, por ejemplo sumarlos, se invoca al método específico y se realiza la operación. Esto es también denominado sobrecarga de operadores, ya que se le asigna una función específica a un operador cuando es utilizado con objetos.

Para el ejemplo visto usaremos el monto del pase, así que se debe agregar el atributo *valor* a la clase e incorporar el método especial ``__add__`` de modo que al sumar objetos de tipo ``Jugador()`` se sumen estos campos. 

.. code:: python

        def __add__(self, otro):
            return self.valor + otro.valor

Si ahora sumamos dos jugadores, obtendremos la suma de sus valores.

.. code:: python
    
    # otro jugador
    higuain = Jugador('Gonzalo Higuaín', '10-12-1987', 'Desconocido')

    # asignamos valor a cada jugador
    pipa.valor = 1130000
    d10s.valor = 9000000
    higuain.valor = 1.20

    # sumamos los jugadores
    valor_equipo = pipa + d10s + higuain
    print(valor_equipo)

Del mismo modo se implementan los métodos especiales para los siguientes operadores binarios:

::

    Operador            Método

     +          __add__(self, other)
     -          __sub__(self, other)
     *          __mul__(self, other)
     //         __floordiv__(self, other)
     /          __div__(self, other)
     %          __mod__(self, other)
     **         __pow__(self, other[, modulo])
     <<         __lshift__(self, other)
     >>         __rshift__(self, other)
     &          __and__(self, other)
     ^          __xor__(self, other)
     |          __or__(self, other) 
     

Existen muchos otros métodos especiales como los de asignaciones extendidas y operadores unarios.

El presente capítulo ha sido una breve introducción a la POO, a continuación se expone el código completo de lo desarrollado.

**En jugadores.py:**

.. code:: python

    from datetime import date
    import dateutil

    class Jugador():
        """Clase Jugador"""
        def __init__(self, nombre=None, fecha_nac=None, posicion=None):
            '''define los atributos que se pasan al crearlo'''
            self.nombre = nombre
            self.fecha_nac = fecha_nac
            self.posicion = posicion
            self.clubes = []
            
        def agregar_club(self, club):
            '''agrega club a la lista de clubes'''
            self.clubes.append(club)
        
        def club_actual(self):
            '''retorna el club actual'''
            return self.clubes[-1]
    
        def calcular_edad(self):
            '''retorna la edad del jugador'''
            d, m, a = self.fecha_nac.split("-")
            fecha_nac = date(int(a), int(m), int(d))
            edad = dateutil.relativedelta.relativedelta(date.today(), fecha_nac)
            return edad.years
        
        def __str__(self):
            salida = self.nombre
            salida += '\n' + '='*len(self.nombre) + '\n'
            salida += 'Edad: ' + str(self.calcular_edad()) + '\n'
            salida += 'Posición: ' + self.posicion + '\n'
            return salida
        
        def __lt__(self, otro):
            '''retorna True si self es menor a otro'''
            return (self.calcular_edad() > otro.calcular_edad())
         
        def __add__(self, otro):
            return self.valor + otro.valor
    
**En prueba_jugadores.py:**

.. code:: python 
   
    from futbol import Jugador
    pipa = Jugador('Lucas Alario', '08-10-1992', 'Delantero')
    pipa.agregar_club('Colon')
    pipa.agregar_club('River')
    print(pipa)
    
    d10s = Jugador('El Diego', '30-10-1960', 'Enganche')
    d10s.agregar_club('Argentino Jr.')
    d10s.agregar_club('Boca')
    d10s.agregar_club('Barcelona')
    d10s.agregar_club('Nápoles')
    d10s.agregar_club('Sevilla')
    d10s.agregar_club("Newell's")
    d10s.agregar_club("Boca")
    print(d10s)
    
    pipa.valor = 1130000
    d10s.valor = 9000000
    monto = pipa + d10s

Se recomienda profundizar este tema en el capítulo *Un primer vistazo a las clases (pag. 61)* del Tutorial de Python.

.. raw:: pdf

   PageBreak oneColumn

Usando módulos externos
-----------------------

Una de las ventajas de la programación orientada a objetos es que permite organizar en una forma mas clara el código de un programa lo que facilita la comprensión para su uso, por este motivo la inmensa mayoría de módulos externos utilizan este paradigma.  En la presente sección aplicaremos los conceptos aprendidos previamente haciendo uso del módulo para procesamiento de imágenes denominado *PIL (Python Imagin Library)*.

.. Note:: Instalando Pillow

    Aquí utilizamos la versión de PIL denominada **Pillow**, para instalarla basta ejecutar bajo la línea de comandos: ``pip3 install pillow``. Para detalles de su instalación puede acceder a la documentación oficial en: http://pillow.readthedocs.io/en/3.0.x/installation.html

Este módulo nos permite analizar y manipular imágenes utilizando el paradigma de orientación a objetos que ha sido descripto con anterioridad. Dentro de las operaciones que realizaremos podemos destacar:

- abrir y guardar archivos de imágenes
- analizar el tamaño y otras propiedades
- modificar el brillo
- separar los colores
- modificar la coloración

.. code:: python 

    from PIL import Image               # importamos Image
    iarchi = input("Archivo: ")         # lee nombre del archivo
    img = Image.open(iarchi)            # Método open
    print('Ancho:', img.width)          # Atributos:
    print('Alto:', img.height)          #    width y height
