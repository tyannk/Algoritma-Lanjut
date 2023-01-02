from problem2 import *

L = []
i = 0

while True:
    try:
        el = int(input('Masukkan elemen list index ke-' + str(i) + ':'))
        if (el==0):
            break
        else:
            L.append(el)
            i += 1
    except ValueError:
        print('Bukan bilangan bulat!')

print('List terbentuk:', L)
Jumlah = jumlah(L)
print('Jumlah = ', Jumlah)
Ratarata = ratarata((L))
print('Rata-rata =', Ratarata)

Median = median(L)
print('Median = ', Median)
MinL = terkecil(L)
MaxL = terbesar(L)
print('List utama =', L)
print('Nilai terkecil = ', MinL)
print('Nilai terbesar = ', MaxL)