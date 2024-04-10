"""
Se le dan dos cadenas palabra1 y palabra2. Combine las cadenas agregando letras en orden alterno,
comenzando con la palabra1. Si una cadena es más larga que la otra, agregue las letras adicionales 
al final de la cadena fusionada.
Devuelve la cadena fusionada.
"""
class Solution:
    def mergeAlternately(self, word1, word2):
        join=""  
        if len(word1) >= len(word2):
            for indice1, indice2 in zip(word1,word2):
                join+=indice1+indice2
            join+=word1[len(word2):]
        else:
            for indice1, indice2 in zip(word1,word2):
                join+=indice1+indice2
            join+=word2[len(word1):]
        return join


palabra1="abcd"
palabra2="pq"
Objeto= Solution()
print(Objeto.mergeAlternately(palabra1, palabra2))