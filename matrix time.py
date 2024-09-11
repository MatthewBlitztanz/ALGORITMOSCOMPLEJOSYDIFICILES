import time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import os

import sys

sys.setrecursionlimit(15000)

'''

Decidí no usar comentarios en estas funciones ya que hay un codigo para cada una de ellas donde tienen su propio comentario.

Además así se mantiene un poco el orden en este codigo donde hay varias funciones y algoritmos.

'''

def multiplicacion_matrices_tradicional(A, B):
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


def mamasoytrans(matrix):
    n = len(matrix)
    transposed = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    return transposed

def matrix_returns(A, B):
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


def pad_matrix(matrix, new_size):

    padded_matrix = np.zeros((new_size, new_size))

    original_size = len(matrix)
    padded_matrix[:original_size, :original_size] = matrix
    return padded_matrix

def split(matrix):
    n = len(matrix)
    return matrix[:n//2, :n//2], matrix[:n//2, n//2:], matrix[n//2:, :n//2], matrix[n//2:, n//2:]

def strassen(A, B):
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


def leer_matrices_bin(nombre_archivo, n):
    matrices = []
    with open(nombre_archivo, 'rb') as f:
        for _ in range(n):
            matrices.append(np.load(f))
    return matrices


def test_algorithms(file_name, num_matrices):
    """
    Evalúa el rendimiento de tres algoritmos de multiplicación de matrices en términos de tiempo de ejecución.

    Parámetros:
    - file_name (str): Nombre del archivo binario que contiene las matrices a multiplicar.
    - num_matrices (int): Número de matrices a leer del archivo.

    Retorna:
    - pd.DataFrame: Un DataFrame con los tiempos promedio de ejecución para cada algoritmo.
    """
    matrices = leer_matrices_bin(file_name, num_matrices)
    
    times = {
        'Algoritmo iterativo cúbico tradicional': [],
        'Algoritmo con transposición': [],
        'Algoritmo de Strassen': [],
    }
    
    for i in range(0, len(matrices), 2):
        if i + 1 < 100:
            A = matrices[i]
            B = matrices[i + 1]
            
            start_time = time.time()
            multiplicacion_matrices_tradicional(A, B)
            end_time = time.time()
            times['Algoritmo iterativo cúbico tradicional'].append(end_time - start_time)
            
            start_time2 = time.time()
            matrix_returns(A, B)
            end_time2 = time.time()
            times['Algoritmo con transposición'].append(end_time2 - start_time2)
            
            start_time3 = time.time()
            strassen(A, B)
            end_time3 = time.time()
            times['Algoritmo de Strassen'].append(end_time3 - start_time3)
    
    avg_times = {algo: sum(times[algo]) / len(times[algo]) for algo in times}
    
    results = {
        'Algorithm': list(avg_times.keys()),
        'Average Time (s)': list(avg_times.values())
    }
    
    df = pd.DataFrame(results)
    return df


files = ['matriz_cuadrada.bin', 'matriz_rectangular.bin']

for file in files:
    base_name = os.path.splitext(file)[0]
    weird_name = base_name.replace('_', ' ')

    df = test_algorithms(file, 100)
    print(f"\nResults for {weird_name}:")
    print(df)
    df.plot(kind='bar', x='Algorithm', y='Average Time (s)', legend=False)
    plt.ylabel('Seconds')
    plt.title(f'Resultado promedio de algortimos de multiplicación de matrices con {weird_name}')
    plt.show()

files = ['matriz_grande.bin']
 
for file in files:
    base_name = os.path.splitext(file)[0]
    weird_name = base_name.replace('_', ' ')

    df = test_algorithms(file, 10)
    print(f"\nResults for {weird_name}:")
    print(df)
    df.plot(kind='bar', x='Algorithm', y='Average Time (s)', legend=False)
    plt.ylabel('Seconds')
    plt.title(f'Resultado promedio de algortimos de multiplicación de matrices con {weird_name}')
    plt.show()