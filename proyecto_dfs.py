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
        self.adj = [] #diccionario: nodo -> lista de vecinos
    
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []
    
    def add_edge(self, u, v):
        #Grafor NO dirigido
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    

def pruebas():
    pass

if __name__ == "__main__":
    pruebas()