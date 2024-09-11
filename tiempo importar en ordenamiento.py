import time

import pandas as pd
import matplotlib.pyplot as plt

import os

import sys

sys.setrecursionlimit(15000)

'''

Decidí no usar comentarios en estas funciones ya que hay un codigo para cada una de ellas donde tienen su propio comentario.

Además así se mantiene un poco el orden en este codigo donde hay varias funciones y algoritmos.

'''

def insertion_sort(arr):

    if len(arr) <= 1:
        return
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
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

    if l < r:
 
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quicksort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)

        quicksort(arr, pi + 1, high)


def leer_desde_archivo(nombre_archivo):

    with open(nombre_archivo, 'r') as f:
        datos = [int(line.strip()) for line in f]

    return datos


def measure_time(func, *args):
    """
    Mide el tiempo de ejecución de una función específica.

    Parámetros:
    func (function): La función a la que se le medirá el tiempo de ejecución.
    *args: Los argumentos a pasar a la función.

    Retorna:
    float: El tiempo que tardó en ejecutarse la función en segundos.
    """
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time


def test_algorithms(file_name):
    """
    Prueba los algoritmos de ordenamiento Insertion Sort, Merge Sort, Quick Sort y el método sort() de Python,
    midiendo el tiempo promedio de ejecución para cada algoritmo en un dataset específico.

    Parámetros:
    file_name (str): El nombre del archivo que contiene el dataset a ordenar.

    Retorna:
    pd.DataFrame: Un DataFrame con el nombre de los algoritmos y sus respectivos tiempos promedio de ejecución.
    """
    datos = leer_desde_archivo(file_name)
    n = len(datos)
    
    times = {
        'Insertion Sort': [],
        'Merge Sort': [],
        'Quick Sort': [],
        'Sort() Python': []
    }
    
    for _ in range(100):
        data_copy = datos.copy()
        times['Insertion Sort'].append(measure_time(insertion_sort, data_copy))
        
        data_copy = datos.copy()
        start_time = time.time()
        mergeSort(data_copy, 0, n - 1)
        end_time = time.time()
        times['Merge Sort'].append(end_time - start_time)
        
        data_copy = datos.copy()
        start_time2 = time.time()
        quicksort(data_copy, 0, n - 1)
        end_time2 = time.time()
        times['Quick Sort'].append(end_time2 - start_time2)
        
        data_copy = datos.copy()
        start_time3 = time.time()
        data_copy.sort()
        end_time3 = time.time()
        times['Sort() Python'].append(end_time3 - start_time3)
    
    avg_times = {algo: sum(times[algo]) / len(times[algo]) for algo in times}
    
    results = {
        'Algorithm': list(avg_times.keys()),
        'Average Time (s)': list(avg_times.values())
    }
    
    df = pd.DataFrame(results)
    return df

files = ['datos_aleatorios.txt', 'datos_parcialmente_ordenados.txt', 'datos_semi_ordenados.txt', 'datos_invertidos.txt']

for file in files:
    base_name = os.path.splitext(file)[0]
    weird_name = base_name.replace('_', ' ')

    df = test_algorithms(file)
    print(f"\nResults for {weird_name}:")
    print(df)
    df.plot(kind='bar', x='Algorithm', y='Average Time (s)', legend=False)
    plt.ylabel('Seconds')
    plt.title(f'Resultado promedio de algortimos de ordenamiento con {weird_name}')
    plt.show()