# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*

add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')
add_vertex('F')
add_vertex('G')
add_vertex('Z')

add_edge('A', 'B', 4)
add_edge('A', 'D', 3)
add_edge('A', 'E', 4)
add_edge('B', 'C', 5)
add_edge('C', 'Z', 10)
add_edge('D', 'C', 6)
add_edge('D', 'Z', 8)
add_edge('D', 'G', 8)
add_edge('D', 'E', 2)
add_edge('E', 'F', 4)
add_edge('F', 'G', 3)
add_edge('G', 'Z', 8)

print("Graph:", graph)
d, pre = dijkstra('A')

print("Distance:", d)
print("Pendahulu:", pre)




