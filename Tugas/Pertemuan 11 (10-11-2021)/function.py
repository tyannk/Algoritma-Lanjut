# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

Vertex = []
graph = []
graph_list = {}
jumlah_vertex = 0


def ask_delete_vertex_matrix():
    pilihan = input("ingin menghapus vertex matrix? ya/tidak:")
    while pilihan != 'ya' and pilihan != 'tidak':
        print("Inputan anda salah, silahkan ulangi\n")
        pilihan = input("ingin menghapus vertex matrix? ya/tidak:")
    while pilihan == 'ya':
        delete_vertex = input("\ninputkan vertex yang ingin di delete:")
        delete_vertex_matrix(delete_vertex)
        print("\nVertex matrix terbaru:", Vertex)
        print("Graph adjacency matrix terbaru:", graph, "\n")
        pilihan = input("ingin menghapus vertex matrix lagi? ya/tidak:")
        while pilihan != 'ya' and pilihan != 'tidak':
            print("Inputan anda salah, silahkan ulangi\n")
            pilihan = input("ingin menghapus vertex matrix? ya/tidak:")


def ask_delete_edge_matrix():
    pilihan = input("ingin menghapus edge matrix? ya/tidak:")
    while pilihan != 'ya' and pilihan != 'tidak':
        print("Inputan anda salah, silahkan ulangi\n")
        pilihan = input("ingin menghapus edge matrix? ya/tidak:")
    while pilihan == 'ya':
        delete_edge = input("\ninputkan edge matrix yang ingin di delete:")
        while len(delete_edge) != 2:
            print("inputan salah silahkan ulangi\n")
            delete_edge = input("\ninputkan edge yang ingin di delete:")
        delete_edge_matrix(delete_edge[0],delete_edge[1])
        print("\nVertex terbaru:", Vertex)
        print("Edge Terbaru:", graph, "\n")
        pilihan = input("ingin menghapus edge matrix lagi? ya/tidak:")
        while pilihan != 'ya' and pilihan != 'tidak':
            print("Inputan anda salah, silahkan ulangi\n")
            pilihan = input("ingin menghapus edge matrix lagi? ya/tidak:")


def ask_delete_vertex_list():
    pilihan = input("ingin menghapus vertex list? ya/tidak:")
    while pilihan != 'ya' and pilihan != 'tidak':
        print("Inputan anda salah, silahkan ulangi\n")
        pilihan = input("ingin menghapus vertex list? ya/tidak:")
    while pilihan == 'ya':
        delete_vertex = input("\ninputkan vertex list yang ingin di delete:")
        delete_vertex_list(delete_vertex)
        print("Graph adjacency list terbaru:", graph_list, "\n")
        pilihan = input("ingin menghapus vertex list lagi? ya/tidak:")
        while pilihan != 'ya' and pilihan != 'tidak':
            print("Inputan anda salah, silahkan ulangi\n")
            pilihan = input("ingin menghapus vertex list lagi? ya/tidak:")


def ask_delete_edge_list():
    pilihan = input("ingin menghapus edge list? ya/tidak:")
    while pilihan != 'ya' and pilihan != 'tidak':
        print("Inputan anda salah, silahkan ulangi\n")
        pilihan = input("ingin menghapus edge list? ya/tidak:")
    while pilihan == 'ya':
        delete_edge = input("\ninputkan edge list yang ingin di delete:")
        while len(delete_edge) != 2:
            print("inputan salah silahkan ulangi\n")
            delete_edge = input("\ninputkan edge list yang ingin di delete:")
        delete_edge_matrix(delete_edge[0],delete_edge[1])
        print("Graph adjacency list terbaru:", graph_list, "\n")
        pilihan = input("ingin menghapus edge list lagi? ya/tidak:")
        while pilihan != 'ya' and pilihan != 'tidak':
            print("Inputan anda salah, silahkan ulangi\n")
            pilihan = input("ingin menghapus edge list lagi? ya/tidak:")


def graph_adj_matrix():
    boolean = True
    while boolean:
        vertex_matrix = input("\nInputkan Vertexnya:")
        add_vertex_matrix(vertex_matrix)

        pilihan = input("\nIngin menambah Vertex lagi? ya/tidak:")
        boolean = ask_menambah_vertex(pilihan)

    boolean = True
    while boolean:
        print("Inputkan Vertex yang ingin diberi Edge dan Inputkan Bobot-nya")
        vertex_asal = input("\nVertex Asal:")
        vertex_tujuan = input("\nVertex Tujuan:")
        bobot = int(input("\nBobot:"))
        add_edge_matrix(vertex_asal, vertex_tujuan, bobot)

        pilihan = input("\nIngin menambah Edge lagi? ya/tidak:")
        boolean = ask_menambah_edge(pilihan)


def graph_adj_list():
    boolean = True
    while boolean:
        vertex_list = input("\nInputkan Vertexnya:")
        add_vertex_list(vertex_list)

        pilihan = input("\nIngin menambah Vertex lagi? ya/tidak:")
        boolean = ask_menambah_vertex(pilihan)

    boolean = True
    while boolean:
        print("Inputkan Vertex yang ingin diberi Edge dan Inputkan Bobot-nya")
        vertex_asal = input("\nVertex Asal:")
        vertex_tujuan = input("\nVertex Tujuan:")
        bobot = int(input("\nBobot:"))
        add_edge_list(vertex_asal, vertex_tujuan, bobot)

        pilihan = input("\nIngin menambah Edge lagi? ya/tidak:")
        boolean = ask_menambah_edge(pilihan)


def graph_adj_matrix_dan_list():
    boolean = True
    while boolean:
        vertex_list = input("\nInputkan Vertexnya:")
        add_vertex_matrix(vertex_list)
        add_vertex_list(vertex_list)

        pilihan = input("\nIngin menambah Vertex lagi? ya/tidak:")
        boolean = ask_menambah_vertex(pilihan)

    boolean = True
    while boolean:
        print("Inputkan Vertex yang ingin diberi Edge dan Inputkan Bobot-nya")
        vertex_asal = input("\nVertex Asal:")
        vertex_tujuan = input("\nVertex Tujuan:")
        bobot = int(input("\nBobot:"))
        add_edge_matrix(vertex_asal, vertex_tujuan, bobot)
        add_edge_list(vertex_asal, vertex_tujuan, bobot)

        pilihan = input("\nIngin menambah Edge lagi? ya/tidak:")
        boolean = ask_menambah_edge(pilihan)


def ask_menambah_vertex(pilihan):
    while pilihan != 'tidak' and pilihan != 'ya':
        print("inputan yang anda masukkan salah")
        pilihan = input("\nIngin menambah Vertex lagi? ya/tidak:")
    if pilihan == 'tidak':
        return False
    elif pilihan == 'ya':
        return True


def ask_menambah_edge(pilihan):
    while pilihan != 'tidak' and pilihan != 'ya':
        print("inputan yang anda masukkan salah\n")
        pilihan = input("\nIngin menambah Edge lagi? ya/tidak:")
    if pilihan == 'tidak':
        return False
    elif pilihan == 'ya':
        return True


def add_vertex_matrix(v):
    global jumlah_vertex
    if v in Vertex:
        print("\n", v, 'sudah ada di graph')
    else:
        Vertex.append(v)
        jumlah_vertex += 1
        for i in graph:
            i.append(0)
        baris_baru = []
        for j in range(jumlah_vertex):
            baris_baru.append(0)
        graph.append(baris_baru)


def add_edge_matrix(v1, v2, bobot):
    if v1 not in Vertex or v2 not in Vertex:
        print('Vertex tidak ada di graph')
    else:
        idx1 = Vertex.index(v1)
        idx2 = Vertex.index(v2)
        graph[idx1][idx2] = bobot


def delete_vertex_matrix(v):
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


def delete_edge_matrix(v1, v2):
    if v1 not in Vertex or v2 not in Vertex:
        print('Vertex tidak ada di graph_adjacency_matrix')
    else:
        idx1 = Vertex.index(v1)
        idx2 = Vertex.index(v2)
        graph[idx1][idx2] = 0
        graph[idx2][idx1] = 0


def print_graph_matrix():
    global jumlah_vertex
    print(Vertex)
    for i in range(jumlah_vertex):
        for j in range(jumlah_vertex):
            print(graph[i][j], end=' ')
        print()


def add_vertex_list(v):
    if v in graph_list:
        print('vertex sudah ada di graph')
    else:
        graph_list[v] = []


def add_edge_list(v1, v2, bobot):
    if v1 not in graph_list or v2 not in graph_list:
        print('vertex tidak ada di graph')
    else:
        graph_list[v1].append(v2)
        graph_list[v1].append(bobot)


def delete_vertex_list(v):
    if v in graph_list:
        graph_list.pop(v)
        for key, value in graph_list.items():
            if v in value:
                value.remove(v)
    else:
        print('vertex tidak ada di graph')


def delete_edge_list():
    v2 = input("Masukkan v2 yang ingin dihilangkan:")
    bobot = input("Masukkan bobot yang ingin dihilangkan:")
    if v2 not in graph_list or bobot not in graph_list:
        print('vertex tidak ada di graph')
    else:
        graph_list[v2].remove(bobot)
        graph_list[bobot].remove(v2)
