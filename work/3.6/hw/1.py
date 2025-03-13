
import random
import networkx as nx
import matplotlib.pyplot as plt


####################################

#bfs

def bfs(graph:nx.Graph, start):
    visited=[]
    backlog = []

    spread_routes:list[list]=[]
    totalTold:dict={}

    backlog.append(start)
    current=start



    while (len(backlog)!=0):
        current=backlog.pop()
        visited.append(current)

        keys = [key for key in totalTold]
        if current not in keys:
            totalTold[current]=[]


        teller=current
        
        if type(graph) == nx.Graph:
            neighbours = list(graph.neighbors(current))
        elif type(graph) == nx.DiGraph:
            neighbours = list(graph.successors(current))

        for neighbour in neighbours:
            if neighbour not in (visited + backlog):
                backlog.append(neighbour)
                listener=neighbour
                spread_routes.append([teller,listener])
                totalTold[teller].append(listener)            

    return spread_routes,totalTold





#########################################

people=["Jeff","Randy","bob","jefferson","alica","trisha","justin","austin","bobstin","robson","renninson","denninson"]
edges=[('bob', 'denninson', {'weight': 15}), ('bob', 'trisha', {'weight': 4}), ('justin', 'austin', {'weight': 11}), ('justin', 'denninson', {'weight': 3}), ('alica', 'bobstin', {'weight': 19}), ('bobstin', 'robson', {'weight': 9}), ('bobstin', 'robson', {'weight': 13}), ('robson', 'Randy', {'weight': 5}), ('bobstin', 'trisha', {'weight': 14}), ('robson', 'Randy', {'weight': 8}), ('renninson', 'trisha', {'weight': 17}), ('renninson', 'trisha', {'weight': 18}), ('bob', 'Jeff', {'weight': 9}), ('trisha', 'jefferson', {'weight': 18}), ('alica', 'trisha', {'weight': 16}), ('bob', 'trisha', {'weight': 13}), ('renninson', 'denninson', {'weight': 16}), ('bobstin', 'Jeff', {'weight': 5}), ('Randy', 'Jeff', {'weight': 4}), ('denninson', 'justin', {'weight': 17}), ('Jeff', 'robson', {'weight': 2}), ('jefferson', 'bob', {'weight': 16}), ('robson', 'austin', {'weight': 5}), ('renninson', 'Randy', {'weight': 18}), ('Randy', 'bobstin', {'weight': 6}), ('renninson', 'denninson', {'weight': 11}), ('alica', 'trisha', {'weight': 12}), ('robson', 'bob', {'weight': 3}), ('alica', 'Jeff', {'weight': 3})]

#####################################################
# Generates edges

# for i in range(30):
#     i1=random.randint(0, len(people)-1)
#     i2=random.randint(0, len(people)-1)
#     if i1==i2:
#         continue
#     p1=people[i1]
#     p2=people[i2]
#     weight=random.randint(1, 20)
#     wdict={"weight":weight}
#     edges.append((p1,p2,wdict))
# print(edges)
#####################################################

graph=nx.Graph()
nodes=people


graph.add_nodes_from(nodes)

graph.add_edges_from(edges)

fig, ax = plt.subplots()

# pos=nx.kamada_kawai_layout(graph)
# pos=nx.shell_layout(graph)

pos=nx.circular_layout(graph)


# nodes
nx.draw_networkx_nodes(graph,pos,node_size=300,node_color="#1f2120", node_shape="o" ) #  

nx.draw_networkx_labels(graph,pos,font_color="#cdcecf")  #,font_size=14

#edges

nx.draw_networkx_edges(graph,pos,width=2,edge_color="#cdcecf")
edge_labels=dict([((u,v),d["weight"]) for u,v,d in graph.edges(data=True)])

nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels,font_color="#1f2120")
#other

ax.set_facecolor("#2a303c")

# plt.axis('off')

###################################


routes,totalTold=bfs(graph, "denninson")


# print(routes)
# print(telling)


for key in totalTold:
    if len(totalTold[key])!=0:
        print(f"{key} TOLD: {[person for person in totalTold[key]]}")

print("==================")
for i in range(len(routes)):
    route=routes[i]
    print(f"{i+1}. {route[0]} TOLD {route[1]}")


print("==================")
# maps route ontop
routesGraph=nx.Graph()
routesGraph.add_nodes_from(nodes)
routesGraph.add_edges_from(routes)
pos2=nx.circular_layout(graph)
nx.draw_networkx_edges(routesGraph,pos2,width=2,edge_color="red")

###################################

plt.show()