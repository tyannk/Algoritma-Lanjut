def add_vertex(v):
    if v in graph:
        print('vertex sudah ada di graph')
    else:
        graph[v] = []

def add_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print('vertex tidak ada di graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_vertex(v):
    if v not in graph:
        print('vertex tidak ada di graph')
    else:
        graph.pop(v)
        for key,value in graph.items():
            if v in value:
               value.remove(v)

def delete_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print('vertex tidak ada di graph')

    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)


graph = {}
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_edge('A','B')
add_edge('A','C')
add_edge('B','C')
print(graph)
delete_edge('A','C')



print(graph)
