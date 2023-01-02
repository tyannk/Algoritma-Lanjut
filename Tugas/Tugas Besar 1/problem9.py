# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    List4 = []
    for row in csv_reader:
        row.pop(3)# Menghapus kolom kapal_tiba
        row.pop(3)# Menghapus kolom penumpang_naik
        row.pop(3)# Menghapus kolom penumpang_turun
        if row[2] == '0' or row[0] == 'tanggal':
            List4.append(row)

label4 = List4.pop(0)
ubahTypeDataKeInteger(List4, 2)# Mengubah Type data dari string ke integer pada kolom kapal_berangkat
print("Data Pelabuhan yang tidak ada keberangkatan kapal:", List4)

while len(List4) != 2:
    if List4[1][1] == 'HARAPAN':
        List4.pop(0)
    elif List4[1][1] == 'SABIRA':
        List4.pop(1)

print("Pelabuhan yang tidak memiliki kedatangan kapal adalah pelabuhan", List4[0][1], "dan", List4[1][1])