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
    pass

def pruebas():
    pass

if __name__ == "__main__":
    pruebas()