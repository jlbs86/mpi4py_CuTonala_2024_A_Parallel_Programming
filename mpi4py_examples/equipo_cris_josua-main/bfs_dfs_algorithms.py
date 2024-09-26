import time
from collections import deque


class GraphSearch:
    """
    Clase para realizar búsquedas en grafos.
    """

    def __init__(self, graph):
        
        self.graph = graph

    def dfs_method(self, start_node):
        """
        Realiza una búsqueda en profundidad (DFS) a partir del nodo inicial dado.
        """
        visited = set()
        result = []

        def dfs_helper(node):
            nonlocal visited
            nonlocal result
            visited.add(node)
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        start_time = time.time()
        dfs_helper(start_node)
        end_time = time.time()
        print(f"Tiempo de ejecución DFS: {end_time - start_time} segundos")
        return result

    def bfs_method(self, start_node):
        """
        Realiza una búsqueda en anchura (BFS) a partir del nodo inicial dado.
        """
        visited = set()
        result = []
        queue = deque([start_node])

        start_time = time.time()
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        end_time = time.time()
        print(f"Tiempo de ejecución BFS: {end_time - start_time} segundos")
        return result


    #clase GraphSearch
if __name__ == "__main__":
    # Grafo  (lista de adyacencia)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Crear objeto GraphSearch
    search = GraphSearch(graph)

    # Realizar búsqueda DFS desde el nodo 'A'
    dfs_result = search.dfs_method('A')
    print("DFS Result:", dfs_result)

    # Realizar búsqueda BFS desde el nodo 'A'
    bfs_result = search.bfs_method('A')
    print("BFS Result:", bfs_result)
