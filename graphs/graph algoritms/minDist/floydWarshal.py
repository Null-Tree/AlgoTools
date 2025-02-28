import networkx as nx

# an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph
def floyd_warshall(graph: nx.DiGraph) -> list:
    
    
    nodes_to_index = {node: i for i, node in enumerate(graph.nodes)}
    # creates a unique integer index for all nodes

    distances = [[float('inf') for _ in range(len(graph.nodes))] for _ in range(len(graph.nodes))]
    # creates a 2d (adjacency) matrix populated with 'inf'

    #set distance for directly connected nodes
    for edge in graph.edges:
    
        distances[nodes_to_index[edge[0]]][nodes_to_index[edge[1]]] = graph.edges[edge]['weight']
    
    
    
    #vertices are distance zero to themselves
    for vertex in graph.nodes:
        distances[nodes_to_index[vertex]][nodes_to_index[vertex]] = 0
    
    
    for k in range(len(graph.nodes)):
    
        for i in range(len(graph.nodes)):
    
            for j in range(len(graph.nodes)):
	
                # repeatedly checks combinations of node connections
                # if it finds a lower one, it replaces the precious value
                # this works with connections with 2+ edges because distances start storing multi edge connections on iterations
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    
    return distances

