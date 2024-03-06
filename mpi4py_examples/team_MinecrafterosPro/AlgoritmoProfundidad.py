"""
Nombre del Módulo: Algoritmo en profundidad
Autor: Roberto Vasquez Deniz, Jesus Isaac Estrada Ramirez, Haydee Josselyn Cortes Ubaldo
Fecha: 06 Marzo 2024
Descripción: 
    Este modulo contiene un algoritmo de profundidad en ejecucion normal (no paralelizado)

Funciones:
    def __init__(self): inicializa el grafo
    def agregar_vertice(self, vertice): agrega vertices al grafo
    def agregar_arista(self, vertice_origen, vertice_destino): Agrega una arista entre dos vértices
    def dfs(self, vertice_inicial): Método de búsqueda en profundidad (DFS)


Clases:
    class Grafo: Instancia todo el programa
"""
# Importación de bibliotecas

# Definición de constantes

# Definición de funciones

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
 
    def dfs(self, vertice_inicial): 
        visitados = set()

        def dfs_recursivo(vertice):
            visitados.add(vertice)
            print(vertice)

            for vecino in self.vertices[vertice]:
                if vecino not in visitados:
                    dfs_recursivo(vecino)

        dfs_recursivo(vertice_inicial)

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

    # Agregamos las aristas
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('B', 'E')
    grafo.agregar_arista('C', 'F')

    # Realizamos la búsqueda en profundidad desde el vértice 'A'
    print("Recorrido en profundidad (DFS):")
    grafo.dfs('A')
