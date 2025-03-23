
def sep():
    print("---------------")


nodes:list[str] = [

]

# [source, target]
edges:list[tuple[str]] = [

]

in_node="."

stage="nodes"

while stage=="nodes":
    in_node = input("node: ")
    if in_node =="":
        stage="edges"
        break
    nodes.append(in_node)

sep()
n1=""
n2=""
weight=0
while stage=="edges":
    n1=input("n1: ")
    if n1=="":
        stage="end"
        break
    n2=input("n2: ")
    weight=input("weight: ")
    tup=(n1,n2,{"weight":int(weight)})
    edges.append(tup)
    print(tup)
    sep()

sep()
print("Nodes")
print(nodes)
sep()
print("edges")
print(edges)