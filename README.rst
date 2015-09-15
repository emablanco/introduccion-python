Introducción al Desarrollo de Software
======================================

Objetivo General
----------------

- Conocer los conceptos fundamentales de la algorítmica computacional
- Resolver problemas aplicando un lenguaje estructurado de programación
- Dominar la sintaxis de un lenguaje de programación
- Comprender y reutilizar código desarrollado por terceros

Contenidos mínimos
------------------

- Conceptos básicos: variables, declaraciones, tipos de datos, operadores, expresiones lógicas, estructuras de control, estructuras repetitivas, procedimientos y funciones
- Programación estructurada, modular y orientada a objetos, tipos de lenguajes

Organización del material
-------------------------

Desde estos links se pueden visualizar estáticamente:

* `Unidad 1 <http://nbviewer.ipython.org/urls/gitlab.com/emilopez/dev01/raw/master/Unidad01.ipynb>`_ Conceptos básicos
* `Unidad 2 <http://nbviewer.ipython.org/urls/gitlab.com/emilopez/dev01/raw/master/Unidad02.ipynb>`_ Control de flujo
* `Unidad 3 <http://nbviewer.ipython.org/urls/gitlab.com/emilopez/dev01/raw/master/Unidad03.ipynb>`_ Funciones
* Unidad 4...

Modificar el material
----------------------

Apunte principal
''''''''''''''''
Correr el notebook de ipython3 (versión IPython 3.1.0) bajo el directorio que se encuentran los .ipynb haciendo: ipython3 notebook

Modificar sobre el notebook (por ej, Unidad01.ipynb) y, luego de guardar, se debe:

* Convertir al formato rst haciendo

.. code-block:: bash

	 ipython3 nbconvert Unidad01.ipynb --to rst

Ahora hay dos opciones:

1. USANDO SPHINX: Generar todo el apunte en un único pdf

* Mover el archivo generado (Unidad01.rst) al directorio doc 

.. code-block:: bash

	mv Unidad01.rst doc/

* Regenerar la documentación, estando bajo el directorio doc hacer

.. code-block:: bash

	make html
	make latexpdf

Estos pasos actualizarán la documentación estática almacenada bajo doc/_build

2. USANDO RST2PDF: genera un pdf por unidad (la salida es mas atractiva)

.. code-block:: bash

	rst2pdf Unidad01.rst

Slides
''''''
.. code-block:: bash

    ipython3 nbconvert SlidesU1-01.ipynb --to slides --post serve
    
Sin el último parámetro las guarda como html

Licencia
--------

.. figure:: http://i.creativecommons.org/l/by-sa/2.5/ar/88x31.png
   :target: http://creativecommons.org/licenses/by-sa/2.5/ar/deed.es_AR


    Licencia Creative Commons Atribución-CompartirIgual 2.5 Argentina (CC BY-SA 2.5 AR)

Créditos y referencias
----------------------

El material fue desarrollado específicamente para el curso "Introducción al Desarrollo de Software" de la Tecnicatura Universitaria en Software Libre, perteneciente a la Facultad de Ingeniería y Ciencias Hídricas de la Universidad Nacional del Litoral. 

Gran parte del material utilizado fue basado en los siguientes recursos:

- El tutorial de Python. Guido van Rossum
- Aprenda a pensar como un programador con Python. Allen Downey
- An introduction to computer science. John Zelle
- https://github.com/mgaitan/curso-python-cientifico
- Beginning Python. From Novice to Professional. Second Edition. Magnus Lie Hetland
- The Python Language Reference: https://docs.python.org/3/reference/index.html#reference-index
- The Hitchhiker’s Guide to Python! http://docs.python-guide.org/en/latest/
