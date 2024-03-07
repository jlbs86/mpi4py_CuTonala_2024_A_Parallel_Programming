"""Docstring: Tipos de Busqueda BFS y DFS """
from collections import deque
import time

class AlgBusqueda:
    """Clase para realizar búsqueda en grafos utilizando DFS y BFS."""

    def __init__(self, graph: dict, start: str, goal: str):
        """
        Inicializa la clase GraphSearch.

        Args:
            graph (dict): Grafo representado como un diccionario.
            start (str): Nodo de inicio.
            goal (str): Nodo objetivo.
        """
        self.graph = graph
        self.start = start
        self.goal = goal
    
    start_time = time.time()
    def bfs_method(self) -> list:
        """
        Realiza una búsqueda BFS en el grafo.

        Returns:
            list: Lista de nodos que forman el camino desde el nodo inicial al nodo objetivo.
        """

        
        visited = set()
        queue = deque([(self.start, [self.start])])

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            if current == self.goal:
                return path

            for neighbour in self.graph.get(current, []):
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))
                    

        return []
    
    time.sleep(1)
    end_time = time.time()
    print(f"Tiempo transcurrido para DFS: {end_time - start_time:.6f} segundos")

    def dfs_method(self) -> list:
        """
        Realiza una búsqueda DFS en el grafo.

        Returns:
            list: Lista de nodos que forman el camino desde el nodo inicial al nodo objetivo.
        """
        start_time = time.time()

        def dfs(current, path, visited):
            visited.add(current)
            if current == self.goal:
                return path

            for neighbour in self.graph.get(current, []):
                if neighbour not in visited:
                    result = dfs(neighbour, path + [neighbour], visited)
                    if result:  
                        
                        return result
            return []
        
        time.sleep(1)
        end_time = time.time()
        print(f"Tiempo transcurrido para DFS: {end_time - start_time:.6f} segundos")
        return dfs(self.start, [self.start], set())

if __name__ == "__main__":
    graph = {
        'S': ['A', 'D'],
        'A': [],
        'B': [],
        'C': [],
        'D': ['A', 'E'],
        'E': ['B', 'F'],
        'F': ['G'],
        'G': []
    }

    start = 'S'
    goal = 'G'

    search = AlgBusqueda(graph, start, goal)
    bfs_path = search.bfs_method()
    if bfs_path:
        print("Camino encontrado mediante BFS:", bfs_path)
    else:
        print("No se encontró un camino desde:", start, "a", goal)

    dfs_path = search.dfs_method()
    if dfs_path:
        print("Camino encontrado mediante DFS:", dfs_path)
    else:
        print("No se encontró un camino desde:", start, "a", goal)
        
