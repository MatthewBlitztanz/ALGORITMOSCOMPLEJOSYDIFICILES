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

def mamasoytrans(matrix):
    """
    Realiza la transposición manual de una matriz.

    Parámetros:
    matrix (np.ndarray): La matriz a transponer.

    Retorna:
    np.ndarray: La matriz transpuesta.
    """
    n = len(matrix)
    transposed = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    return transposed

def matrix_returns(A, B):
    """
    Multiplica dos matrices utilizando la transposición para optimizar el acceso en caché.

    Parámetros:
    A (np.ndarray): La primera matriz a multiplicar.
    B (np.ndarray): La segunda matriz a multiplicar.

    Retorna:
    np.ndarray: La matriz resultante de la multiplicación de A y B.
    """
    n = len(A)
    B_T = mamasoytrans(B)
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += A[i][k] * B_T[j][k]
            C[i][j] = sum
    return C

matrices = leer_matrices_bin('matriz_cuadrada.bin', 100) ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

for i in range(0, 100, 2):
    if i + 1 < 100:
        A = matrices[i]
        B = matrices[i + 1]
        C = matrix_returns(A, B)

matrices = leer_matrices_bin('matriz_rectangular.bin', 100) ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

for i in range(0, 100, 2):
    if i + 1 < 100:
        A = matrices[i]
        B = matrices[i + 1]
        C = matrix_returns(A, B)