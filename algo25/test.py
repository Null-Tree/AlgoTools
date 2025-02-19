

from graphhelpers import graph


nodes:list[str] = [
    "A",
    "B",
    "C",
    "D"
]

# [source, target]
edges:list[tuple[str]] = [
    ("B", "A", {"dist":10}),
    ("D", "B", {"dist":10}),
    ("B", "C", {"dist":10}),
    ("C", "D", {"dist":10})
]



graph(nodes,edges,directed=False,show=True)