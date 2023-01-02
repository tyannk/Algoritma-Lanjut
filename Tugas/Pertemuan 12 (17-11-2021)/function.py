import math
# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

Vertex = []
graph = {}
jumlah_vertex = 0

def add_vertex(v):
    if v in graph:
        print('vertex sudah ada di graph')
    else:
        graph[v] = {}


def add_edge(v1, v2, bobot):
    if v1 not in graph or v2 not in graph:
        print('vertex tidak ada di graph')
    else:
        graph[v1][v2] = bobot
        graph[v2][v1] = bobot


def print_graph():
    global jumlah_vertex
    print(jumlah_vertex)
    print(Vertex)
    for i in range(jumlah_vertex):
        for j in range(jumlah_vertex):
            print(graph[i][j], end=' ')
        print()


def dijkstra(source):
    queue = {v: math.inf for v in graph}
    # print("\nqueue:", queue)
    d = {v: math.inf for v in graph}
    # print("\nDistance", d)
    predecessor = {v: None for v in graph}
    # print("\nPredecessor:", predecessor)
    d[source] = 0
    #d[tujuan] = math.inf
    queue[source] = 0

    while queue:
        u = min(queue, key=queue.get)
        # print("\nnilai U:", u)
        queue.pop(u)
        # print("\nqueue", queue)
        # print("\ngraph u:", graph[u])
        for v in graph[u]:
            # print("\nv:", v)
            dtemp = d[u] + graph[u][v]
            # print("\ngraph u v:", graph[u][v])
            # print("\nd u:", d[u])
            # print("\ndtemp:", dtemp)
            # print("\nd v:", d[v])
            if dtemp < d[v]:
                d[v] = dtemp
                predecessor[v] = u
                # print("\npredecessor v:", predecessor[v])
    # i = 1
    # jalur = []
    # ptemp = tujuan
    # jalur.append(ptemp)
    # while ptemp != source:
    #     if i == 1:
    #         ptemp = predecessor[tujuan]
    #     elif i > 1:
    #         ptemp = predecessor[ptemp]
    #     jalur.append(ptemp)
    #     i += 1
    # jalur.reverse()
    return d, predecessor

