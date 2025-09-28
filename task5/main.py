from bintree import Node, dfs_iterative, generate_colors, bfs_iterative, draw_tree




root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)




dfs_order = dfs_iterative(root)
colors = generate_colors(len(dfs_order))
for node, color in zip(dfs_order, colors):
    node.color = color
draw_tree(root, "DFS (обхід у глибину)")

bfs_order = bfs_iterative(root)
colors = generate_colors(len(bfs_order))
for node, color in zip(bfs_order, colors):
    node.color = color
draw_tree(root, "BFS (обхід у ширину)")