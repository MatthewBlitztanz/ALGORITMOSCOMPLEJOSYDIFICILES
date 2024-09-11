import numpy as np

def leer_matrices_bin(nombre_archivo, n):
    """
    Lee n matrices desde un archivo binario.

    Parámetros:
    nombre_archivo (str): Nombre del archivo binario de donde se leerán las matrices.
    n (int): Número de matrices a leer desde el archivo.

    Retorna:
    list: Una lista de matrices (np.ndarray) leídas desde el archivo binario.
    """
    matrices = []
    with open(nombre_archivo, 'rb') as f:
        for _ in range(n):
            matrices.append(np.load(f))
    return matrices

def multiplicacion_matrices_tradicional(A, B):
    """
    Multiplica dos matrices utilizando el algoritmo iterativo cúbico tradicional (O(n^3)).

    Parámetros:
    A (np.ndarray): La primera matriz a multiplicar.
    B (np.ndarray): La segunda matriz a multiplicar.

    Retorna:
    np.ndarray: La matriz resultante de la multiplicación de A y B.

    Lanza:
    ValueError: Si las dimensiones de las matrices no permiten la multiplicación.
    """
    filas_A, columnas_A = A.shape
    filas_B, columnas_B = B.shape

    if columnas_A != filas_B:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")

    C = np.zeros((filas_A, columnas_B))

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

n = 100

matrices = leer_matrices_bin('matriz_cuadrada.bin', n) ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

for i in range(0, 100, 2):
    if i + 1 < n:
        A = matrices[i]
        B = matrices[i + 1]
        C = multiplicacion_matrices_tradicional(A, B)


matrices = leer_matrices_bin('matriz_rectangular.bin', n) ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

for i in range(0, 100, 2):
    if i + 1 < n:
        A = matrices[i]
        B = matrices[i + 1]
        C = multiplicacion_matrices_tradicional(A, B)