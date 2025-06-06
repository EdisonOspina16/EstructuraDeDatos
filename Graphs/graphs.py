class EdgeListGraph:

    def __init__(self):
        self.edges = []

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def remove_edge(self, u, v):
        try:
            self.edges.remove((u, v))
        except ValueError:
            raise ValueError(f"No edge exists between {u} and {v}")

    def __str__(self):
        return str(self.edges)


class AdjMatrixGraph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, src, dest, weight=1):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.adj_matrix[src][dest] = weight
        else:
            raise ValueError("Index out of range")

    def remove_edge(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.adj_matrix[src][dest] = 0
        else:
            raise ValueError("Index out of range")


class AdjListGraph:

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest, weight=1):
        if src in self.adj_list:
            self.adj_list[src].append((dest, weight))
            self.adj_list[dest].append((src, weight))
        else:
            raise ValueError(f"source vertex {src} not in graph ")

    def remove_edge(self, src, dest):
        if src in self.adj_list:
            if dest in self.adj_list[src]:
                self.adj_list[src].remove(dest)
            else:
                raise ValueError(f"edge {src, dest} not in graph")

    def dfs(self, src, visited=None):
        if not visited:
            visited = set()
        visited.add(src)
        print(src)
        for neighbour in self.adj_list[src]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def get_neighbors(self, vertex):
        return self.adj_list.get[vertex, []]

    def get_nodes(self):
        return list(self.adj_list.keys())

    def string_to_graph(self, string):
        for i in range(len(string) - 1):
            v1 = string[i]
            v2 = string[i + 1]

            # Añadir vértices si no existen
            if v1 not in self.adj_list:
                self.add_vertex(v1)
            if v2 not in self.adj_list:
                self.add_vertex(v2)

            # Añadir arista si no existe
            if v2 not in self.adj_list[v1]:
                self.add_edge(v1, v2)

    def __str__(self):
        return f"Grafo: {self.adj_list}\nVértices: {len(self.adj_list)}\nAristas: {sum(len(v) for v in self.adj_list.values())}"

class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)


    def delete_neighbour(self, neighbour):
        if neighbour in self.neighbours:
            self.neighbours.remove(neighbour)


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)

    def add_edge(self, src_value, dest_value):
        if src_value in self.vertices and dest_value in self.vertices:
            src_vertex = self.vertices[src_value]
            dest_vertex = self.vertices[dest_value]
            src_vertex.add_neighbour(dest_vertex)

    def remove_edge(self, src_value, dest_value):
        if src_value in self.vertices and dest_value in self.vertices:
            src_vertex = self.vertices[src_value]
            dest_vertex = self.vertices[dest_value]
            src_vertex.delete_neighbour(dest_vertex)


g = AdjListGraph()
g.string_to_graph("Estructuras")
print(g)
