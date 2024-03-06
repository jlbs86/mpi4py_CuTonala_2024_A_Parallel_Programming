"Este es un codigo del algoritmo de profundidad o mejor conocido como BFS"

from collections import deque

def bfs(grafo, nodo_inicial):
    visitado = set()
    fila = deque([nodo_inicial])

# Evaluamos con un while y tomamos el primer nodo de la cola
    while fila:
        nodo_actual = fila.popleft()
        if nodo_actual not in visitado:
            print(nodo_actual)
            visitado.add(nodo_actual)

            # Agregamos los vecinos no visitados a la cola
            for vecino in grafo[nodo_actual]:
                if vecino not in visitado:
                    fila.append(vecino)

if __name__ == "__main__":
    # Grafo
    grafo = {
        'A': ['B', 'C'],
        'C': ['D', 'E'],
        'B': ['F'],
        'D': [],
        'F': ['E'],
        'E': []
    }

    nodo_inicial = 'A'
    bfs(grafo, nodo_inicial)
