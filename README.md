# Proyecto: DFS Iterativo con Pila Propia

##  Descripción

Este proyecto implementa el algoritmo **DFS (Depth First Search)** de manera iterativa, es decir, sin utilizar recursión.  
Para lograrlo, se diseñó e implementó manualmente una estructura de datos **Stack (Pila)** que permite simular el comportamiento de la pila de llamadas del sistema.

El proyecto también incluye funcionalidades adicionales para trabajar con grafos no dirigidos.

---

##  Objetivo

Aplicar los conceptos fundamentales de estructuras de datos mediante:

- Implementación manual de una pila (Stack).
- Representación de un grafo mediante lista de adyacencia.
- Desarrollo del algoritmo DFS iterativo.
- Cálculo de componentes conexas.
- Detección de ciclos en grafos no dirigidos.

---

##  Conceptos aplicados

- Estructura de datos tipo LIFO (Stack)
- Grafos no dirigidos
- Lista de adyacencia
- Recorrido en profundidad (DFS)
- Componentes conexas
- Detección de ciclos usando nodo padre

---

##  Funcionalidades implementadas

### Clase `Stack`
- `push(x)`
- `pop()`
- `peek()`
- `is_empty()`
- `size()`

### Clase `Graph`
- `add_edge(u, v)`
- `dfs_iterative(start)`
- `connected_components()`
- `has_cycle_undirected()`

---

##  Pruebas incluidas

El programa ejecuta automáticamente tres pruebas:

1. **DFS en grafo sin ciclo**
   - Se imprime el orden de recorrido desde un nodo inicial.

2. **Detección de ciclo**
   - Se evalúa un grafo con ciclo y se muestra `True` o `False`.

3. **Componentes conexas**
   - Se genera un grafo con múltiples componentes y se muestran agrupadas.

---

##  Cómo ejecutar :)

Asegúrate de tener Python 3 instalado.

Ejecuta en la terminal:

```bash
python proyecto_dfs.py
```

El programa mostrará los resultados de las tres pruebas en pantalla.

---

##  Estructura del proyecto

```
PROYECTO-DFS/
│
├── proyecto_dfs.py
├── proyecto_dfs_iterativo.ipynb
└── README.md
```

---

##  Integrantes

- Edwuard Chay  
- Giovana Diaz  
- David Morales  

---

##  Materia

Estructura de Datos  

##  Fecha de entrega

27 de Febrero