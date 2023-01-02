# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    List3 = []
    for row in csv_reader:
        row.pop(0) # Menghapus kolom tanggal
        row.pop(1) # Menghapus kolom kapal_berangkat
        row.pop(1) # Menghapus kolom kapal_tiba
        row.pop(1) # Menghapus kolom penumpang_naik
        List3.append(row) # Memindahkan baris dari csv_reader ke dalam List3

label3 = List3.pop(0) # Menyimpan List3 baris 1 ke variabel label2

ubahTypeDataKeInteger(List3, 1) # Mengubah type data dari string ke integer pada kolom penumpang_turun
pnpTiapPlbh(List3) # Menghitung jumlah penumpang turun di tiap pelabuhan
print("Jumlah penumpang turun di tiap pelabuhan :", List3, '\n')

mergesort_asc(List3, 1) # Mengurutkan secara ascending
print("Data Setelah diurutkan berdasarkan jumlah penumpang turun :", List3, '\n')

idx_terakhir = len(List3)-1 # Menyimpan index terakhir List3
print("Pelabuhan dengan penumpang turun terbanyak yaitu", List3[idx_terakhir][0], "dengan jumlah penumpang turun :", List3[idx_terakhir][1])