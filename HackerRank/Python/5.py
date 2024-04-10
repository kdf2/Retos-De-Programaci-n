"""
Casi cada cuatro años se añade un día extra al calendario, el 29 de febrero, y el día se denomina bisiesto.
Corrige el calendario por el hecho de que nuestro planeta tarda aproximadamente 365,25 
días en orbitar alrededor del sol. Un año bisiesto contiene un día bisiesto.
En el calendario gregoriano se utilizan tres condiciones para identificar los años bisiestos:
El año se puede dividir uniformemente entre 4, es bisiesto, a menos que:
El año se puede dividir uniformemente entre 100, NO es año bisiesto, a menos que:
El año también es divisible por 400. Entonces es un año bisiesto.
Esto significa que en el calendario gregoriano los años 2000 y 2400 son años bisiestos, 
mientras que 1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos. Fuente

Tarea
Dado un año, determine si es bisiesto. Si es un año bisiesto, devuelve el valor booleano Verdadero; 
en caso contrario, devuelve Falso.
Tenga en cuenta que el código auxiliar proporcionado lee y pasa argumentos a la función is_leap. 
Solo es necesario completar la función is_leap.
"""
def is_leap(year):
    leap = False
    if(not year % 4):
        if(not year % 100 ):
            if(not  year % 400):
                leap= True
            else:
                leap =False
        else:
            leap = True
    else:
        leap =False
    return leap

print(is_leap(2020))