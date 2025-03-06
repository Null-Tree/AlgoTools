

from graphhelpers import *

################################

nodes:list[str] = [str(x) for x in range (1,7)]

# [source, target]
edges:list[tuple[str]] = [
    ("1", "5", {"weight":5}),
    ("3", "2", {"weight":23}),
    ("2", "5", {"weight":5}),
    ("5", "4", {"weight":14}),
    ("4", "3", {"weight":11}),
    ("1", "6", {"weight":18}),
    ("3", "6", {"weight":18})
]



#########################

newgraph = graph(nodes,edges,directed=False,show=True )
