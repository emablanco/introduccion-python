Guía de ejercitación N°3: control de flujo
------------------------------------------

:Autor: Emiliano López - elopez@fich.unl.edu.ar

1. Con el siguiente fragmento de programa se puede determinar si el caracter almacenado en 
la variable ``letra`` es una vocal:

.. code:: python

    if letra in ("aeiou"):
        print("Es vocal!")
        
Utilizando el fragmento previo realice un programa que permita ingresar una palabra e 
informe la cantidad de vocales que posee. 

2. Basado en el ejercicio anterior, extiéndalo para que contabilice la repetición de cada vocal.
Si por ejemplo se ingresa la palabra "divididos" debería mostrar que la vocal *i* se repite 3 veces y la *o* una.

3. Utilice una estructura repetitiva ``for`` para iterar sobre las letras de una palabra 
y muestre en pantalla su versión encriptada. Para encriptarla imprima en pantalla el 
reemplazo de una letra con un número según lo siguiente: a->4, b->8, e->3, f->7, t->2, 
g->9, i->1, o->0. Si por ejemplo se ingresa la cadena "fontanarosa" debería mostrar *70n24n4r0s4*.

4. Realice un programa que lea las calificaciones de un curso y muestre el promedio y 
la nota mas alta. La lectura de notas finaliza cuando se ingresa un valor negativo.

5. Utilizando lo visto hasta aquí (variables, while y for), de qué manera podría modificar
el ejercicio previo para mostrar cuántos alumnos superaron el promedio.

6. Se ingresan por teclado la edad de 20 personas. Muestre en pantalla las edades de las 
dos personas mayores. 



7. Modifique el programa anterior para que en lugar de ingresar las edades sean generadas en forma aleatoria.

8. Programe el cálculo de la sensación térmica a partir de diferentes valores de temperatura del aire y velocidad del viento.
Utilice la siguiente ecuación para el cálculo:

sensacion_termica = 13.12 + 0,6215*T - 11,37*V^0,16 +0,3965*T*V^0,16.

Haga uso de esta ecuación para una T que varía entre 5 y 10°C, y para una velocidad de viento que va desde 40 a 50 km/h, ambos valores varían de a una unidad.
