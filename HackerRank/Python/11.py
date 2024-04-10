"""
Dada la hoja de puntuación de los participantes para su Día del Deporte Universitario, 
deberá encontrar la puntuación del segundo lugar. Te dan n puntuaciones. 
Guárdelos en una lista y encuentre la puntuación del subcampeón.
La primera línea contiene n . La segunda línea contiene una matriz a[] de n números enteros, 
cada uno separado por un espacio.
"""

if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]
    primer_lugar=max(arr)
    arr=[ indice for indice in arr if indice!=primer_lugar ]
    segundo_ligar=max(arr)
    print("El segun lugar es: ",segundo_ligar)
