import networkx as nx

def bfs(graph, start, target):
    visited=[]
    
    backlog = []

    backlog.append(start)
    current=start
    while (current!=target and len(backlog)!=0):
        current=backlog.pop()
        visited.append(current)
        
        if type(graph) == nx.Graph:
            neighbours = list(graph.neighbors(current))
        elif type(graph) == nx.DiGraph:
            neighbours = list(graph.successors(current))

        for neighbour in neighbours:
            if neighbour not in (visited + backlog):
                backlog.append(neighbour)
    
    return visited


def dfs(graph, start, target):
    visited=[]
    
    backlog = []
    backlog.insert(0,start)
    current=start
    while (current!=target and len(backlog)!=0):


        current=backlog.pop()
        visited.append(current)
        
        
        if type(graph) == nx.Graph:
            neighbours = list(graph.neighbors(current))
        elif type(graph) == nx.DiGraph:
            neighbours = list(graph.successors(current))

        for neighbour in neighbours:
            if neighbour not in (visited+backlog):
                backlog.insert(0,neighbour)
    
    return visited
