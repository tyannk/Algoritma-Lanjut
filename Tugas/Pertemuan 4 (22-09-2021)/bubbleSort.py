def bubblesortA(A):
    n = len(A)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if (A[j] > A[j+1]):
                A[j],A[j+1] = A[j+1],A[j] #swap
                swapped = True


        if swapped == False:
            break

    return A


def bubblesortD(A):
    n = len(A)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if (A[j] < A[j+1]):
                A[j],A[j+1] = A[j+1],A[j] #swap
                swapped = True

        if swapped == False:
            break

    return A

def inputList(L,n):
    for i in range(n):
        try:
            el = int(input('Masukkan elemen list index ke-' + str(i) + ':'))
            L.append(el)
            i += 1
        except ValueError:
            print('Bukan bilangan bulat!')

    return L