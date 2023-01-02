# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import*
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    List = []
    for row in csv_reader:
        List.append(row)

label1 = List.pop(0)

# Memanggil fungsi untuk mengubah type data string ke integer dari index yang berisi data kapal berangkat,kapal tiba, penumpang naik, dan penumpang turun
ubahTypeDataKeInteger(List,2)
ubahTypeDataKeInteger(List,3)
ubahTypeDataKeInteger(List,4)
ubahTypeDataKeInteger(List,5)

# Memanggil fungsi untuk menghitung total dari kapal_berangkat,kapal tiba, penumpang naik, dan penumpang turun
ttlKapaldanTtlPenupang(List,2)
ttlKapaldanTtlPenupang(List,3)
ttlKapaldanTtlPenupang(List,4)
ttlKapaldanTtlPenupang(List,5)