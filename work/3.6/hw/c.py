import matplotlib.pyplot as plt
import networkx as nx


def tsDFS(graph:nx.DiGraph,visitedNodes,currentNode,stack:list)->list:
    
    
    visitedNodes.append(currentNode)


    for successor in graph.successors(currentNode):
        if successor not in visitedNodes:
            tsDFS(graph,visitedNodes,successor,stack)
            stack.append(currentNode)


    stack.append(currentNode)

def topologicalSort(graph:nx.DiGraph) -> list:
    stack=[]
    visitedNodes=[]
    notVisitedNodes=[node for node in graph.nodes]

    for currentNode in notVisitedNodes:
        if currentNode not in visitedNodes:

            tsDFS(graph,visitedNodes,currentNode,stack)

        
    stack.reverse()
    return stack
        

    



nodes=['tiger', 'human', 'fish', 'sheep', 'shrimp', 'plankton', 'wheat']
edges=[('wheat', 'human', {'weight': 1}), ('wheat', 'sheep', {'weight': 1}), ('plankton', 'shrimp', {'weight': 1}), ('plankton', 'shrimp', {'weight': 1}), ('shrimp', 'fish', {'weight': 1}), ('shrimp', 'human', {'weight': 1}), ('fish', 'human', {'weight': 1}), ('fish', 'tiger', {'weight': 1}), ('human', 'tiger', {'weight': 1}), ('sheep', 'human', {'weight': 1}), ('sheep', 'tiger', {'weight': 1})]    




fig,ax=plt.subplots()

graph=nx.DiGraph()
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)


pos=nx.shell_layout(graph)



nodesize=1000
# nodes
nx.draw_networkx_nodes(graph,pos,node_size=nodesize,node_color="#1f2120", node_shape="o" ) #  

nx.draw_networkx_labels(graph,pos,font_color="#cdcecf")  #,font_size=14

#edges

nx.draw_networkx_edges(graph,pos,width=2,edge_color="#cdcecf",arrowsize=15,arrows=True,node_size=nodesize)
edge_labels=dict([((u,v),d["weight"]) for u,v,d in graph.edges(data=True)])

nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels,font_color="#1f2120")
#other

ax.set_facecolor("#2a303c")



print(topologicalSort(graph))

plt.show()
