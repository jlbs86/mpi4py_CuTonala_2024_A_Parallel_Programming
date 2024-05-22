"""Docstring: Tipos de Busqueda BFS y DFS """
from collections import deque
import time

"""Docstring: Metodo BFS

Returns:
        list: Lista de nodos que forman el camino desde el nodo inicial al nodo objetivo.
"""
iniciobfs = time.time()
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == goal:
            return path

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))
time.sleep(1)
finbfs = time.time()                
               
"""Docstring: Metodo DFS

Returns:
    list: Lista de nodos que forman el camino desde el nodo inicial al nodo objetivo.
"""                
iniciodfs = time.time() 
class BusDFS:
    def __init__(self, n):
        self.vexnum = n
        self.vertices = [''] * n
        self.arcs = [[0] * n for _ in range(n)]
        self.visited = [False] * n

    def addEdge(self, i, j):
        if i == j:
            return
        self.arcs[i][j] = 1
        self.arcs[j][i] = 1

    def setVertices(self, vertices):
        self.vertices = vertices

    def setVisited(self, visited):
        self.visited = visited

    def visit(self, i):
        print(self.vertices[i], end=' ')

    def traverse(self, i):
        self.visited[i] = True
        self.visit(i)
        for j in range(self.vexnum):
            if self.arcs[i][j] == 1 and not self.visited[j]:
                self.traverse(j)

    def DFSTraverse(self):
        for i in range(self.vexnum):
            self.visited[i] = False
        for i in range(self.vexnum):
            if not self.visited[i]:
                self.traverse(i)
time.sleep(1)
findfs = time.time()                


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
    
    path = bfs(graph, start, goal)
    if path:
        print("Camino encontrado mediante BFS: ", path)
        tiempo_transcurrido = finbfs - iniciobfs
        print(f"Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")
    else:
        print("No se encontró un camino desde: ", start, " a ", goal)
        tiempo_transcurrido = finbfs - iniciobfs
        print(f"Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")
    
if __name__ == "__main__":
    g = BusDFS(8)
    vertices = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    g.setVertices(vertices)

    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(5, 2)
    g.addEdge(5, 4)
    g.addEdge(5, 6)
    g.addEdge(6, 5)
    g.addEdge(6, 7)
    g.addEdge(4, 1)
    g.addEdge(4, 5)
    g.addEdge(5, 4)
    g.addEdge(5, 2)
    g.addEdge(5, 6)
    g.addEdge(2, 5)
    g.addEdge(2, 3)
    g.addEdge(6, 5)
    g.addEdge(6, 7)

    print("primer recorrido en profundidad DFS:", end=' ')
    g.DFSTraverse()
    print()
    tiempo_transcurrido = findfs - iniciodfs
    print(f"Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")
    

    
