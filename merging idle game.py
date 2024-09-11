def merge(arr, l, m, r):
    """
    Fusiona dos sublistas de arr[l..m] y arr[m+1..r] en una sola lista ordenada.

    Parámetros:
    arr (list): La lista de elementos que contiene las sublistas a fusionar.
    l (int): Índice inicial de la primera sublista.
    m (int): Índice final de la primera sublista y punto medio.
    r (int): Índice final de la segunda sublista.
    """
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)
 

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     
    j = 0    
    k = l    
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

 
def mergeSort(arr, l, r):
    """
    Ordena una lista utilizando el algoritmo de Merge Sort.

    Parámetros:
    arr (list): La lista de elementos a ordenar.
    l (int): Índice inicial del rango a ordenar.
    r (int): Índice final del rango a ordenar.
    """
    if l < r:
 
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def leer_desde_archivo(nombre_archivo):

    with open(nombre_archivo, 'r') as f:
        datos = [int(line.strip()) for line in f]

    return datos


datos_aleatorios_leidos = leer_desde_archivo('datos_aleatorios.txt') ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

n = len(datos_aleatorios_leidos)

mergeSort(datos_aleatorios_leidos, 0, n - 1)

print(datos_aleatorios_leidos)