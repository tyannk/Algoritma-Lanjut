# Anggota Kelompok NIM - Nama Lengkap
# 41520010201 - Ganendra Ekapradhana
# 41520010057 - Tyan Nur Khollis
# 41520010217 -  Bulan Suci Rama Dhini


from Function import *


L = acak(1, 100, 20)
print("list acak:", L)
if L[0] % 2 == 1:
    L = insertionsort_asc(L)
    print("list setelah diurutkan dengan insertion sort ascending:", L)
else:
    L = insertionsort_desc(L)
    print("list setelah diurutkan dengan insertion sort descending:", L)
