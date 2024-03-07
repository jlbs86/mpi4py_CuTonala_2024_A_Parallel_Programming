"""Programa en python para algotimos de 
de busqueda por amplitud (bfs) y por 
profundidad (dfs)"""

from collections import defaultdict

"""Esta clase reprenta un grafo dirigido
que hace uso de la representación de listas
de adyacencia"""

class grafo:
    #Constructor
    def __init__(self):
        #Diccionario default que almacenara los elementos del grafo
        self.grafo = defaultdict(list)

    def vertices(self, u, v):
        self.grafo[u].append(v)
     
    def BFS (self, s):
        #Marca todos los vertices como no visitados
        visited = [False]*(max(self.grafo)+1)
        #Creación de una cola:
        cola = []

        """Marca ell nodo de origen como vistado
        y lo añade a la cola:"""
        cola.append(s)
        visited[s] = True

        while cola:
            #Se elimina un vertice de la cola y se imprime
            s = cola.pop(0)
            print(s, end='')