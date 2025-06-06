from graphs import AdjListGraph


"""
Cree una función que reciba un grafo dirigido G, un vertice origen v1 y un vertice destino v2,
y un conjunto vertices excluidos Vex = {'v4','v3'},
la función debe retornar cuantas rutas existen entre v1 y v2 pero sin pasar por los vertices excluidos.
Si no existe ruta entre v1 y v2, ó las rutas que existen pasan por v4 ó v3, debe retornar 0.
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

        for neighbor in graph.get(current, []):
            if neighbor not in path:  # Evitar ciclos
                stack.append((neighbor, path + [neighbor]))

    return count

g = AdjListGraph()
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

v1 = 'A'
v2 = 'D'
Vex = {'E', 'F'}

# Aquí sí estamos usando tu clase
print(dfs(g.adj_list, v1, v2, Vex))  # Resultado esperado: 2

