"""Docstring: Busqueda a profundidad """

class BusProfundidad:
    """Docstring: """
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

if __name__ == "__main__":
    g = BusProfundidad(8)
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

    print("primer recorrido en profundidad (recursivo):", end=' ')
    g.DFSTraverse()
    print()


