"Este es un codigo del algoritmo de profundidad o mejor conocido como DFS"

def dfs(grafo, nodo_inicial, visitado=None):
    if visitado is None:
        visitado = set() 

    visitado.add(nodo_inicial) 
    print(nodo_inicial) 

    for vecino in grafo[nodo_inicial]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)

if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'C': ['D', 'E'],
        'B': ['F'],
        'D': [],
        'F': ['E'],
        'E': []
    }

    nodo_inicial = '1'  
    dfs(grafo, nodo_inicial)