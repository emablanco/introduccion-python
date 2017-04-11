
Guía de ejercitación N° 4: funciones y archivos
-----------------------------------------------


1. Programe el ejercicio de la guía anterior donde se codifica una palabra en código morse, pero utilizando funciones.


2. Escriba una función que reciba como parámetro la temperatura
expresada en grados centígrados (ºC) e imprima en pantalla la misma
temperatura en grados Fahrenheit (ºF). Tenga en cuenta que la formula de
conversión de Celsius a Fahrenheit es la siguiente:

.. math:: F = (9C/5.0) + 32


3. Escriba un programa que lea un archivo con temperaturas expresadas
en grados centigrados, y que luego genere otro archivo que contenga
dichas temperaturas pero expresadas en grado Fahrenheit. Como archivo de
entrada, utilice el siguiente:

::

    10 ºC
    12.5 ºC
    14.2 ºC 
    16.6 ºC
    18.2 ºC
    20.1 ºC
    26.8 ºC
    22.6 ºC
    20.4 ºC


4. Modifique el programa anterior para que soporte como entrada un
archivo que no solo tiene la temperatura expresada en grados
centígrados, sino que puede tener temperaturas expresadas en Fahrenheit
o Kelvin, pero que siga generando un archivo de salida con las
temperaturas en grados Fahrenheit. Para esto tenga en cuenta que la
formula de conversión de Kelvin (ºK) a Fahrenheit (ºF) es la siguiente:

.. math:: F = (9*(K-273.15)/5.0) + 32

Utilice el siguiente archivo de temperaturas de entradas:

::

    50 ºF
    12.5 ºC
    287.35 ºK 
    16.6 ºC
    291.35 ºK
    20.1 ºC
    299.95 ºK
    22.6 ºF
    20.4 ºC


5. El Observatorio de Importaciones de la Prov. de Santa Fe realiza un reporte donde se informa la variación de los volúmenes de importaciones entre el año 2014 y 2016.  Los campos consisten en Rubro, Producto, Unidad, cantidades desde Enero al 20 de Septiembre 2015 y cantidades desde Enero al 20 de Octubre 2016 y se encuentran separados por un punto y coma. En el siguiente `enlace
<https://www.santafe.gov.ar/index.php/web/content/download/231400/1209770/file/Observatorio%20importaciones%20Enero%20a%2020%20Octubre%202014%20-2015%20-2016.csv>`_ descargue el archivo con la información descripta y realice un programa que lea el contenido del archivo e informe: a) El producto que más incrementó su volumen de importación. b) El incremento de kilos del producto "Zanahorias". 


6. Programe una función que reciba tres argumentos: un valor numérico correspondiente a una distancia, una cadena de caracter correspondiente a la unidad de la medida, y otra que significa la unidad a la que se debe convertir. Las unidades de conversión pueden ser "yarda" o "metro", la relación de conversión es 1 metro = 1 yarda / 1.0936, y por lo tanto tenemos que 1 yarda = 1 metro * 1.0936. Invoque la función desde el programa principal convirtiendo de una unidad a otra.


7. Un hospital estudia la inflamación de los pacientes que han sido sometidos a un nuevo tratamiento para la artritis y necesitan analizar los resultados obtenidos. Los datos son almacenados en un archivo donde cada renglón contiene información de un único paciente, las columnas representan los días sucesivos y los valores numéricos representan el nivel de inflamación. Una muestra de las primeras filas del archivo se observan a continuación:

 0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
 0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
 0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
 0,0,2,0,4,2,2,1,6,7,10,7,9,13,8,8,15,10,10,7,17,4,4,7,6,15,6,4,9,11,3,5,6,3,3,4,2,3,2,1
 0,1,1,3,3,1,3,5,2,4,4,7,6,5,3,10,8,10,6,17,9,14,9,7,13,9,12,6,7,7,9,6,3,2,2,4,2,0,1,1

Se solicita que realice un programa que lea el contenido del archivo y muestre por pantalla la inflamación promedio y máxima de cada paciente.
