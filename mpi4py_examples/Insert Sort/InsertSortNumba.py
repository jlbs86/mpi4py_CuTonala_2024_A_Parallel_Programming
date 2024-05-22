#########    Algoritmo de Insert Sort implementando NUMBA   ###############
##
##
##              Autor: Martinez Pérez Marco Uriel

from numba import njit
import numpy as np
import time

@njit
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

# Función para dividir el arreglo en partes iguales
def split_array(arr, size):
    n = len(arr)
    part_size = n // size
    remainder = n % size
    send_counts = [part_size + 1 if i < remainder else part_size for i in range(size)]
    displacements = [sum(send_counts[:i]) for i in range(size)]
    return [arr[displacements[i]:displacements[i] + send_counts[i]] for i in range(size)]

# Función para fusionar dos partes ordenadas
@njit
def merge_two_sorted_arrays(arr1, arr2):
    sorted_arr = np.empty(len(arr1) + len(arr2), dtype=arr1.dtype)
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr[k] = arr1[i]
            i += 1
        else:
            sorted_arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        sorted_arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        sorted_arr[k] = arr2[j]
        j += 1
        k += 1

    return sorted_arr

# Función para unir las partes ordenadas
def merge_sorted_parts(sorted_parts):
    while len(sorted_parts) > 1:
        new_sorted_parts = []
        for i in range(0, len(sorted_parts), 2):
            if i + 1 < len(sorted_parts):
                merged_part = merge_two_sorted_arrays(sorted_parts[i], sorted_parts[i + 1])
                new_sorted_parts.append(merged_part)
            else:
                new_sorted_parts.append(sorted_parts[i])
        sorted_parts = new_sorted_parts
    return sorted_parts[0]

if __name__ == "__main__":
    arr = np.array([5, 2, 4, 6, 1, 3, 8, 10, 32, 7, 1, 20, 9, 12], dtype=np.int32)
    size = 4  # Número de partes en las que se dividirá el arreglo

    start_time = time.time()  # Registrar el tiempo de inicio

    # Dividir el arreglo en partes iguales
    parts = split_array(arr, size)

    # Ordenar cada parte localmente usando Numba
    for part in parts:
        insertion_sort(part)

    # Unir partes ordenadas
    sorted_arr = merge_sorted_parts(parts)

    end_time = time.time()  # Registrar el tiempo de finalización

    print("Lista original:", arr)
    print("Lista ordenada:", sorted_arr)
    print(f"Tiempo de ejecución: {end_time - start_time:.8f} segundos")