# Anggota Kelompok NIM - Nama Lengkap
# 41520010201 - Ganendra Ekapradhana
# 41520010057 - Tyan Nur Khollis
# 41520010217 -  Bulan Suci Rama Dhini


from Function import *

ListBarang = [[21,'Sampo',43000], [18,'Sabun',28000],
[9,'Detergent',21000], [2,'Pasta Gigi',18000],
[6,'Sikat Gigi',12000],[24,'Tissue',8000],
[5,'Handuk',78000],[15,'Gayung',17500],
[28,'Conditioner',31000],[1,'Sabun Tangan',19000]]


print("Pilih Pencarian:")
print("1.Pencarian ID")
print("2.Pencarian nama barang\n")
nomor = int(input("input nomor:"))

if nomor == 1:
    id = int(input("Ingin mencari id berapa?:"))
    hasil = sequentialSearch(ListBarang, id)
    if hasil >= 0:
        print("id berhasil ditemukan pada index ke-",hasil)
    else:
        print("id tidak ditemukan")
elif nomor == 2:
    ListBarang = mergesort_asc(ListBarang, 1)
    print("nama barang setelah diurutkan:",ListBarang)
    barang = input("Ingin mencari barang apa?:")
    hasil = binarySearch(ListBarang,barang,0,1)
    if hasil >= 0:
        print("Barang berhasil ditemukan pada index ke-",hasil)
    else:
        print("Barang tidak ditemukan")
