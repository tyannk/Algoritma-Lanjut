# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*

print("====== PROGRAM SEDERHANA UNTUK MEMBUAT WEIGHTED DIRECTED GRAPH =====")
print("===== DENGAN REPRESENTASI ADJACENCY MATRIX ATAU ADJECENCY LIST  ====")

print("Ingin membuat Graph dengan representasi apa?")
print("Pilihan:")
print("1. Adjacency Matrix")
print("2. Adjacency List")
print("3. Adjecancy Matrix dan List")
pilihan = input("Input Nomor Pilihan :")


if pilihan == '1':
    graph_adj_matrix()
    print("\nVertex matrix:", Vertex)
    print("Graph adjacency matrix:", graph, "\n")
    ask_delete_vertex_matrix()
    ask_delete_edge_matrix()
elif pilihan == '2':
    graph_adj_list()
    print("Graph adjacency List:", graph_list)
    ask_delete_vertex_list()
    ask_delete_edge_list()
elif pilihan == '3':
    graph_adj_matrix_dan_list()
    print("\nVertex matrix:", Vertex)
    print("Graph adjacency matrix:", graph)
    print("Graph adjacency List:", graph_list,"\n")
    ask_delete_vertex_matrix()
    ask_delete_edge_matrix()
    ask_delete_vertex_list()
    ask_delete_edge_list()
    print("\nVertex matrix:", Vertex)
    print("Graph adjacency matrix:", graph)
    print("Graph adjacency List:", graph_list, "\n")
else:
    print("Inputan anda salah")


