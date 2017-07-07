Guía de ejercitación N°3: estructuras de datos
----------------------------------------------

:Autor: Emiliano López - elopez@fich.unl.edu.ar

1. Ingrese las notas de alumnos de un curso de programación hasta que el valor sea negativo. Agregue estos valores en una lista y luego muestre el promedio y la cantidad de alumnos que lo superaron. 

2. Almacene 10 nombres de personas en una lista que son ingresados por teclado. Muestre por pantallala  lista  original,  ordenada,  en  sentido  inverso,  y  pase  a  mayúsculas  la  primer  letra.  Además,  permita ingresar un nombre que sea eliminado de la lista y muestre el resultado de la eliminación o un mensaje alusivo si no fue posible la eliminación.

3. Cree una lista con 100 valores numéricos, del 0 al 99. Luego mezcle la lista en forma aleatoria de modo que pueda simular un bolillero de un bingo, donde se van sacando números al azar y mostrando uno a uno.

4. El operador ``in`` sirve para consultar si un elemento se encuentra en una secuencia, por ejemplo, ``if e in lista``. Agregue al ejercicio previo la posibilidad para que dos usuarios ingresen 5 números de su bingo y que el programa indique el ganador.

5. Se lee una cadena de caracteres por teclado y se pide que la traduzca a código morse utilizando el siguiente diccionario como base:

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
