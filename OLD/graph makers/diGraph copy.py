#####################################################################
# unweighted directed graph maker
# positions not fixed
#####################################################################
import networkx as nx
import matplotlib.pyplot as plt
nodes=['a', 'b', 'c', 'd', 'e', 'f']
edges=[('a', 'b', {'weight': 6}), ('a', 'd', {'weight': 5}), ('a', 'c', {'weight': 1}), ('b', 'c', {'weight': 5}), ('d', 'c', {'weight': 5}), ('b', 'e', {'weight': 3}), ('e', 'f', {'weight': 6}), ('e', 'c', {'weight': 6}), ('c', 'f', {'weight': 4}), ('d', 'f', {'weight': 2})]

# edges=[ ('a', 'b', {'weight': 5}), ('a', 'b', {'weight': 1}), ('b', 'c', {'weight': 5})]


ingraph=nx.DiGraph()


ingraph.add_nodes_from(nodes)

ingraph.add_edges_from(edges)
a=ingraph

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