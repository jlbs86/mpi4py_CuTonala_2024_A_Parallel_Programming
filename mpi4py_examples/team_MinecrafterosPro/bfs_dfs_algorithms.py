"""
Nombre del Módulo: Algoritmos BFS Y DFS
Autor: Roberto Vasquez Deniz, Jesus Isaac Estrada Ramirez, Haydee Josselyn Cortes Ubaldo
Fecha: 06 Marzo 2024
Descripción: 
    Este modulo contiene un algoritmo de profundidad en ejecucion normal (no paralelizado)

Funciones:
    def __init__(self): inicializa el grafo
    def agregar_vertice(self, vertice): agrega vertices al grafo
    def agregar_arista(self, vertice_origen, vertice_destino): Agrega una arista entre dos vértices
    def dfs(self, vertice_inicial): Método de búsqueda en profundidad (DFS)
    def bfs(self, vertice_inicial): Método de búsqueda en anchura (BFS)
    def execution_time(funcion, *args, **kwargs): calcula el tiempo de ejecucion de la funcion


Clases:
    class Grafo: Instancia todo el programa
"""
# Importación de bibliotecas
import time

# Definición de constantes

# Definición de funciones
def execution_time(funcion, *args, **kwargs):
    inicio = time.time()
    funcion(*args, **kwargs)
    fin = time.time()
    print(f'Tiempo de ejecución {funcion.__name__}: {fin - inicio} segundos')

# Clase de Grafo
class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice_origen, vertice_destino):
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            self.vertices[vertice_origen].append(vertice_destino)
        else:
            print("Vertice origen o destino no encontrado.")
 
    def dfs_method(self, vertice_inicial): 
        visitados = set()

        def dfs_recursivo(vertice):
            visitados.add(vertice)
            print(vertice)

            for vecino in self.vertices[vertice]:
                if vecino not in visitados:
                    dfs_recursivo(vecino)

        dfs_recursivo(vertice_inicial)
    
    def bfs_method(self, vertice_inicial):
        visitados = set()
        cola = [vertice_inicial]

        while cola:
            vertice_actual = cola.pop(0)
            if vertice_actual not in visitados:
                print(vertice_actual)
                visitados.add(vertice_actual)
                for vecino in self.vertices[vertice_actual]:
                    if vecino not in visitados:
                        cola.append(vecino) 

# Código principal
if __name__ == "__main__":
    # Se inicializa el grafo
    grafo = Grafo()

    # Agregamos los vértices
    grafo.agregar_vertice('A')
    grafo.agregar_vertice('B')
    grafo.agregar_vertice('C')
    grafo.agregar_vertice('D')
    grafo.agregar_vertice('E')
    grafo.agregar_vertice('F')
    grafo.agregar_vertice('G')
    grafo.agregar_vertice('H')
    grafo.agregar_vertice('I')
    grafo.agregar_vertice('J')
    grafo.agregar_vertice('K')


    # Agregamos las aristas
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('K', 'E')
    grafo.agregar_arista('C', 'F')
    grafo.agregar_arista('F', 'G')
    grafo.agregar_arista('G', 'H')
    grafo.agregar_arista('H', 'I')
    grafo.agregar_arista('H', 'J')
    grafo.agregar_arista('I', 'K')

    # Realizamos la búsqueda en profundidad desde el vértice 'A'
    print("Recorrido en profundidad (DFS):")
    execution_time(grafo.dfs_method, 'A')
    
    
    print("\nRecorrido en anchura (BFS):")
    execution_time(grafo.bfs_method,'A')
    
