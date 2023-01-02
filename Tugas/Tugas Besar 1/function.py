# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

import csv

#fungsi untuk menghitung banyak kapal (berangkat/tiba) dan penumpang (naik/turun) secara keseluruhan
def ttlKapaldanTtlPenupang(list,idx):
    i = 0
    total = 0
    while i < len(list):
        total += list[i][idx]
        i += 1

    if idx == 2:
        print('total kapal berangkat keseluruhan adalah :', total)
    elif idx == 3:
        print('total kapal tiba keseluruhan adalah :', total)
    elif idx == 4:
        print('total penumpang naik keseluruhan adalah :', total)
    elif idx == 5:
        print('total penumpang turun keseluruhan adalah :', total)
    else :
        print('index yang anda masukkan salah')



#fungsi untuk mengubah list index ke-i menjadi int
def ubahTypeDataKeInteger(list,idx):
    i = 0
    while i < len(list):
        list[i][idx] = int(list[i][idx])
        i += 1

#fungsi untuk menghitung jumlah penumpang naik/turun di tiap pelabuhan
def pnpTiapPlbh(list):
    i = True
    while i == True:
        if list[1][0] == "P. MUARA ANGKE":
            list[0][1] += list[1][1]
            list.pop(1)
        elif list[2][0] == "MARINA ANCOL":
            list[1][1] += list[2][1]
            list.pop(2)
        elif list[3][0] == "UNTUNG JAWA":
            list[2][1] += list[3][1]
            list.pop(3)
        elif list[4][0] == "LANCANG":
            list[3][1] += list[4][1]
            list.pop(4)
        elif list[5][0] == "PARI":
            list[4][1] += list[5][1]
            list.pop(5)
        elif list[6][0] == "TIDUNG/PAYUNG":
            list[5][1] += list[6][1]
            list.pop(6)
        elif list[7][0] == "PRAMUKA/PANGGANG":
            list[6][1] += list[7][1]
            list.pop(7)
        elif list[8][0] == "KELAPA":
            list[7][1] += list[8][1]
            list.pop(8)
        elif list[9][0] == "HARAPAN":
            list[8][1] += list[9][1]
            list.pop(9)
        elif list[10][0] == "SABIRA":
            list[9][1] += list[10][1]
            list.pop(10)
        if len(list) == 10:
            i = False

    return list

def mergesort_asc(A,id):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergesort_asc(L,id)
        mergesort_asc(R,id)
        i = j = k = 0
        while i < len(L) and j < len(R):
                if L[i][id] < R[j][id]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
        return A
