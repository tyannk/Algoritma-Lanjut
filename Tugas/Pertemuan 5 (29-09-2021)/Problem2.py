# Anggota Kelompok NIM - Nama Lengkap
# 41520010201 - Ganendra Ekapradhana
# 41520010057 - Tyan Nur Khollis
# 41520010217 -  Bulan Suci Rama Dhini


from Function import *
from Problem1 import L


print("\nMEMBUAT LIST BARU")
list_Int = list_baru(5)
list_Int.extend(L)
print("list setelah digabungkan dengan list dari problem 1:",list_Int)
if list_Int[len(list_Int)-1] % 2 == 1:
    idx = 0
    for i in list_Int:
        list_Int[idx] = i * 3
        idx += 1
    selectionsort_asc(list_Int)
    print("list setelah dikali 3 dan dirutkan menggunakan selection sort ascending:", list_Int)
else:
    idx = 0
    for i in list_Int:
        list_Int[idx] = i * 2
        idx += 1
    selectionsort_desc(list_Int)
    print("list setelah dikali 2 dan dirutkan menggunakan selection sort descending:", list_Int)

