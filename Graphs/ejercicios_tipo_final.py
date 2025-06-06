# ejercicios_tipo_final.py

from graphs import AdjListGraph

"""
Función que calcula cuántas rutas existen entre dos vértices
sin pasar por un conjunto de vértices excluidos.
"""

def dfs(graph, start, end, excluded):
    stack = [(start, [start])]
    count = 0

    while stack:
        current, path = stack.pop()

        if current in excluded:
            continue

        if current == end:
            count += 1
            continue

        for neighbor, _ in graph.get(current, []):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return count


# Crear grafo y añadir vértices
g = AdjListGraph()
for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
    g.add_vertex(v)

# Añadir aristas
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.add_edge('C', 'G')
g.add_edge('E', 'D')
g.add_edge('F', 'G')
g.add_edge('G', 'H')
g.add_edge('H', 'I')
g.add_edge('I', 'D')

# Parámetros de búsqueda
v1 = 'A'
v2 = 'D'
Vex = {'E', 'F'}  # Vértices excluidos

print(dfs(g.adj_list, v1, v2, Vex))
