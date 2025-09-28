import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_size=10)
    plt.show()


def build_heap_tree(heap, i=0):
    if i >= len(heap):
        return None
    root = Node(heap[i])
    root.left = build_heap_tree(heap, 2 * i + 1)
    root.right = build_heap_tree(heap, 2 * i + 2)
    return root
  
def generate_colors(n, start=(18, 50, 80), end=(180, 220, 255)):
    colors = []
    for i in range(n):
        r = int(start[0] + (end[0] - start[0]) * i / (n - 1))
        g = int(start[1] + (end[1] - start[1]) * i / (n - 1))
        b = int(start[2] + (end[2] - start[2]) * i / (n - 1))
        colors.append(f'#{r:02X}{g:02X}{b:02X}')
    return colors
  
  
def dfs_iterative(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited

def bfs_iterative(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited