# -*- coding: utf-8 -*-
"""Ambos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vhVzU_dWVlF5_qJeP694FZGwIRBFUNR3
"""

# -*- coding: utf-8 -*-
"""
======================================
Algoritmos de búsqueda en grafos: DFS y BFS
======================================

Este programa implementa los algoritmos de búsqueda en grafos: DFS (Depth-First Search)
y BFS (Breadth-First Search).

DFS (Búsqueda en Profundidad):
    - Visita un nodo y luego explora lo más profundo posible a lo largo de cada rama antes de retroceder.
    - Utiliza una pila (o recursión) para llevar un seguimiento de los nodos a visitar.

BFS (Búsqueda en Anchura):
    - Visita todos los vecinos de un nodo antes de avanzar a los vecinos de los vecinos.
    - Utiliza una cola para llevar un seguimiento de los nodos a visitar.

Uso:
    - Ejecuta el script para ver los resultados de los recorridos DFS y BFS en el grafo proporcionado.

Formato de docstring de Sphinx:

'''[Resumen]

:param [NombreParámetro]: [DescripciónParámetro], por defecto [ValorParámetroPredeterminado]
:type [NombreParámetro]: [TipoParámetro](, opcional)
...
:raises [TipoError]: [DescripciónError]
...
:return: [DescripciónRetorno]
:rtype: [TipoRetorno]
''''
"""

from typing import List, Dict, Set
import time


class Graph:
    def __init__(self):
        # Inicializa el grafo como un diccionario vacío
        self.graph = {}

    def add_edge(self, u, v):
        # Agrega una arista entre los nodos u y v al grafo
        if u not in self.graph:
            # Si el nodo u no está en el grafo, crea una lista vacía para almacenar sus vecinos
            self.graph[u] = []
        # Agrega v a la lista de vecinos del nodo u
        self.graph[u].append(v)

    def dfs_method(self, start):
        # Realiza un recorrido en profundidad (DFS) desde el nodo de inicio
        visited = set()  # Conjunto para mantener un registro de nodos visitados

        def dfs(node):
            # Función interna para realizar la búsqueda DFS recursivamente
            if node not in visited:
                # Si el nodo actual no ha sido visitado, lo imprime y lo marca como visitado
                print(node)
                visited.add(node)
                # Para cada vecino del nodo actual, realiza una llamada recursiva a dfs
                for neighbor in self.graph.get(node, []):
                    dfs(neighbor)

        # Llama a la función dfs con el nodo de inicio
        dfs(start)

    def bfs_method(self, start):
        # Realiza un recorrido en anchura (BFS) desde el nodo de inicio
        visited = set()  # Conjunto para mantener un registro de nodos visitados
        queue = [start]  # Cola para almacenar los nodos que se visitarán

        while queue:
            # Mientras la cola no esté vacía
            node = queue.pop(0)  # Extrae el primer elemento de la cola
            if node not in visited:
                # Si el nodo actual no ha sido visitado, lo imprime y lo marca como visitado
                print(node)
                visited.add(node)
                # Agrega todos los vecinos del nodo actual a la cola
                queue.extend(self.graph.get(node, []))

# Creación del grafo con 15 nodos
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(3, 8)
g.add_edge(4, 9)
g.add_edge(5, 10)
g.add_edge(6, 11)
g.add_edge(7, 12)
g.add_edge(8, 13)
g.add_edge(9, 14)
g.add_edge(10, 15)

# Medir el tiempo de ejecución de DFS
print("DFS:")
start_time_dfs = time.time()
g.dfs_method(1)
end_time_dfs = time.time()
execution_time_dfs = end_time_dfs - start_time_dfs
print("Tiempo de ejecución de DFS:", execution_time_dfs)
print(" ")

# Medir el tiempo de ejecución de BFS
print("BFS:")
start_time_bfs = time.time()
g.bfs_method(1)
end_time_bfs = time.time()
execution_time_bfs = end_time_bfs - start_time_bfs
print("Tiempo de ejecución de BFS:", execution_time_bfs)