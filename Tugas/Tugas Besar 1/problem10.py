# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    List5 = []
    for row in csv_reader:
        row.pop(2)  # Menghapus kolom kapal_berangkat
        row.pop(3)  # Menghapus kolom penumpang_naik
        row.pop(3)  # Menghapus kolom penumpang_turun
        if row[2] == '0' or row[0] == 'tanggal':
            List5.append(row)# Memindahkan baris dari csv_reader ke List5

label5 = List5.pop(0)
ubahTypeDataKeInteger(List5, 2)# Mengubah Type data dari string ke integer pada kolom kapal_tiba
print("Data Pelabuhan yang tidak ada kedatangan kapal:", List5)

while len(List5) != 2:
    if List5[1][1] == 'HARAPAN':
        List5.pop(0)
    elif List5[1][1] == 'SABIRA':
        List5.pop(1)

print("Pelabuhan yang tidak memiliki kedatangan kapal adalah pelabuhan", List5[0][1], "dan", List5[1][1])