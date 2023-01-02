# Anggota Kelompok NIM - Nama Lengkap
# 41520010201 - Ganendra Ekapradhana
# 41520010057 - Tyan Nur Khollis
# 41520010217 -  Bulan Suci Rama Dhini


from Function import *


List =  [[21,'Sampo',43000], [18,'Sabun',28000],
[9,'Detergent',21000], [2,'Pasta Gigi',18000],
[6,'Sikat Gigi',12000],[24,'Tissue',8000],
[5,'Handuk',78000],[15,'Gayung',17500],
[28,'Conditioner',31000],[1,'Sabun Tangan',19000]]

print('Pilih Pengurutan:')
print('1. id terkecil ke terbesar')
print('2. id besar ke terkecil')
print('3. Nama barang a ke z')
print('4. Nama barang z ke a')
print('5. Harga barang termurah ke termahal')
print('6. Harga barang termahal ke termurah')
print('Pilih angka: ', end= ' ' )
angka = input()

if angka=='1':
    print(mergesort_asc(List, 0))
elif angka=='2':
    print(mergesort_desc(List, 0))
elif angka=='3':
    print(mergesort_asc(List, 1))
elif angka == '4':
    print(mergesort_desc(List, 1))
elif angka =='5':
    print(mergesort_asc(List, 2))
elif angka =='6':
    print(mergesort_desc(List, 2))
