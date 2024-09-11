import sys

sys.setrecursionlimit(15000)

def partition(arr, low, high):
    """
    Función de partición que coloca el pivote en su posición correcta y organiza los elementos menores y mayores alrededor de él.

    Parámetros:
    arr (list): La lista de elementos a ordenar.
    low (int): El índice inicial.
    high (int): El índice final.

    Retorna:
    int: La posición del pivote.
    """
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:

            i += 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1

def quicksort(arr, low, high):
    """
    Ordena una lista utilizando el algoritmo de Quicksort.

    Parámetros:
    arr (list): La lista de elementos a ordenar.
    low (int): El índice inicial.
    high (int): El índice final.
    """
    if low < high:

        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)

        quicksort(arr, pi + 1, high)

def leer_desde_archivo(nombre_archivo):

    with open(nombre_archivo, 'r') as f:
        datos = [int(line.strip()) for line in f]

    return datos


datos_aleatorios_leidos = leer_desde_archivo('datos_aleatorios.txt') ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

quicksort(datos_aleatorios_leidos, 0, len(datos_aleatorios_leidos) - 1)

print(datos_aleatorios_leidos)
