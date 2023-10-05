
def addEdge(myGraph,n,v ):
    myGraph[n].append(v)


def generate_edge(myGraph):
    l = []
    for node in myGraph:
        for value in myGraph[node]:
            l.append((node, value))
    return l



myGraph = {
    "a": ["b", "c"],
    "b": ["c", "d"],
    "c": ["d", "e"],
    "d": [],
    "e": []
}


addEdge(myGraph, "d", "e")

data = generate_edge(myGraph)
# print(generate_edge(myGraph))
print(data)