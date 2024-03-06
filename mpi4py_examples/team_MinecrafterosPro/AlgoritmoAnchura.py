"""
Nombre del Módulo: Algoritmo en anchura
Autor: Roberto Vasquez Deniz, Jesus Isaac Estrada Ramirez, Haydee Josselyn Cortes Ubaldo
Fecha: 06 Marzo 2024
Descripción: 
    Este modulo contiene un algoritmo de anchura en ejecucion normal (no paralelizado)

Funciones:
    def agregar_vertice(self, vertice): agrega vertices al grafo
    def agregar_arista(self, vertice_origen, vertice_destino): Agrega una arista entre dos vértices
    def bfs(self, vertice_inicial): Método de búsqueda en anchura (BFS)


Clases:
    class Grafo: Instancia todo el programa
"""
# Importación de bibliotecas

# Definición de constantes

# Definición de funciones

# Clase de grafo
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

    def bfs(self, vertice_inicial):
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

    # Realizamos la búsqueda en anchura desde el vértice 'A'
    print("Recorrido en anchura (BFS):")
    grafo.bfs('A')
