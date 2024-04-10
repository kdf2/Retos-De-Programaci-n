"""
Se le proporcionan dos matrices de números enteros nums1 y nums2, 
ordenadas en orden no decreciente, y dos números enteros myn, que representan el número de elementos
en nums1 y nums2 respectivamente.
Fusione nums1 y nums2 en una única matriz ordenada en orden no decreciente.
La función no debe devolver la matriz ordenada final, sino que debe almacenarse dentro de la matriz nums1.
Para dar cabida a esto, nums1 tiene una longitud de m + n, donde los primeros m elementos denotan los 
elementos que deben fusionarse, y los últimos n elementos se establecen en 0 y deben ignorarse. 
nums2 tiene una longitud de n.
"""


class solution:
    def merge (self,num1, m, num2, n):
        num1=num1[:-n]
        for elemento in num2:
            num1.append(elemento)
        num1.sort()
        return num1


Objeto=solution()


num1=[1,2,3,0,0,0]

num2=[2,5,6]
m=3
n=3
print(Objeto.merge(num1, m, num2, n))
