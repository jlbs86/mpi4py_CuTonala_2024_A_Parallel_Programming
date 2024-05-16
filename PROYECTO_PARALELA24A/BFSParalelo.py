from mpi4py import MPI
import time
import os

# Inicialización de MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Función BFS
def BFS(graph, frontier_nodes, bfs_tree, end_node):
    start_time = time.time()
    # Terminar cuando no haya más nodos en la frontera o se encuentre el nodo final
    if len(frontier_nodes) == 0 or any(node == end_node for node in frontier_nodes):
        end_time = time.time() #Tiempo de finalización
        execution_time = end_time - start_time #Calcular el tiempo de ejecución
        print(f"Rango: {rank}. Tiempo de ejecucion: {execution_time} segundos.")
        return bfs_tree
    else:
        # Obtener todos los vecinos de la frontera actual
        neighbors = graph[list(frontier_nodes)[0]]

        # Etiquetar los vecinos con el nodo del que provienen y aplanar
        next_nodes = {(ne, n): ne for n in frontier_nodes for ne in graph[n]}

        # Eliminar los vecinos que ya han sido explorados
        next_nodes = {ne for ne in next_nodes if bfs_tree.get(ne, -1) == -1}

        # Escribir en bfs_tree los punteros hacia atrás
        for ne, n in next_nodes:
            bfs_tree[ne] = n

        # Eliminar duplicados comprobando si ya se ha escrito
        next_nodes = {ne for ne, n in next_nodes if n not in bfs_tree or bfs_tree[n] != ne}

        # Recursión
        return BFS(graph, next_nodes, bfs_tree, end_node)   
# Función para obtener el camino de un nodo a su raíz en el árbol
def TREE_PATH(node, bfs_tree):
    if bfs_tree[node] == node:
        return [node]
    else:
        return [node] + TREE_PATH(bfs_tree[node], bfs_tree)

if rank == 0:
    # Grafo de ejemplo
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Nodo inicial y nodo final
    start_node = 'A'
    end_node = 'F'

    # Inicializar bfs_tree con el nodo inicial apuntando a sí mismo
    bfs_tree = {start_node: start_node}

    start_time = time.time()
    # Ejecutar BFS en el nodo raíz (nodo inicial)
    bfs_tree = BFS(graph, {start_node}, bfs_tree, end_node)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Rango:{rank}. Tiempo de ejecucion: {execution_time} segundos.")
    # Imprimir el árbol BFS resultante
    print("BFS Tree:", bfs_tree)

# Sincronizar todos los procesos antes de finalizar
comm.Barrier()

print(f"Rango actual: {rank} de total de procesos: {size}")