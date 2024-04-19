from collections import defaultdict, deque
import time


class GraphAlgorithms:
    """
    Clase para implementar algoritmos de búsqueda en grafos.
    """

    def __init__(self) -> None:
        """
        Inicializa un grafo vacío.
        """
        self.graph: defaultdict[list[int]] = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        """
        Agrega una arista entre los nodos u y v.

        Parámetros:
            u (int): Nodo de inicio de la arista.
            v (int): Nodo de fin de la arista.
        """
        self.graph[u].append(v)

    def dfs_method(self, start_node: int) -> None:
        """
        Realiza un recorrido DFS (Depth First Search) en el grafo.

        Parámetros:
            start_node (int): Nodo de inicio del recorrido DFS.
        """
        visited: set[int] = set()

        def dfs_util(node: int) -> None:
            visited.add(node)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        start_time: float = time.time()
        dfs_util(start_node)
        end_time: float = time.time()
        print("\nTiempo de ejecución del DFS:", end_time - start_time, 
"segundos")

    def bfs_method(self, start_node: int) -> None:
        """
        Realiza un recorrido BFS (Breadth First Search) en el grafo.

        Parámetros:
            start_node (int): Nodo de inicio del recorrido BFS.
        """
        visited: set[int] = set()
        queue: deque[int] = deque([start_node])
        visited.add(start_node)

        start_time: float = time.time()

        while queue:
            node: int = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        end_time: float = time.time()
        print("\nTiempo de ejecución del BFS:", end_time - start_time, 
"segundos")


# Ejemplo de uso
if __name__ == "__main__":
    graph = GraphAlgorithms()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Recorrido DFS comenzando desde el nodo 2:")
    graph.dfs_method(2)

    print("\nRecorrido BFS comenzando desde el nodo 2:")
    graph.bfs_method(2)

