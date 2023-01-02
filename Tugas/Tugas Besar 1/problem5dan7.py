# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    List2 = []
    for row in csv_reader:
        row.pop(0) # Menghapus kolom tanggal
        row.pop(1) # Menghapus kolom kapal_berangkat
        row.pop(1) # Menghapus kolom kapal_tiba
        row.pop(2) # Menghapus kolom penumpang turun
        List2.append(row) # Memindahkan baris dari csv_reader ke dalam List2

label2 = List2.pop(0) # Menyimpan List2 baris 1 ke variabel label2

ubahTypeDataKeInteger(List2, 1) # Mengubah type data dari string ke integer pada kolom penumpang_naik
pnpTiapPlbh(List2)  # Menghitung jumlah penumpang naik di tiap pelabuhan
print("Jumlah penumpang naik di tiap pelabuhan :", List2, '\n')

mergesort_asc(List2, 1) #mengurutkan secara ascending
print("Data Setelah diurutkan berdasarkan jumlah penumpang naik :", List2, '\n')

idx_terakhir = len(List2)-1 # Menyimpan index terakhir List2
print("Pelabuhan dengan penumpang naik terbanyak yaitu", List2[idx_terakhir][0], "dengan jumlah penumpang naik :", List2[idx_terakhir][1])