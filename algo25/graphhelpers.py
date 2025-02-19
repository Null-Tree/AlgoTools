import networkx as nx
import matplotlib.pyplot as plt

from datetime import datetime




def saveplt():
    now = datetime.now()
    filename = f'Plt_{now.strftime("%d%m%Y_%H%M%S")}.png'
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.0)

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
        edge_labels=dict([((u,v),d["dist"]) for u,v,d in a.edges(data=True)])

        nx.draw_networkx_edge_labels(a,pos,edge_labels=edge_labels,font_color="#1f2120")
        #other

        ax.set_facecolor("#2a303c")

        if save:
            saveplt()

        if show:
            plt.show()
        return a
    else:
        return a