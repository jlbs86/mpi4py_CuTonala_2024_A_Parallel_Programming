import time

def execution_time(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f'Tiempo de ejecución {funcion.__name__}: {fin - inicio} segundos')
        return resultado
    return wrapper

class Grafo:
    def __init__(self):
        self.vertices = {}

    def recorrido(self, vertice_inicial, metodo):
        visitados = set()
        estructura = [vertice_inicial] if metodo == 'bfs' else [vertice_inicial]

        while estructura:  # Add a base case to break the loop when empty
            vertice_actual = estructura.pop(0) if metodo == 'bfs' else estructura.pop()  # Use pop() for DFS
            if vertice_actual not in visitados:
                print(vertice_actual)
                visitados.add(vertice_actual)
                estructura.extend(self.vertices[vertice_actual]) if metodo == 'bfs' else estructura.extend(self.vertices[vertice_actual])


    def agregar_vertice(self, vertice):
        self.vertices.setdefault(vertice, [])

    def agregar_arista(self, vertice_origen, vertice_destino):
        self.vertices.setdefault(vertice_origen, []).append(vertice_destino)

   

    @execution_time
    def dfs_method(self, vertice_inicial):
        self.recorrido(vertice_inicial, 'dfs')

    @execution_time
    def bfs_method(self, vertice_inicial):
        self.recorrido(vertice_inicial, 'bfs')

if __name__ == "__main__":
    grafo = Grafo()

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('K', 'E'), ('C', 'F'), ('F', 'G'),
               ('G', 'H'), ('H', 'I'), ('H', 'J'), ('I', 'K')]

    for vertice in vertices:
        grafo.agregar_vertice(vertice)

    for arista in aristas:
        grafo.agregar_arista(*arista)

    print("Recorrido en profundidad (DFS):")
    grafo.dfs_method('A')

    print("\nRecorrido en anchura (BFS):")
    grafo.bfs_method('A')
