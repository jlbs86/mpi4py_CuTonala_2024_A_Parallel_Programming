
from collections import deque

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
        print("Camino encontrado mediante BFS:", path)
    else:
        print("No se encontró un camino desde", start, "a", goal)
        print(path)
