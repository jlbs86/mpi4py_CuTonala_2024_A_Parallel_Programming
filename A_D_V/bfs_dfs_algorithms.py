"""
================================
algorithms implementation
================================

Ejemplo de Algoritmos DFS Y BFS usando el mismo grafo para los ejemplos,
uso de la libreria time para obtener el tiempo de ejecución,
EJECUTAR python bfs_dfs_algorithms.py

"""

import time
#!ALGORITMO 1 DFS (Depth-First Search)
def dfs_method(grafo, nodo_inicial):
    """
    Realiza una búsqueda en profundidad iterativa en un grafo.

    Parámetros:
      grafo: Un diccionario que representa el grafo.
      nodo_inicial: El nodo inicial a explorar.
    """
    pila = [nodo_inicial]
    visitados = set()

    start_time = time.time()  # Obtener el tiempo inicial

    while pila:
        # Sacar el último nodo de la pila
        nodo_actual = pila.pop()

        # Si el nodo no ha sido visitado, procesarlo
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            print(nodo_actual)

            # Añadir los nodos adyacentes no visitados a la pila
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    pila.append(vecino)

    end_time = time.time()  # Obtener el tiempo final
    print("Tiempo de ejecución:", end_time - start_time)  # Imprimir el tiempo de ejecución

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido DFS:")
dfs_method(grafo, "A")


#!Algoritmo 2 BFS (Breadth First Search)
def bfs(graph, start, visited=None):
    """
    Realiza una búsqueda por anchura en un grafo.

    Parámetros:
      graph: Un diccionario que representa el grafo.
      start: El nodo inicial a explorar.
      visited: Un conjunto opcional para guardar los nodos ya visitados (predeterminado a `None`).
    """
    if visited is None:
        visited = set()

    # Cola para almacenar los nodos a explorar
    queue = [start]

    start_time = time.time()  # Obtener el tiempo inicial

    while queue:
        # Sacar el primer nodo de la cola
        node = queue.pop(0)

        # Si el nodo no ha sido visitado, procesarlo
        if node not in visited:
            visited.add(node)
            print(node)

            # Añadir los nodos adyacentes a la cola
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    end_time = time.time()  # Obtener el tiempo final
    print("Tiempo de ejecución:", end_time - start_time)  # Imprimir el tiempo de ejecución

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido BFS:")
bfs(graph, 'A')