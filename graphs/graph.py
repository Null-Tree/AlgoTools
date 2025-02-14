import networkx as nx
import matplotlib.pyplot as plt

a=nx.Graph()

nodes:list[str] = [
    "A",
    "B",
    "C",
    "D"
]

# [source, target]
edges:list[tuple[str]] = [
    ("B", "A"),
    ("D","B"),
    ("B","C"),
    ("C","D")
]

a.add_nodes_from(nodes)

a.add_edges_from(edges)

# makes shell layour for graph a
pos = nx.shell_layout(a)
nx.draw_networkx_nodes(a,pos)
nx.draw_networkx_edges(a,pos)
nx.draw_networkx_labels(a,pos)

plt.show()
