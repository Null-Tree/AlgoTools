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


#################################################################################################################################
# set up graphs

fig,ax=plt.subplots()

#################################################################################################################################

#

#################################################################################################################################
# CREATE ORIGINAL GRAPH

originalGraph=nx.Graph()
# weighted edges for 3.6 activity
originalGraph.add_edge(4,5,weight=3.5)
originalGraph.add_edge(4,7,weight=3.7)
originalGraph.add_edge(5,7,weight=2.8)
originalGraph.add_edge(0,7,weight=1.6)
originalGraph.add_edge(1,5,weight=3.2)
originalGraph.add_edge(0,4,weight=3.8)
originalGraph.add_edge(2,3,weight=1.7)
originalGraph.add_edge(1,7,weight=1.9)
originalGraph.add_edge(0,2,weight=2.6)
originalGraph.add_edge(1,2,weight=3.6)
originalGraph.add_edge(1,3,weight=2.9)
originalGraph.add_edge(2,7,weight=3.4)
originalGraph.add_edge(6,2,weight=4.0)
originalGraph.add_edge(3,6,weight=5.2)
originalGraph.add_edge(4,5,weight=3.5)
originalGraph.add_edge(6,0,weight=5.8)
originalGraph.add_edge(6,4,weight=9.3)
#################################################################################################################################

#

#################################################################################################################################
# draw original graph
pos = nx.shell_layout(originalGraph) # position nodes on canvas
nx.draw_networkx_nodes(originalGraph, pos, node_size=1000,node_color='LightGray',ax=ax)
nx.draw_networkx_labels(originalGraph, pos, font_size=20,font_family='sans-serif',ax=ax)
nx.draw_networkx_edges(originalGraph, pos, width=5, edge_color='LightBlue',ax=ax)

edge_labels=dict([((u,v),d['weight'])for u,v,d in originalGraph.edges(data=True)])
nx.draw_networkx_edge_labels(originalGraph, pos,edge_labels=edge_labels,ax=ax)

plt.axis('off')
#################################################################################################################################

#

#################################################################################################################################
# CREATE OVERLAY

overlayGraph = prim(originalGraph)

overlayEdges=overlayGraph.edges

# note first needs to be original grpah
nx.draw_networkx_edges(originalGraph,pos,edgelist=overlayEdges, width=3, edge_color='red',ax=ax)

# redraw edge labels
nx.draw_networkx_edge_labels(originalGraph, pos,edge_labels=edge_labels,ax=ax)
#################################################################################################################################


plt.show()