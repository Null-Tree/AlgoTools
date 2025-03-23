import networkx as nx


print("\n=================\nQuestion A\n=======================\n")
  
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

def dijkstra_initialise(graph: nx.Graph, start, end) -> list:


    node_distances = dijkstra(graph, start)

    path = [end]

    while path[0] != start:

        for i in graph.neighbors(path[0]):

            if node_distances[i] == node_distances[path[0]] - graph[path[0]][i]['weight']:

                path.insert(0, i)

                break

    return path




# nodes:list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# # [source, target]
# edges:list[tuple[str]] =[('a', 'b', {'weight': 8}), ('a', 'f', {'weight': 5}), ('f', 'g', {'weight': 9}), ('a', 'c', {'weight': 7}), ('c', 'd', {'weight': 4}), 
#                          ('c', 'g', {'weight': 6}), ('d', 'g', {'weight':3}), ('d', 'e', {'weight': 3}), ('g', 'h', {'weight': 4}), ('e', 'h', {'weight': 2})]



nodes=['a', 'b', 'c', 'd', 'e', 'f']
edges=[('a', 'c', {'weight': 4}), ('c', 'e', {'weight': 2}), ('a', 'b', {'weight': 3}), ('a', 'd', {'weight': 4}), ('b', 'd', {'weight': 2}), ('d', 'f', {'weight': 6}), ('d', 'e', {'weight': 4}), ('e', 'f', {'weight': 3})]
graph=nx.Graph()

graph.add_nodes_from(nodes)

graph.add_edges_from(edges)

out=dijkstra_initialise(graph,"f","a")
print(out)
