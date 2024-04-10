def incrementar(n):
	return n + 1

numeros = (0, 1, 2, 3, 4)
resultado = map(incrementar, numeros)
resultado_lista = list(resultado)
print(resultado_lista)