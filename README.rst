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

* `Unidad 1 <http://nbviewer.ipython.org/urls/gitlab.com/emilopez/dev01/raw/master/Unidad01.ipynb>`_ Instalación e introducción a los algoritmos computacionales.

* Unidad 2
* Unidad 3
* Unidad 4...

Modificar el material
----------------------

Una vez modificado un notebook (por ej, Unidad01.ipynb) se debe:

* Convertir al formato rst haciendo

.. code-block:: bash

	 ipython nbconvert Unidad01.ipynb --to rst

* Mover el archivo generado (Unidad01.rst) al directorio doc 

.. code-block:: bash

	mv Unidad01.rst doc/

* Regenerar la documentación, estando bajo el directorio doc hacer

.. code-block:: bash

	make html

Estos pasos actualizarán la documentación estática almacenada bajo doc/_build

Licencia
--------

.. figure:: http://i.creativecommons.org/l/by-sa/2.5/ar/88x31.png
   :target: http://creativecommons.org/licenses/by-sa/2.5/ar/deed.es_AR


    Licencia Creative Commons Atribución-CompartirIgual 2.5 Argentina (CC BY-SA 2.5 AR)

Créditos
--------

El material fue desarrollado específicamente para el curso "Introducción al Desarrollo de Software" de la Tecnicatura Universitaria en Software Libre, perteneciente a la Facultad de Ingeniería y Ciencias Hídricas de la Universidad Nacional del Litoral. 

Gran parte del material utilizado fue basado en los siguientes recursos:

- https://github.com/mgaitan/curso-python-cientifico
- 
- 
