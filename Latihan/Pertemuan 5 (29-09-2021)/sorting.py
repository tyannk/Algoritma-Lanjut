def selectionsortA(A,idx):
    # nama barang : idx 0
    # harga : idx 1

    # Melalui semua elemen pada list
    for i in range(len(A)):

        # Cari elemen terkecil dari bagian yang belum terurut
        # index terpilih sebagai elemen terkecil: inisialisasi elemen index i
        min_idx = i

        # Bagian belum terutut:
        for j in range(i + 1, len(A)):
            # jika elemen dari index terpilih lebih besar dari elemen index j
            # maka index j jadi index terpilih
            if A[min_idx][idx] > A[j][idx]:
                min_idx = j

        # swap elemen terkecil dengan elemen terkiri dari bagian belum terurut
        A[i], A[min_idx] = A[min_idx], A[i]
        print(A, i, min_idx)
    return A


def selectionsortD(A, idx):
    # nama barang : idx 0
    # harga : idx 1

    # Melalui semua elemen pada list
    for i in range(len(A)):

        # Cari elemen terkecil dari bagian yang belum terurut
        # index terpilih sebagai elemen terkecil: inisialisasi elemen index i
        max_idx = i

        # Bagian belum terutut:
        for j in range(i + 1, len(A)):
            # jika elemen dari index terpilih lebih besar dari elemen index j
            # maka index j jadi index terpilih
            if A[max_idx][idx] < A[j][idx]:
                max_idx = j

        # swap elemen terkecil dengan elemen terkiri dari bagian belum terurut
        A[i], A[max_idx] = A[max_idx], A[i]
        print(A, i, max_idx)
    return A


def bubblesort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if (A[j] > A[j+1]):
                A[j],A[j+1] = A[j+1],A[j] #swap   x,y = y,x
                swapped = True
            print('List ', A, i, j)
        if swapped == False:
            break
    return A

def selectionsort(A):
    # Melalui semua elemen pada list
    for i in range(len(A)):

        # Cari elemen terkecil dari bagian yang belum terurut
        # index terpilih sebagai elemen terkecil: inisialisasi elemen index i
        min_idx = i

        # Bagian belum terutut:
        for j in range(i + 1, len(A)):
            # jika elemen dari index terpilih lebih besar dari elemen index j
            # maka index j jadi index terpilih
            if A[min_idx] > A[j]:
                min_idx = j

        # swap elemen terkecil dengan elemen terkiri dari bagian belum terurut
        A[i], A[min_idx] = A[min_idx], A[i]
        print(A, i, min_idx)
    return A



def insertionSort(A):
    # Iterasi dimulai dari index 1 sampai index terakhir
    for i in range(1, len(A)):

        el = A[i] #elemen index i

        # Pindahkan elemen A[0..i-1],
        # jika nilainya lebih besar dari el,
        # ke posisi kanannya

        j = i - 1
        while j >= 0 and el < A[j]:
            print(A, i, j, el)
            A[j + 1] = A[j]

            j -= 1

        A[j + 1] = el
        print(A,i,j, el)
    return A




def mergeSort(A):
    if len(A) > 1:

        # Temukan titik tengah list
        mid = len(A) // 2

        # Bagi dua elemen: setengah kiri
        L = A[:mid]
        print("L", L)

        # setengah kanan
        R = A[mid:]
        print("R", R)

        # Rekursif untuk setengah list kiri
        mergeSort(L)

        # Rekursif untuk setengah list kanan
        mergeSort(R)

        i = j = k = 0

        # Tahap penggabungan dan pengurutan
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1


        # Pengecekan apakah masih ada elemen tersisa
        # Untuk elemen yang tidak punya pasangan L atau R-nya
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

        print(A,L,R)
        return A

