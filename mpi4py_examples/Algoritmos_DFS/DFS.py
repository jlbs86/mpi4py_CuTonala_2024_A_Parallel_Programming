"Este es un codigo del algoritmo de profundidad o mejor conocido como DFS"

def dfs(grafo, nodo_inicial, visitado=None):
    if visitado is None:
        visitado = set()  # Conjunto para almacenar los nodos visitados

    visitado.add(nodo_inicial)  # Marcamos el nodo actual como visitado
    print(nodo_inicial)  # Procesamos el nodo (puedes modificar esto según tus necesidades)

    # Recorremos los vecinos no visitados del nodo actual
    for vecino in grafo[nodo_inicial]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como un diccionario de listas de adyacencia
    grafo = {
        'A': ['B', 'C'],
        'C': ['D', 'E'],
        'B': ['F'],
        'D': [],
        'F': ['E'],
        'E': []
    }

    nodo_inicial = 'A'  # Nodo raíz}
    print('Metodo DFS: ')
    dfs(grafo, nodo_inicial) 
