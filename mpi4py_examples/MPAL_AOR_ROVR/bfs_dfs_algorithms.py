'''
miembros del equipo:
Avalos Lopez Marlene Paola
De la O Ramirez Alejandro
Vazquez Rodriguez Ramon Oswaldo
'''

import time


class Grafo:
    def __init__(self):
        self.nodos_visitados = set()
        self.camino = list()
        self.grafo = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["G"],
            "D": [],
            "E": ["F"],
            "F": [],
            "G": [],
        }

    def DFS(self, nodo_actual):
        self.nodos_visitados.add(nodo_actual)
        self.camino.append(nodo_actual)

        for vecino in self.grafo[nodo_actual]:
            if vecino not in self.nodos_visitados:
                self.DFS(vecino)

    def BFS(self, nodo_inicial):
        nodos_visitados = set()
        # Este es un conjunto vacio que almacena los nodos que ya se visitaron.
        nodos_faltantes = [nodo_inicial]
        # Esta es una cola vacia para almacenar los nodos faltantes.
        nodos_visitados.add(nodo_inicial)
        # Marcamos el nodo inicial como visitado.

        while nodos_faltantes:
            # Creamos un bucle mientras la cola no este vacia.
            nodo_inicial = nodos_faltantes.pop(0)
            # El .pop(0) elimina el ultimo elemento de los Nodos_faltantes y lo manda al Nodo_actual

            for vecinos in self.grafo[nodo_inicial]:
                # Repetimos esto sobre los vecinos del nodo actual en el grafo.
                if vecinos not in nodos_visitados:
                    nodos_faltantes.append(vecinos)
                    nodos_visitados.add(vecinos)
            # Si los vecinos no estan en los nodos visitados entonces:
            # si los vecinos no estan faltantes se agregan al final de la lista de los nodos faltantes.
            # Si los vecinos no estan en visitados se agregan a los nodos visitados.

        print(f"Nodos totales visitados: {len(nodos_visitados)}")
        print(
            f"Nodos máximos visitados por cualquier proceso: {max(len(nodos_visitados) for _ in self.grafo)}"
        )


# Definición de constantes


# Definición de funciones
def execution_time(funcion, *args, **kwargs):
    inicio = time.time()
    funcion(*args, **kwargs)
    fin = time.time()
    print(f"Tiempo de ejecución {funcion.__name__}: {(fin - inicio)*1000} milisegundos")


if __name__ == "__main__":
    nodo_inicial = "A"
    instancia = Grafo()

    execution_time(instancia.DFS, "A")
    execution_time(instancia.BFS, "A")
