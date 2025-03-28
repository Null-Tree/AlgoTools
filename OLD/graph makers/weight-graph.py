#####################################################################
# unweighted directed graph maker
# positions not fixed
#####################################################################
import networkx as nx
import matplotlib.pyplot as plt
a=nx.Graph()

nodes:list[str] = ['a', 'b', 'c', 'd', 'e', 'f']

# [source, target]
edges:list[tuple[str]] = [('a', 'b', {'weight': 6}), ('a', 'd', {'weight': 5}), ('a', 'c', {'weight': 1}), ('b', 'c', {'weight': 5}), ('d', 'c', {'weight': 5}), ('b', 'e', {'weight': 3}), ('e', 'f', {'weight': 6}), ('e', 'c', {'weight': 6}), ('c', 'f', {'weight': 4}), ('d', 'f', {'weight': 2})]




# define color map. user_node = red, book_nodes = green
# color_map = ['red' if node == user_id else 'green' for node in G]        
# graph = nx.draw_networkx(G,pos, node_color=color_map) # node lables



graph=nx.Graph()





graph.add_nodes_from(nodes)

graph.add_edges_from(edges)

fig, ax = plt.subplots()

pos=nx.kamada_kawai_layout(graph)




# nodes
nx.draw_networkx_nodes(graph,pos,node_size=300,node_color="#1f2120", node_shape="o" ) #  

nx.draw_networkx_labels(graph,pos,font_color="#cdcecf")  #,font_size=14

#edges

nx.draw_networkx_edges(graph,pos,width=2,edge_color="#cdcecf")
edge_labels=dict([((u,v),d["weight"]) for u,v,d in graph.edges(data=True)])

nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels,font_color="#1f2120")
#other

ax.set_facecolor("#2a303c")

# plt.axis('off')
plt.savefig("test.png", bbox_inches="tight", pad_inches=0.0)
plt.show()