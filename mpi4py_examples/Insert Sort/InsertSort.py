#########    Algoritmo de Insert Sort   ###############
##
##
##              Autor: Martinez Pérez Marco Uriel

import time

"""
Docstring: Algoritmo InsertSort

Returns:
        list: Lista de valores ordenados
        
"""

inicio = time.time()  # Guarda el tiempo de inicio

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]  # Guarda el valor actual a insertar
        position = i
        
        # Mueve los elementos del subarreglo ordenado hacia la derecha
        # para hacer espacio para el valor actual
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Inserta el valor actual en la posición correcta
        arr[position] = current_value
        

# Ejemplo de Arreglo
arr = [5, 2, 4, 6, 1, 3, 8, 10, 32, 7, 1, 20, 9, 12]
print("Lista original:", arr)

insertion_sort(arr)
print("Lista ordenada:", arr)

time.sleep(1)
fin = time.time()  # Guarda el tiempo de finalización
tiempo_ejecucion = fin - inicio  # Calcula el tiempo de ejecución
print(f"Tiempo de ejecución: {tiempo_ejecucion:.8f} segundos")
