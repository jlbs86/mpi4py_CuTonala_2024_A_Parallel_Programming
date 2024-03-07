"Este es un codigo del algoritmo de profundidad o mejor conocido como BFS"

from collections import deque
import time

"Este es el algoritmo de BFS"
inicio1 = time.time()
def bfs(grafo, nodo_inicial):
    visitado = set()
    fila = deque([nodo_inicial])  

    while fila:
        nodo_actual = fila.popleft()
        if nodo_actual not in visitado:
            print(nodo_actual)
            visitado.add(nodo_actual)
            for vecino in grafo[nodo_actual]:
                if vecino not in visitado:
                    fila.append(vecino)
time.sleep(1)
fin1 = time.time()

"Este el algoritmo es el DFS"
inicio2 = time.time()
def dfs(grafo, nodo_inicial, visitado=None):
    if visitado is None:
        visitado = set() 

    visitado.add(nodo_inicial) 
    print(nodo_inicial) 

    for vecino in grafo[nodo_inicial]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)
time.sleep(1)
fin2 = time.time()

if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'C': ['D', 'E'],
        'B': ['F'],
        'D': [],
        'F': ['E'],
        'E': []
    }

    nodo_inicial = 'A' 
    print("Resultado BFS: ")
    bfs(grafo, nodo_inicial)
    print("Resultado DFS: ")
    dfs(grafo, nodo_inicial)

    tiempo_transcurrido = fin1 - inicio1
    print(f"tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")
    tiempo_transcurrido = fin2 - inicio2
    print(f"tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")