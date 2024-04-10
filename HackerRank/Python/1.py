"""
Dado un número entero, realice las siguientes acciones condicionales:
Si es impar, imprima Raro (Weird)
Si es par y está en el rango inclusivo de 2 a 5, imprima No raro (Not Weird)
Si es par y está en el rango inclusivo de 6 a 20, imprima Raro (Weird)
Si es par y mayor que 20, imprima No es raro (Not Weird)
"""
if __name__ == '__main__':
    n = 4;
    if (n % 2 == 0) and ((2 <= n <= 5) or (n > 20)):
        print('Not Weird')
    elif(n % 2 == 1) or ((n % 2 == 0) and (6 <= n <= 20)):
        print('Weird')

#if (2 <= n <= 5):
#if n in range(5, 11): # si n está en el rango 5 - 10*