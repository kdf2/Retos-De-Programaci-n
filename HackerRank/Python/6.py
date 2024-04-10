"""
El código auxiliar incluido leerá un número entero.
Sin utilizar ningún método de cadena, intente imprimir lo siguiente:
Ejemplo
n=5
Imprime la cadena.
12345
Formato de entrada
La primera línea contiene un número entero.
Restricciones
Imprima la lista de números enteros desde hasta como una cadena, sin espacio
"""
if __name__ == '__main__':
    n = 3
    print("".join(str(i) for i in  range(1,n+1)))
    