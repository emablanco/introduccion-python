
Unidad 3: Ejercicios
--------------------

1. Con el siguiente fragmento de programa se puede determinar si una letra es vocal:

.. code:: python

    if letra in ("aeiou"):
        print("Es vocal!")
        
Realice un programa que permita ingresar una palabra y finalmente informe la cantidad 
de vocales que posee. Una vez finalizado el ejercicio, se lo desafía a extenderlo para 
que contabilice la repetición de cada vocal.

2. Utilice una estructura repetitiva ``for`` para iterar sobre las letras de una palabra 
y muestre en pantalla su versión encriptada. Para encriptarla imprima en pantalla el 
reemplazo de una letra con un número según lo siguiente: a->4, b->8, e->3, f->7, t->2, 
g->9, i->1, o->0. 

3. Realice un programa que lea las calificaciones de un curso y muestre el promedio y 
la nota mas alta. La lectura de notas finaliza cuando se ingresa un valor negativo.

4. Agregue al programa previo la funcionalidad siguiente: debe mostrar la cantidad de 
alumnos cuya calificación es superior al promedio.

5. Almacene 10 nombres de personas en una lista que son ingresados por teclado. Muestre
por pantalla la lista original, ordenada, en sentido inverso, y pase a mayúsculas la primer
letra. Además, permita ingresar un nombre que sea eliminado de la lista y muestre el resultado
de la eliminación o un mensaje alusivo si no fue posible la eliminación.

6. NO INCLUIDO: Se lee una cadena de caracteres por teclado y se pide que la traduzca
a código morse utilizando el siguiente diccionario como base:

.. code:: python

    morse = { "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", 
        "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", 
        "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", 
        "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", 
        "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", 
        "Y" : "-.--", "Z" : "--..", "0" : "-----", "1" : ".----", 
        "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", 
        "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", 
        "." : ".-.-.-", "," : "--..--"
    }
