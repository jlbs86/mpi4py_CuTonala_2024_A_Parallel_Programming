"""Programa en python para algotimos de 
de busqueda por amplitud (bfs) y por 
profundidad (dfs)"""

from collections import defaultdict
import time

"""Esta clase reprenta un grafo dirigido
que hace uso de la representación de listas
de adyacencia"""

class Graph:
    def __init__(self):
        # Utilizamos defaultdict para crear una lista de adyacencia
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Función para agregar una arista al grafo
        self.graph[u].append(v)

    def bfs(self, s):
        # Función para recorrido BFS (Breadth First Search)
        visited = [False] * (len(self.graph))  # Marcamos todos los vértices como no visitados
        queue = []  # Inicializamos una cola para el BFS

        visited[s] = True  # Marcamos el vértice inicial como visitado
        queue.append(s)  # Añadimos el vértice inicial a la cola

        start_time = time.time()  # Medimos el tiempo de inicio del algoritmo

        while queue:  # Mientras la cola no esté vacía
            s = queue.pop(0)  # Obtenemos el primer elemento de la cola
            print(s, end=" ")  # Imprimimos el vértice actual

            # Recorremos todos los vértices adyacentes al vértice actual
            for i in self.graph[s]:
                if not visited[i]:  # Si el vértice adyacente no ha sido visitado
                    visited[i] = True  # Marcamos el vértice como visitado
                    queue.append(i)  # Añadimos el vértice a la cola

        end_time = time.time()  # Medimos el tiempo de finalización del algoritmo
        print("\nTiempo de ejecución de BFS: {:.10} segundos".format(end_time - start_time))

    def dfs_util(self, v, visited):
        # Función de utilidad para el recorrido DFS (Depth First Search)
        visited[v] = True  # Marcamos el vértice actual como visitado
        print(v, end=" ")  # Imprimimos el vértice actual

        # Recorremos todos los vértices adyacentes al vértice actual
        for i in self.graph[v]:
            if not visited[i]:  # Si el vértice adyacente no ha sido visitado
                self.dfs_util(i, visited)  # Llamamos recursivamente a la función DFS_util

    def dfs(self):
        # Función para recorrido DFS
        visited = [False] * (len(self.graph))  # Marcamos todos los vértices como no visitados
        start_time = time.time()  # Medimos el tiempo de inicio del algoritmo
        for i in range(len(self.graph)):
            if not visited[i]:  # Si el vértice no ha sido visitado
                self.dfs_util(i, visited)  # Llamamos a la función de utilidad DFS_util
        end_time = time.time()  # Medimos el tiempo de finalización del algoritmo
        print("\nTiempo de ejecución de DFS: {:.10f} segundos".format(end_time - start_time))

# Grafo utilizado para BFS
g_bfs = Graph()
g_bfs.add_edge(0, 1)
g_bfs.add_edge(0, 2)
g_bfs.add_edge(1, 2)
g_bfs.add_edge(2, 0)
g_bfs.add_edge(2, 3)
g_bfs.add_edge(3, 5)
g_bfs.add_edge(3, 3)
g_bfs.add_edge(3, 4)
g_bfs.add_edge(4, 2)
g_bfs.add_edge(4, 4)
g_bfs.add_edge(4, 5)
g_bfs.add_edge(5, 1)
g_bfs.add_edge(5, 5)
print("Recorrido de la búsqueda por anchura:")
g_bfs.bfs(5)  # Realizamos el recorrido BFS empezando desde el vértice 5
print("\n")

# Grafo para DFS
g_dfs = Graph()
g_dfs.add_edge(0, 1)
g_dfs.add_edge(0, 2)
g_dfs.add_edge(1, 1)
g_dfs.add_edge(1, 2)
g_dfs.add_edge(2, 2)
g_dfs.add_edge(2, 3)
g_dfs.add_edge(3, 3)
g_dfs.add_edge(3, 4)
g_dfs.add_edge(4, 3)
g_dfs.add_edge(4, 4)
g_dfs.add_edge(4, 5)
g_dfs.add_edge(5, 4)
g_dfs.add_edge(5, 5)
print("El recorrido a profundidad es el siguiente:")
g_dfs.dfs()  # Realizamos el recorrido DFS