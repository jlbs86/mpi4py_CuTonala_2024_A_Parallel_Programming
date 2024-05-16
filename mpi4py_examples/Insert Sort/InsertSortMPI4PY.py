from mpi4py import MPI

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

# Función para dividir el arreglo en partes iguales
def split_array(arr, size):
    n = len(arr)
    part_size = n // size
    remainder = n % size
    send_counts = [part_size + 1 if i < remainder else part_size for i in range(size)]
    displacements = [sum(send_counts[:i]) for i in range(size)]
    return [arr[displacements[i]:displacements[i] + send_counts[i]] for i in range(size)]

# Función para unir las partes ordenadas
def merge_sorted_parts(sorted_parts):
    return sorted(sum(sorted_parts, []))

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        arr = [5, 2, 4, 6, 1, 3]
    else:
        arr = None

    # Dividir el arreglo en partes iguales
    arr_part = comm.scatter(split_array(arr, size), root=0)

    # Ordenar la parte local
    insertion_sort(arr_part)

    # Recopilar partes ordenadas
    sorted_parts = comm.gather(arr_part, root=0)

    # Unir partes ordenadas
    if rank == 0:
        sorted_arr = merge_sorted_parts(sorted_parts)
        print("Lista original:", arr)
        print("Lista ordenada:", sorted_arr)