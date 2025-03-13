# Python3/Trinket 3.6 Breakout Activity Graph
import matplotlib.pyplot as plt
import networkx as nx


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



G=nx.Graph()
# weighted edges for 3.6 activity
G.add_edge(4,5,weight=3.5)
G.add_edge(4,7,weight=3.7)
G.add_edge(5,7,weight=2.8)
G.add_edge(0,7,weight=1.6)
G.add_edge(1,5,weight=3.2)
G.add_edge(0,4,weight=3.8)
G.add_edge(2,3,weight=1.7)
G.add_edge(1,7,weight=1.9)
G.add_edge(0,2,weight=2.6)
G.add_edge(1,2,weight=3.6)
G.add_edge(1,3,weight=2.9)
G.add_edge(2,7,weight=3.4)
G.add_edge(6,2,weight=4.0)
G.add_edge(3,6,weight=5.2)
G.add_edge(4,5,weight=3.5)
G.add_edge(6,0,weight=5.8)
G.add_edge(6,4,weight=9.3)




displayG=prim(G)
pos = nx.shell_layout(displayG) # position nodes on canvas
nx.draw_networkx_nodes(displayG, pos, node_size=1000,node_color='LightGray')
nx.draw_networkx_labels(displayG, pos, font_size=20,font_family='sans-serif')
nx.draw_networkx_edges(displayG, pos, width=3, edge_color='LightBlue')

edge_labels=dict([((u,v),d['weight'])
for u,v,d in displayG.edges(data=True)])



nx.draw_networkx_edge_labels(displayG, pos,edge_labels=edge_labels)
plt.axis('off')
plt.show()


