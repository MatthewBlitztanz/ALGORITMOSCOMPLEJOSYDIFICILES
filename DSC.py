import random
import numpy as np

def generar_datos_aleatorios(tamaño):
    """
    Genera una lista de números aleatorios entre 0 y 1000.

    Parámetros:
    tamaño (int): El número de elementos en la lista.

    Retorna:
    list: Una lista de números aleatorios.
    """
    if tamaño <= 0:
        raise ValueError("El tamaño debe ser un número positivo.")
    
    random.seed(42)
    return [random.randint(0, 1000) for _ in range(tamaño)]

def generar_datos_semi_ordenados(tamaño):
    """
    Genera una lista de datos semi ordenados, desordenando el 10% de los datos.

    Parámetros:
    tamaño (int): El número de elementos en la lista.

    Retorna:
    list: Una lista de datos semi ordenados.
    """
    datos = list(range(tamaño))
    for _ in range(tamaño // 10):
        i, j = random.sample(range(tamaño), 2)
        datos[i], datos[j] = datos[j], datos[i]
    return datos

def generar_datos_parcialmente_ordenados(tamaño):
    """
    Genera una lista de datos parcialmente ordenados, desordenando el 10% de la primera mitad.

    Parámetros:
    tamaño (int): El número de elementos en la lista.

    Retorna:
    list: Una lista de datos parcialmente ordenados.
    """
    datos = list(range(tamaño // 2)) + list(random.sample(range(tamaño // 2, tamaño), tamaño // 2))

    return datos

def generar_datos_invertidos(tamaño):
    """
    Genera una lista de números en orden descendente (invertidos).
    
    Parámetros:
    tamaño (int): El número de elementos en la lista.
    
    Retorna:
    list: Una lista de números en orden descendente.
    """
    if tamaño <= 0:
        raise ValueError("El tamaño debe ser un número positivo.")
    
    return list(range(tamaño, 0, -1))

def generar_matrices_cuadradas(n, tamaño):
    """
    Genera n matrices cuadradas aleatorias de tamaño especificado.

    Parámetros:
    n (int): Número de matrices a generar.
    tamaño (int): Tamaño de las matrices (tamaño x tamaño).

    Retorna:
    list: Una lista de matrices cuadradas.
    """
    matrices = [np.random.randint(0, 1000, size=(tamaño, tamaño)) for _ in range(n)]
    return matrices

def generar_matriz_rectangular(n, max_dim, min_dim):
    """
    Genera n matrices rectangulares aleatorias de tamaño especificado, con dimensiones al menos min_dim.

    Parámetros:
    n (int): Número de matrices a generar.
    max_dim (int): Tamaño máximo de las matrices (filas x columnas).
    min_dim (int): Tamaño mínimo de las matrices (filas x columnas).

    Retorna:
    list: Una lista de matrices rectangulares.
    """
    matrices = []
    for _ in range(n):
        filas_A = random.randint(min_dim, max_dim)
        columnas_A = random.randint(min_dim, max_dim)
        filas_B = columnas_A 
        columnas_B = random.randint(min_dim, max_dim)
        
        A = np.random.randint(0, 1000, size=(filas_A, columnas_A))
        B = np.random.randint(0, 1000, size=(filas_B, columnas_B))
        
        matrices.append((A, B))
    return matrices

def guardar_en_archivo(datos, nombre_archivo):
    """
    Guarda una lista de datos en un archivo de texto.

    Parámetros:
    datos (list): La lista de datos a guardar.
    nombre_archivo (str): El nombre del archivo donde se guardarán los datos.
    """
    with open(nombre_archivo, 'w') as f:
        for dato in datos:
            f.write(f"{dato}\n")

def guardar_matrices_bin(matrices, nombre_archivo):
    """
    Guarda una lista de matrices en un archivo binario.

    Parámetros:
    matrices (list): Lista de matrices a guardar.
    nombre_archivo (str): Nombre del archivo binario.
    """
    with open(nombre_archivo, 'wb') as f:
        for matriz in matrices:
            np.save(f, matriz)

# Generar y guardar datos aleatorios
datos_aleatorios = generar_datos_aleatorios(10000)
guardar_en_archivo(datos_aleatorios, 'datos_aleatorios.txt')

# Generar y guardar datos semi ordenados
datos_semi_ordenados = generar_datos_semi_ordenados(10000)
guardar_en_archivo(datos_semi_ordenados, 'datos_semi_ordenados.txt')

# Generar y guardar datos parcialmente ordenados
datos_parcialmente_ordenados = generar_datos_parcialmente_ordenados(10000)
guardar_en_archivo(datos_parcialmente_ordenados, 'datos_parcialmente_ordenados.txt')

# Generar y guardar datos invertidos
datos_invertidos = generar_datos_invertidos(10000)
guardar_en_archivo(datos_invertidos, 'datos_invertidos.txt')

# Generar y guardar matriz cuadrada
matrices = generar_matrices_cuadradas(100, 128)
guardar_matrices_bin(matrices, 'matriz_cuadrada.bin')

# Generar y guardar matriz rectangular
matrices2 = generar_matriz_rectangular(100, 128, 64)
guardar_matrices_bin(matrices, 'matriz_rectangular.bin')

# Generar y guardar matriz de 512x512
matriz_grande = generar_matrices_cuadradas(10, 512)
guardar_matrices_bin(matriz_grande, 'matriz_grande.bin')