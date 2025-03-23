import networkx as nx
import matplotlib.pyplot as plt


nodes=['a', 'b', 'c', 'd', 'e', 'f']
edges=[('a', 'b', {'weight': 6}), ('a', 'd', {'weight': 5}), ('a', 'c', {'weight': 1}), ('b', 'c', {'weight': 5}), ('d', 'c', {'weight': 5}), ('b', 'e', {'weight': 3}), ('e', 'f', {'weight': 6}), ('e', 'c', {'weight': 6}), ('c', 'f', {'weight': 4}), ('d', 'f', {'weight': 2})]


def prim(graph:nx.Graph):

    
    # initialise tree by providing first node
    minTree=nx.Graph()
    minTree.add_node(list(graph.nodes)[0])

    # while we have not connected all original input nodes, keep looking
    while len(minTree.nodes) < len(graph.nodes):
        edges=[]
        for edge in graph.edges.data():
            if edge[0] in minTree.nodes and edge[1] in minTree.nodes:
                # if the end nodes of the points are already in min span tree, ignore
                continue
            if edge[0] in minTree.nodes or edge[1] in minTree.nodes:
                edges.append(edge)

        # sort, for key is the third item, with value of key weight
        edges.sort(key=lambda x:x[2]['weight']) 
        print(edges)

        # add edge with least weight
        minTree.add_edges_from([edges[0]])

    return minTree


ingraph=nx.Graph()


ingraph.add_nodes_from(nodes)

ingraph.add_edges_from(edges)


graph=prim(ingraph)


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
# plt.savefig("test.png", bbox_inches="tight", pad_inches=0.0)
plt.show()







