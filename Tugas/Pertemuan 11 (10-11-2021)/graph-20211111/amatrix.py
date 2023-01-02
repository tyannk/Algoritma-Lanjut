Vertex = []
graph = []
jumlah_vertex = 0

def add_vertex(v):
    global jumlah_vertex
    if v in Vertex:
        print(v, 'sudah ada di graph')
    else:
        Vertex.append(v)
        jumlah_vertex += 1
        for i in graph:
            i.append(0)
        baris_baru = []
        for j in range(jumlah_vertex):
            baris_baru.append(0)
        graph.append(baris_baru)

def add_edge(v1,v2):
    if v1 not in Vertex or v2 not in Vertex:
        print('Vertex tidak ada di graph')
    else:
        idx1 = Vertex.index(v1)
        idx2 = Vertex.index(v2)
        graph[idx1][idx2] = 1
        graph[idx2][idx1] = 1

def delete_vertex(v):
    global jumlah_vertex
    if v not in Vertex:
        print(v, 'tidak ada di graph')
    else:
        idx = Vertex.index(v)
        graph.pop(idx)
        Vertex.remove(v)
        jumlah_vertex -= 1
        for i in graph:
            i.pop(idx)

def delete_edge(v1,v2):
    if v1 not in Vertex or v2 not in Vertex:
        print('Vertex tidak ada di graph')
    else:
        idx1 = Vertex.index(v1)
        idx2 = Vertex.index(v2)
        graph[idx1][idx2] = 0
        graph[idx2][idx1] = 0



def print_graph():
    global jumlah_vertex
    print(Vertex)
    for i in range(jumlah_vertex):
        for j in range(jumlah_vertex):
            print(graph[i][j],end=' ')
        print()

add_vertex('A')
add_vertex('B')
add_vertex('C')
print_graph()
add_edge('A','B')
print_graph()
delete_vertex('C')
print_graph()
delete_edge('A','B')
print_graph()

