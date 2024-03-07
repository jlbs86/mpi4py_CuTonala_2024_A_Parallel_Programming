"""Algoritmos de busqueda en arboles (grafos)."""


class Node:
    def __init__(self, value):
        self.value = value
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)


def bfs_iterativo(root):
    """Algoritmo de busqueda en anchura iterativo."""
    nodes = [root]
    visitados = []
    while nodes:
        current = nodes.pop()
        print(current.value)

        if current.childs and current not in visitados:
            nodes[:0] = current.childs[::-1]

        visitados.append(current)


def bfs_recursivo(root, first=True, visitados=[]):
    """Algoritmo de busqueda en anchura recursivo."""
    if not root or root in visitados:
        return

    if first:
        print(root.value)
        visitados.append(root)

    for node in root.childs:
        print(node.value)
        visitados.append(node)

    for node in root.childs:
        bfs_recursivo(node, False)


def dfs_iterativo(root):
    """Algoritmo de busqueda en profundidad iterativo."""
    nodes = [root]
    visitados = []
    while nodes:
        current = nodes.pop()
        print(current.value)

        if current.childs and current not in visitados:
            nodes.extend( current.childs[::-1] )

        visitados.append(current)


def dfs_recursivo(root, visitados=[]):
    """Algoritmo de busqueda en profundidad recursivo."""
    if not root or root in visitados:
        return

    print(root.value)
    visitados.append(root)
    for node in root.childs:
        dfs_recursivo(node, visitados)


def main():
    """Funcion Principal."""
    # (1 (2 9 7) (4 14 22))
    root = Node(1)
    child_1 = Node(2)
    child_2 = Node(4)
    root.add_child(child_1)
    root.add_child(child_2)
    child_1.add_child( Node(9) )
    child_1.add_child( Node(7) )
    child_2.add_child( Node(14) )
    child_2.add_child( Node(22) )

    node_a = Node('a')
    node_b = Node('b')
    node_a.add_child(node_b)
    node_b.add_child(node_a)

    bfs_recursivo(root)
    bfs_recursivo(node_a)


if __name__ == '__main__':
    main()
