Introducción al Desarrollo de Software
======================================

:Autor: Emiliano López - emiliano.lopez@gmail.com
:Colaborador: Maximiliano Boscovich 

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

La documentación está escrita en RestructuredText. Inicialmente fué escrita desde ``ipython3 notebook`` y luego convertidos a rst usando el comando ``ipython3 nbconvert Unidad01.ipynb --to rst``, pero **ahora** se trabaja directamente sobre los rst. Las versiones a tener en cuenta son las rst.

Las versiones iniciales se almacenaron en el directorio ipynb.


Modificar el material
----------------------

Apunte principal
''''''''''''''''

1. Modificar los rst y luego, usando ``rst2pdf``

2. Generar un pdf por unidad usando el estilo mystile.txt

    .. code-block:: bash

        rst2pdf -s style/mystyle.txt Unidad01.rst

Ahora hay que unir con la carátula PDF de provista por la carrera (bajo el directorio caratulas), usamos ``pdftk``:

    .. code-block:: bash

        pdftk caratulas/U1.pdf Unidad01.pdf output Unidad01-ConCaratula.pdf

Finalmente, pisar Unidad01.pdf con la generada que incluye la carátula y almacenar en directorio pdfs

Slides
''''''

Para cada unidad hay slides que fueron usadas como soporte para generar los videostutoriales. Los slides fueron hechos usando ipython3 notebook y mostrándolos con ipython3 usando el siguiente comando:

.. code-block:: bash

    ipython3 nbconvert SlidesU1-01.ipynb --to slides --post serve
    
(Sin el último parámetro las guarda como html pero sin la animación)

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
