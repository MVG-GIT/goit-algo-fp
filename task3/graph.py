import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {i: [] for i in range(vertices)}  # adjacency list

    def add_edge(self, start, end, weight):
        self.adj[start].append((end, weight))
        self.adj[end].append((start, weight))

    def dijkstra(self, start):
        dist = {i: float('inf') for i in range(self.vertices)}
        dist[start] = 0

        heap = [(0, start)]

        while heap:
            current_dist, start_vertice = heapq.heappop(heap)

            # is the shortest path
            if current_dist > dist[start_vertice]:
                continue

            for end_vertice, weight in self.adj[start_vertice]:
                if dist[start_vertice] + weight < dist[end_vertice]:
                    dist[end_vertice] = dist[start_vertice] + weight
                    heapq.heappush(heap, (dist[end_vertice], end_vertice))

        return dist
