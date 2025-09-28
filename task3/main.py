from graph import Graph

g = Graph(6)
g.add_edge(0, 1, 7)
g.add_edge(0, 2, 9)
g.add_edge(0, 5, 14)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 11)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, 6)
g.add_edge(4, 5, 9)

start_vertex = 0
shortest_paths = g.dijkstra(start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for v in shortest_paths:
    print(f"Відстань до {v} = {shortest_paths[v]}")
