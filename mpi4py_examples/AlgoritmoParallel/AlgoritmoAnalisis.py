import time


start_time = time.time()
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir el array en mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Ordenar recursivamente cada mitad
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinar las mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_pointer, right_pointer = 0, 0

    # Combinar las mitades ordenadas
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            merged.append(left[left_pointer])
            left_pointer += 1
        else:
            merged.append(right[right_pointer])
            right_pointer += 1

    # Agregar los elementos restantes de left (si hay alguno)
    while left_pointer < len(left):
        merged.append(left[left_pointer])
        left_pointer += 1

    # Agregar los elementos restantes de right (si hay alguno)
    while right_pointer < len(right):
        merged.append(right[right_pointer])
        right_pointer += 1

    return merged

if __name__ == "__main__":
    array = [12, 7, 3, 9, 5, 6, 8, 1]
    
    # Medir el tiempo de ejecución
    sorted_array = merge_sort(array)
    time.sleep(1)
    end_time = time.time()

    print("Array ordenado:", sorted_array)
    print("Tiempo de ejecución:", end_time - start_time, "segundos")
