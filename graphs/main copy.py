
from graph_algoritms.dijkstra import dijkstra
import networkx as nx
import matplotlib.pyplot as plt

from datetime import datetime

reltype = {
    3:"Bffs",
    1:"just friends"

}

def graph(nodes:list[str],

                  edges:list[tuple[str]],
                  directed:bool=False,
                  plot:bool=None,
                  show:bool=None,
                  save:bool=None,
                  nodesize:int=None) -> nx.DiGraph:


    if directed:
        a=nx.DiGraph()
    else:
        a=nx.Graph()
    a.add_nodes_from(nodes)
    a.add_edges_from(edges)

    pos=nx.kamada_kawai_layout(a)

    if (plot or show):
        fig, ax = plt.subplots()

        pos=nx.kamada_kawai_layout(a)


        # define color map. user_node = red, book_nodes = green
        # color_map = ['red' if node == user_id else 'green' for node in G]        
        # graph = nx.draw_networkx(G,pos, node_color=color_map) # node lables


        # nodes
        if not nodesize:
            if directed:
                nodesize=0
            else:
                nodesize=300
        nx.draw_networkx_nodes(a,pos,node_size=nodesize,node_color="#1f2120", node_shape="o" ) #  

        nx.draw_networkx_labels(a,pos,font_color="#cdcecf")  #,font_size=14

        #edges

        nx.draw_networkx_edges(a,pos,width=2,edge_color="#cdcecf")
        edge_labels=dict([((u,v),reltype[d["weight"]]) for u,v,d in a.edges(data=True)])

        nx.draw_networkx_edge_labels(a,pos,edge_labels=edge_labels,font_color="#1f2120")
        #other

        ax.set_facecolor("#2a303c")

        if save:
            plt.saveplt()

        if show:
            plt.show()
        return a
    else:
        return a
   


################################



nodes:list[str] = [
    "A",
    "B",
    "C",
    "D",
    "Q"
]


# reltype: 3 bffs   1 just friends
# [source, target]
edges:list[tuple[str]] = [
    ("B", "A", {"weight":3}),
    ("D", "B", {"weight":1}),
    ("B", "C", {"weight":3}),
    ("C", "D", {"weight":1}),
    ("A", "D", {"weight":3}),
    ("C", "Q", {"weight":3})
]



#########################




newgraph = graph(nodes,edges,directed=False,show=True)

for node in nodes:
    print(f"For {node}: {dijkstra(newgraph,node)}")

for node in nodes:
    mutuals=[]
    dictionary=dijkstra(newgraph,node)
    for subject in (nodes):
        if subject != node:
            weight = dictionary[subject]
            if not newgraph.has_edge(node,subject):
                mutuals.append((subject,weight))

    print(f"mutuals of {node}: {mutuals}")

# the lower the number the stronger the mutuals