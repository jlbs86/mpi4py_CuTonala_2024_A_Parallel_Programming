'''
DFS & BFS algorithms on python by:

1- Guillermo Bertrand Hernandez.
2- Erick Perez Coronado.
'''

from collections import deque
import time

class GraphSearchAlgorithms:
    
    def __init__(self, graph=None):
        self.graph = graph

    def dfs(self, start, visited=None):

        #Start measuring time
        self.startTime = time.time()

        if visited is None: visited = set()

        visited.add(start)
        print(start, " -> ", end='')

        for neighbor in self.graph[start] - visited:
            self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, " -> ", end='')

            for neighbor in self.graph[node] - visited:
                queue.append(neighbor)
                visited.add(neighbor)

    def setGraph(self, graph):
        self.graph = graph

if __name__ == "__main__":

    #Measure time.
    startTime = 0
    endTime = 0
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F', 'G'},
        'D': {'B'},
        'E': {'B'},
        'F': {'C'},
        'G': {'C'}
    }

    #Instantiate lexical analyzer
    graphSearch = GraphSearchAlgorithms(graph)

    startTime = time.time()
    print("DFS: ", end='')
    graphSearch.dfs('A')
    endTime = time.time()
    print("\nDFS execution time: ", (endTime - startTime)*1000, " miliseconds.")

    startTime = time.time()
    print("\nBFS: ", end='')
    graphSearch.bfs('A')
    endTime = time.time()
    print("\nBFS execution time: ", (endTime - startTime)*1000, " miliseconds.")
