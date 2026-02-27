class Stack:
    #Implementacion de una pila con lista
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)
    


class Graph:
    #Implementacion de un grafo con lista de adyacencia
    def __init__(self):
        self.adj = {} #diccionario: nodo -> lista de vecinos
    
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []
    
    def add_edge(self, u, v):
        #Grafor NO dirigido
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs_iterative(self, start): #DFS iterativo
        if start not in self.adj:
            return []

        visited = set()
        order = []
        stack = Stack()
        stack.push(start)

        while not stack.is_empty():
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)
            order.append(node)

            #Para que el DFS se vea "natural", metemos los vecinos al reves
            neighbors = self.adj[node]
            for neigh in reversed(neighbors):
                if neigh not in visited:
                    stack.push(neigh)

        return order

    def connected_components(self): #Componentes conexos
        visited = set()
        comps = []

        for start in self.adj.keys():
            if start in visited:
                continue

            #DFS desde start para sacar un componente
            stack = Stack()
            stack.push(start)
            comp = []

            while not stack.is_empty():
                node = stack.pop()
                if node in visited:
                    continue

                visited.add(node)
                comp.append(node)

                for neigh in self.adj[node]:
                    if neigh not in visited:
                        stack.push(neigh)

            comps.append(comp)

        return comps

def pruebas():
    pass


if __name__ == "__main__":
    pruebas()