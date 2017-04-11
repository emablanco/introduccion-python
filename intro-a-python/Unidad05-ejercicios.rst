Guía de ejercitación N°5
------------------------

1. Realice un programa orientado a objetos para gestionar cds de música. El programa debe permitir cargar los siguientes datos de por cd:

- Nombre del CD
- Artista o grupo
- Género
- Año de publicación
- Duración en minutos
- Lista de canciones

El uso para cargar los datos de un cd debe ser similar al siguiente:

.. code:: python

    cd1 = CD()
    cd1.setNombreCD('Artaud')
    cd1.setArtista('Pescado Rabioso')
    cd1.setGenero('Rock')
    cd1.setFecha(1973)
    cd1.setDuracion('36:56')
    cd1.addCancion('Todas las hojas son del viento')
    cd1.addCancion('Cementerio Club')

    print(cd1.getNombreCD())

Una vez definido la clase para el tipo CD cree otra clase denominada Coleccion que consista simplemente en una lista de objetos CD y dos métodos que permitan buscar el CD de mayor duración o listar todos los de un determinado género musical.

El uso de la clase Coleccion podría ser:

.. code:: python

    misCDs = Coleccion()
    misCDs.addCD(cd1)
    misCDs.addCD(cd2)
    listarock = misCDs.getxGenero('Rock')
    cd_largo = misCDs.getMayorDuracion()
    print(cd_largo.getNombreCD())

2. La biblioteca `pandas <http://pandas.pydata.org/>`_ es utilizada ampliamente para realizar cálculos y visualización de datos de modo similar al que ofrecen las planillas de cálculo. Instale y haga uso de la biblioteca pandas para procesar un archivo de una planilla de cálculos y grafique algunas de sus columnas de datos.
