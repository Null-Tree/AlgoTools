import networkx as nx
import matplotlib.pyplot as plt


print("\n=================\nQuestion B\n=======================\n")

def prim(graph:nx.Graph):

    minTree=nx.Graph()



    # initialise tree
    minTree.add_node(list(graph.nodes)[0])

    while len(minTree.nodes) < len(graph.nodes):
        edges=[]
        for edge in graph.edges.data():
            if edge[0] in minTree.nodes and edge[1] in minTree.nodes:
                # if the end nodes of the poitns are already in min span tree, ignore
                continue
            if edge[0] in minTree.nodes or edge[1] in minTree.nodes:
                edges.append(edge)

            # sort, for key is the third item, with value of key weight
            edges.sort(key=lambda x:x[2]['weight']) 

            # add edge with least weight

            minTree.add_edges_from([edges[0]])

    return minTree


fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2)


G = nx.Graph()
G.add_weighted_edges_from([(4,5,3.5), (4,7,3.7), (5,7,2.8),(0,7,1.6),(1,5,3.2)])
G.add_weighted_edges_from([(0,4,3.8), (2,3,1.7), (1,7,1.9),(0,2,2.6),(1,2,3.6)])
G.add_weighted_edges_from([(1,3,2.9), (2,7,3.4), (6,2,4.0),(3,6,5.2),(6,0,5.8),(6,4,9.3)])
pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=550, node_color='yellow',ax=ax1)
nx.draw_networkx_labels(G,pos,ax=ax1)
nx.draw_networkx_edges(G, pos, width=5, edge_color ='darkblue',ax=ax1)
edge_labels=dict([((u,v),d["weight"])
for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,ax=ax1)



mst=prim(G)
displayG=mst
pos2 = nx.shell_layout(displayG) # position nodes on canvas

nx.draw_networkx_nodes(displayG, pos2, node_size=550, node_color='yellow',ax=ax2)
nx.draw_networkx_labels(displayG,pos2,ax=ax2)
nx.draw_networkx_edges(displayG, pos2, width=2, edge_color ='red',ax=ax2)





plt.axis("off")
plt.show()