def insertion_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de Insertion Sort.

    Parámetros:
    arr (list): La lista de elementos a ordenar.

    Retorna:
    list: La lista ordenada.
    """
    if len(arr) <= 1:
        return
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def leer_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        datos = [int(line.strip()) for line in f]
    return datos

datos_aleatorios_leidos = leer_desde_archivo('datos_aleatorios.txt') ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

insertion_sort(datos_aleatorios_leidos)

print(datos_aleatorios_leidos)