
from graphhelpers import *


################################

nodes:list[str] = [
    "A",
    "B",
    "C",
    "D"
]

# [source, target]
edges:list[tuple[str]] = [
    ("B", "A", {"weight":13}),
    ("D", "B", {"weight":20}),
    ("B", "C", {"weight":7}),
    ("C", "D", {"weight":10})
]



#########################

newgraph = graph(nodes,edges,directed=True,show=False)

###
from minDist.floydWarshal import floyd_warshall

out = floyd_warshall(newgraph)
print(out)

