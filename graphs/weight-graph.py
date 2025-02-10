#####################################################################
# unweighted directed graph maker
# positions not fixed
#####################################################################
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
    ("B", "A", {"dist":10}),
    ("D", "B", {"dist":10}),
    ("B", "C", {"dist":10}),
    ("C", "D", {"dist":10})
]

for node in nodes:
    a.add_node(node)

a.add_edges_from(edges)

fig, ax = plt.subplots()

pos=nx.kamada_kawai_layout(a)


# define color map. user_node = red, book_nodes = green
# color_map = ['red' if node == user_id else 'green' for node in G]        
# graph = nx.draw_networkx(G,pos, node_color=color_map) # node lables


# nodes
nx.draw_networkx_nodes(a,pos,node_size=300,node_color="#1f2120", node_shape="o" ) #  

nx.draw_networkx_labels(a,pos,font_color="#cdcecf")  #,font_size=14

#edges

nx.draw_networkx_edges(a,pos,width=2,edge_color="#cdcecf")
edge_labels=dict([((u,v),d["dist"]) for u,v,d in a.edges(data=True)])

nx.draw_networkx_edge_labels(a,pos,edge_labels=edge_labels,font_color="#1f2120")
#other

ax.set_facecolor("#2a303c")

# plt.axis('off')
plt.savefig("test.png", bbox_inches="tight", pad_inches=0.0)
plt.show()