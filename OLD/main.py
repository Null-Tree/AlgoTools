

from graphhelpers import *

################################

nodes:list[str] = [str(x) for x in range (8)]

# [source, target]
edges:list[tuple[str]] = [
    ("0", "1", {"weight":1}),
    ("0", "2", {"weight":1}),
    ("0", "3", {"weight":1}),
    ("0", "4", {"weight":1}),
    ("1", "5", {"weight":1}),
    ("2", "6", {"weight":1}),
    ("3", "7", {"weight":1}),
    ("4", "8", {"weight":1})

]





#########################

newgraph = graph(nodes,edges,directed=False,show=True , weighted=False)
