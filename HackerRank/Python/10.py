"""
¡Aprendamos sobre la comprensión de listas! Se le dan tres números enteros que representan las dimensiones de un cuboide junto con un número entero.
Imprima una lista de todas las coordenadas posibles dadas por en una cuadrícula 3D donde la suma de no es igual a x+y+z=n. 
Aquí, . Utilice listas de comprensión en lugar de bucles múltiples como ejercicio de aprendizaje.
"""

if __name__ == '__main__':
    x =1 
    y =1
    z = 2 
    n = 3
    """
    for a in range(x+1):
        for b in range(y+1):
            for c in range (z+1):
                if a+b+c!=n:
                    print(a,b,c)
    """
    new_lista=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]
    print(new_lista)