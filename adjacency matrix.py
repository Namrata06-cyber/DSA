class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=" ")

        for i in range(self.vertices):
            if self.adj_matrix[start][i] == 1 and not visited[i]:
                self.dfs(i, visited)

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("Adjacency Matrix:")
for row in g.adj_matrix:
    print(row)

visited = [False] * 5

print("\nDFS Traversal:")
g.dfs(0, visited)