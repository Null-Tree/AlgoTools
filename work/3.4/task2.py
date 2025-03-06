import networkx as nx
import matplotlib.pyplot as plt

from datetime import datetime


############################################################################
nodes:list[str] = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
]

nodeColorsIndex = ["" ,"Red","Red","Blue","Blue",""]

# [source, target]
edges:list[tuple[str]] = [
    ("A", "B", {"weight":2 }),
    ("A", "E", {"weight":3}),
    ("E", "D", {"weight":8,"color":"Blue"}),
    ("D", "F", {"weight":4}),
    ("F", "C", {"weight":4}),
    ("D", "C", {"weight":9}),
    ("C", "B", {"weight":7,"color":"Red"}),
    ("F", "B", {"weight":1}),
]



###################################################################################################
a=nx.Graph()

#process and group

# sets default to black
for i in range(len(nodeColorsIndex)):
    if not nodeColorsIndex[i]:
        nodeColorsIndex[i]="black"

for tup in edges:
    if "color" not in [key for key in tup[2]]:
        tup[2]["color"]="black"


a.add_nodes_from(nodes)
a.add_edges_from(edges)

pos=nx.kamada_kawai_layout(a)
print(pos)


for i in range(len(nodes)):
    node=nodes[i]
    color=nodeColorsIndex[i]
    nx.draw_networkx_nodes(a,pos,nodelist=[node],node_color=color)


nx.draw_networkx_labels(a,pos,font_color="white")  #,font_size=14


for edge in edges:
    color = edge[2]["color"]
    nx.draw_networkx_edges(a,pos, edgelist = [edge], edge_color=color)

edge_labels=dict([((u,v),d["weight"]) for u,v,d in a.edges(data=True)])
nx.draw_networkx_edge_labels(a,pos,edge_labels=edge_labels,font_color="#1f2120")

plt.show()