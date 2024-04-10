"""
Dados los nombres y calificaciones de cada estudiante en una clase de N estudiantes, 
guárdelos en una lista anidada e imprima los nombres de los estudiantes que tengan la segunda calificación
más baja.
Nota: Si hay varios estudiantes con la segunda calificación más baja, ordene sus nombres alfabéticamente
e imprima cada nombre en una nueva línea.
"""


if __name__ == '__main__':
    lista_estudiante=[]
    for _ in range(5):
        name = input("Nombre del estudiante: ")
        score = float(input("Ingrese nota: "))
        lista_estudiante.append([name,score])
    print(lista_estudiante)
    primera_nota_min=min(estudiantes[1] for estudiantes in lista_estudiante)
    cantidad=[estudiantes for estudiantes in lista_estudiante if estudiantes[1]==primera_nota_min]
    for cantidad in cantidad:
        lista_estudiante.remove(cantidad)
    segunda_minima=min(estudiante[1] for estudiante in lista_estudiante)
    lista_estudiante = sorted(lista_estudiante)
    for cx in lista_estudiante:
        if cx[1]==segunda_minima:
            print(cx[0])

