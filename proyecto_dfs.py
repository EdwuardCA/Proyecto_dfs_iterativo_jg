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

    def has_cycle_undirected(self):
        visited = set()

        for start in self.adj.keys():
            if start in visited:
                continue

            # DFS con parent
            stack = Stack()
            stack.push((start, None))

            while not stack.is_empty():
                item = stack.pop()
                if item is None:
                    break
                node, parent = item

                if node in visited:
                    # Ojo: en esta versión, evitamos re-procesar
                    continue

                visited.add(node)

                for neigh in self.adj[node]:
                    if neigh not in visited:
                        stack.push((neigh, node))
                    elif neigh != parent:
                        return True

        return False

def pruebas():
    print("=== PRUEBA 1: DFS en grafo SIN ciclo ===")
    g1 = Graph()
    g1.add_edge("A", "B")
    g1.add_edge("A", "C")
    g1.add_edge("B", "D")
    print("DFS desde A:", g1.dfs_iterative("A"))
    print()

    print("=== PRUEBA 2: Detección de ciclo (grafo CON ciclo) ===")
    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 1)  # ciclo
    print("¿Tiene ciclo?:", g2.has_cycle_undirected())
    print()

    print("=== PRUEBA 3: Componentes conexas (2+ componentes) ===")
    g3 = Graph()
    g3.add_edge("X", "Y")
    g3.add_edge("Y", "Z")
    g3.add_edge("P", "Q")  # componente separada
    print("Componentes:", g3.connected_components())


if __name__ == "__main__":
    pruebas()