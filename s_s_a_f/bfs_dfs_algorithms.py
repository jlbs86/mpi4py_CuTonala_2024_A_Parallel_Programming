"""Deepth and Breadth search methods."""


class Node:
    """Simple node for try search methods."""

    def __init__(self, value):
        self.value = value
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)


class SearchMethods:
    """Class with the search methods."""

    @static
    def bfs_iterative_method(root, target):
        """Breath search method, iterative aproach."""
        nodes = [root]
        visited = []
        while nodes:
            current = nodes.pop()

            # print(current.value)
            if current.value == target:
                return current
    
            if current.childs and current not in visited:
                nodes[:0] = current.childs[::-1]
    
            visited.append(current)

    @static
    def bfs_recursive_method(root, target, visitados=[], first=True):
        """Breath search method, recursive aproach."""
        if not root or root in visitados:
            return
    
        if first:
            # print(root.value)
            if current.value == target:
                return current

            visitados.append(root)
    
        for node in root.childs:
            # print(node.value)
            if node.value == target:
                return node

            visitados.append(node)
    
        for node in root.childs:
            bfs_recursivo(node, target, False)

    @static
    def dfs_iterative_method(root, target):
        """Deepth search method, iterative aproach."""
        nodes = [root]
        visited = []
        while nodes:
            current = nodes.pop()
            # print(current.value)
            if current.value == target:
                return current
    
            if current.childs and current not in visited:
                nodes.extend( current.childs[::-1] )
    
            visited.append(current)

    @static
    def dfs_recursive_method(root, target):
        """Deepth search method, iterative aproach."""
        if not root or root in visitados:
            return
    
        # print(root.value)
        if root.value == target:
            return root

        visitados.append(root)
        for node in root.childs:
            dfs_recursivo(node, visitados)
