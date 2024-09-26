# bfs_dfs_algorithms.py

import time

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_method(self, start):
        start_time = time.time()
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(f"DFS visiting node {node}")
                visited.add(node)
                stack.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)
        time.sleep(1)
        end_time = time.time()
        print(f"BFS execution time: {end_time - start_time:.6f} seconds")        

    def bfs_method(self, start):
        start_time = time.time()
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(f"BFS visiting node {node}")
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)
        time.sleep(1)        
        end_time = time.time()
        print(f"BFS execution time: {end_time - start_time:.6f} seconds")        

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Resultado DFS: ")
    g.dfs_method(2)
    print("Resultado BFS: ")
    g.bfs_method(2)
    
