import networkx as nx
import matplotlib.pyplot as plt
a=nx.DiGraph()

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

for node in nodes:
    a.add_node(node)

a.add_edges_from(edges)

fig, ax = plt.subplots()

pos=nx.kamada_kawai_layout(a)


# define color map. user_node = red, book_nodes = green
# color_map = ['red' if node == user_id else 'green' for node in G]        
# graph = nx.draw_networkx(G,pos, node_color=color_map) # node lables


nx.draw_networkx_nodes(a,pos,node_size=0,node_color="#1f2120", node_shape="o" ) #  

nx.draw_networkx_labels(a,pos,font_color="#cdcecf")  #,font_size=14

nx.draw_networkx_edges(a,pos,width=2,edge_color="#cdcecf")

ax.set_facecolor("#2a303c")

# plt.axis('off')
plt.savefig("test.png", bbox_inches="tight", pad_inches=0.0)
plt.show()