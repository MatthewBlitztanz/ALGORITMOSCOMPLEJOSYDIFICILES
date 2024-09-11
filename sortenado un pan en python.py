def leer_desde_archivo(nombre_archivo):
    """
    Lee una lista de datos desde un archivo de texto.

    Parámetros:
    nombre_archivo (str): El nombre del archivo desde el cual leer los datos.

    Retorna:
    list: Una lista de datos leídos del archivo.
    """
    with open(nombre_archivo, 'r') as f:
        datos = [int(line.strip()) for line in f]

    return datos


datos_aleatorios_leidos = leer_desde_archivo('datos_aleatorios.txt') ##Es posible cambiar el texto para usar cualquier lista de datos preferidad :D

datos_aleatorios_leidos.sort()

print(datos_aleatorios_leidos)