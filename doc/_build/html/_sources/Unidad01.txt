
Introducción
============

Docente: Emiliano López (emiliano [dot] lopez [at] gmail [dot] com)

En el presente capítulo introduciremos los conceptos necesarios para
desarrollar los primeros algoritmos computacionales. Además, se explican
las herramientas necesarias para llevar a cabo el desarrollo y sus
diferentes alternativas.

Instalando Python
-----------------

Actualmente existen dos versiones de Python comúnmente utilizadas, la
versión 2 y 3, ambas son completamente funcionales y muy utilizadas. En
este curso nos basaremos en la versión 3.

Windows
~~~~~~~

Para instalar Python en una máquina con Windows, debemos seguir los
siguientes pasos:

-  Apuntar el navegador a: https://www.python.org/downloads/windows/
-  Ir al link de la última versión disponible (por ej: latest python 3
   relase)
-  En la sección Files, descargar el instalador correspondiente a su
   arquitectura (64/32 bits), por ej:
   https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi
-  Ejecutar el instalador (por ej: python-3.4.3.msi) aceptando las
   opciones por defecto

GNU/Linux
~~~~~~~~~

En los sistemas operativos serios, es muy probable que ya contemos con
el intérprete instalado, incluso en sus dos versiones. Para instalarlo
utilizando los administradores de paquetes debemos ejecutar los
siguientes comandos desde una terminal:

Para sistemas basados en Debian (como Ubuntu o sus derivados):

.. code:: bash

    apt-get install python3

Entornos de programación
------------------------

El intérprete interactivo
~~~~~~~~~~~~~~~~~~~~~~~~~

Ya con el intérprete de Python podemos comenzar programar. Si ejecutamos
en una terminal ``python3``, ingresaremos al intérprete en modo
interactivo y veremos una salida similar a la siguiente:

.. code:: python

    Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
    [GCC 4.9.1] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Podemos ejecutar algunas operaciones matemáticas para corroborar su
funcionamiento.

.. code:: python

    >>> 2*5
    10
    >>> 2*5+10
    20
    >>> -3*19+3.1415
    -53.8585
    >>> 

El intérprete interactivo mejorado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`IPython <http://ipython.org>`__ es una interfaz mejorada del intérprete
nativo. Se lo puede utilizar en modo consola o a través de una interfaz
web. La instalación en GNU/Linux es: ``apt-get install ipython3``.

La ejecución de ipython desde una terminal nos arroja una pantalla
similar a la siguiente:

::

    emiliano@pynandi:~ $ ipython3
    Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
    Type "copyright", "credits" or "license" for more information.

    IPython 2.3.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: 

Otra alternativa muy interesante son los notebooks de ipython, una
interfaz que permite programar utilizando el navegador web como entorno.
No entraremos en detalle ya que posteriormente analizaremos su
funcionamiento. Se debe ejecutar en una terminal ``ipython3 notebook`` y
esto abrirá el navegador por defecto con el entorno cargado.

Entorno integrado de desarrollo (IDE)
-------------------------------------

Un IDE es un entorno que nos facilita las tareas a la hora de programar.
Consiste en la integración de un editor de texto, con características de
resaltado de sintaxis autocompletado -entre otras-, y el intérprete de
Python. Existen cientos de entornos muy buenos, como por ejemplo
`Spyder <https://github.com/spyder-ide/spyder>`__,
`PyCharm <https://www.jetbrains.com/pycharm>`__ o
`Ninja-IDE <http://ninja-ide.org>`__. Para el presente curso, nos
basaremos en Ninja-IDE, software libre que ha sido desarrollado por la
comunidad de Python Argentina, `PyAr <http://python.org.ar>`__.

Una lista bastante completa sobre las IDEs disponibles pueden
encontrarse en la `wiki oficial de
Python <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`__

El primer programa "Adiós mundo!"
---------------------------------

El acercamiento inicial a un lenguaje de programación suele ser con el
archiconocido programa "Hola mundo". Consiste simmplemente en un
programa que muestra en pantalla ese mensaje.

Renunciando a cualquier pretensión de originalidad comenzaremos del
mismo modo, pero despidiéndonos. Para esto utilizaremos la instrucción
*print()* pasando el mensaje de despedida entre comillas, a continuación
la instrucción y su salida correspondiente.

``print("Adios mundo cruel!")``

Adios mundo cruel!

Ahora bien, es muchísimo más lo que podemos hacer programando además de
saludar cordialmente. Veamos los elementos de un programa que nos
permitirán realizar tareas más complejas y entretenidas.

Elementos de un programa
------------------------

Variables
~~~~~~~~~

Operadores relacionales y lógicos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entrada y salida de datos
~~~~~~~~~~~~~~~~~~~~~~~~~

Ejercicios
----------

