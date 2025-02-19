
from algo25.graphhelpers import *


################################

nodes:list[str] = [
    "A",
    "B",
    "C",
    "D"
]

# [source, target]
edges:list[tuple[str]] = [
    ("B", "A", {"dist":13}),
    ("D", "B", {"dist":20}),
    ("B", "C", {"dist":7}),
    ("C", "D", {"dist":10})
]



#########################

newgraph = graph(nodes,edges,directed=True,show=True)