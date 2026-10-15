class RoadNetwork:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_road(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=" ")

        for i in range(self.vertices):
            if self.graph[start][i] == 1 and not visited[i]:
                self.dfs(i, visited)

road = RoadNetwork(5)

road.add_road(0, 1)
road.add_road(0, 2)
road.add_road(1, 3)
road.add_road(2, 4)

print("Adjacency Matrix:")
for row in road.graph:
    print(row)

visited = [False] * 5

print("\nDFS Traversal:")
road.dfs(0, visited)