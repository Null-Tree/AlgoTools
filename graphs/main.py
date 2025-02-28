

from graphhelpers import *

################################

nodes:list[str] = [
    "A",
    "B",
    "C",
    "D",
    "Q"
]

# [source, target]
edges:list[tuple[str]] = [
    ("B", "A", {"weight":13}),
    ("D", "B", {"weight":20}),
    ("B", "C", {"weight":7}),
    ("C", "D", {"weight":10}),
    ("A", "D", {"weight":10}),
    ("C", "Q", {"weight":10})
]



#########################

newgraph = graph(nodes,edges,directed=True,show=False )

def bfs(graph, start, target):
    considered=[]
    return travel(graph,start,target,considered)
    

def travel(graph,current,target,considerd):
    
    if type(graph) == nx.Graph:
        neighbours = list(graph.neighbors(current))
    elif type(graph) == nx.DiGraph:
        neighbours = list(graph.successors(current))

    considerd.append(current)
    for neighbour in neighbours:

        if neighbour not in considerd:
            
            if neighbour == target:
                return [current,target]

            path = travel(graph,neighbour,target,considerd)

            if path:
                return [current]+path
            
            
        

print(bfs(newgraph,"B","D"))