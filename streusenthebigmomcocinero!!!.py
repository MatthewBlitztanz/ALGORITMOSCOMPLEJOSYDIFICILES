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

def pad_matrix(matrix, new_size):
    """
    Añade ceros a una matriz para ajustarla al tamaño especificado.

    Parámetros:
    matrix (np.ndarray): La matriz original que se desea ampliar.
    new_size (int): El tamaño de la nueva matriz cuadrada.

    Retorna:
    np.ndarray: La matriz ampliada con ceros si era necesario.
    """
    padded_matrix = np.zeros((new_size, new_size))

    original_size = len(matrix)
    padded_matrix[:original_size, :original_size] = matrix
    return padded_matrix

def split(matrix):
    """
    Divide una matriz en cuatro submatrices cuadradas de tamaño n/2 x n/2.

    Parámetros:
    matrix (np.ndarray): La matriz que se desea dividir.

    Retorna:
    tuple: Cuatro submatrices de tamaño n/2 x n/2.
    """
    n = len(matrix)
    return matrix[:n//2, :n//2], matrix[:n//2, n//2:], matrix[n//2:, :n//2], matrix[n//2:, n//2:]

def strassen(A, B):
    """
    Implementa el algoritmo de Strassen para la multiplicación de matrices.

    Parámetros:
    A (np.ndarray): La primera matriz a multiplicar.
    B (np.ndarray): La segunda matriz a multiplicar.

    Retorna:
    np.ndarray: La matriz resultante de la multiplicación utilizando Strassen.
    """
    n = len(A)

    if n <= 2:
        return np.dot(A, B)
    
    m = 1 << (n - 1).bit_length()  
    
    if n != m:
        A = pad_matrix(A, m)
        B = pad_matrix(B, m)
    
    a, b, c, d = split(A)
    e, f, g, h = split(B)
    
    p1 = strassen(a+d, e+h)
    p2 = strassen(d, g-e)
    p3 = strassen(a+b, h)
    p4 = strassen(b-d, g+h)
    p5 = strassen(a, f-h)
    p6 = strassen(c+d, e)
    p7 = strassen(a-c, e+f)
    
    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    if n != m:
        C = C[:n, :n]
    
    return C

matrices = leer_matrices_bin('matriz_cuadrada.bin', 100) ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

for i in range(0, 100, 2):
    if i + 1 < 100:
        A = matrices[i]
        B = matrices[i + 1]
        C = strassen(A, B)
