    



import networkx as nx

def dijkstra(graph: nx.Graph, start) -> dict:

    unvisited = list(graph.nodes)
    # gets list

    node_distances = {node: float('inf') for node in graph.nodes}
    # creates set of distances, default initiate to inf
    
    node_distances[start] = 0

    
    while len(unvisited) > 0:
    
        node = min(unvisited, key=lambda x: node_distances[x])
    
        for i in graph.neighbors(node):
    
            if i in unvisited:
    
                node_distances[i] = min(node_distances[i], node_distances[node] + graph[node][i]['weight'])
    
        unvisited.remove(node)
    
    return node_distances

def find_shortest_path(graph: nx.Graph, start, end) -> list:

    node_distances = dijkstra(graph, start)

    path = [end]

    while path[0] != start:

        for i in graph.neighbors(path[0]):

            if node_distances[i] == node_distances[path[0]] - graph[path[0]][i]['weight']:

                path.insert(0, i)

                break

    return path