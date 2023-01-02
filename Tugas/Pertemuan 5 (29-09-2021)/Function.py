# Anggota Kelompok NIM - Nama Lengkap
# 41520010201 - Ganendra Ekapradhana
# 41520010057 - Tyan Nur Khollis
# 41520010217 -  Bulan Suci Rama Dhini


import random


def insertionsort_asc(A):
    for i in range(1, len(A)):
        el = A[i]
        j = i - 1
        while j >= 0 and el < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el
    return A


def insertionsort_desc(A):
    for i in range(1, len(A)):
        el = A[i]
        j = i - 1
        while j >= 0 and el > A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el
    return A


def selectionsort_asc(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


def selectionsort_desc(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] < A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


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

def mergesort_desc(A,id):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergesort_desc(L,id)
        mergesort_desc(R,id)
        i = j = k = 0
        while i < len(L) and j < len(R):
                if L[i][id] > R[j][id]:
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


def acak(n, m, k):     # fungsi untuk membuat sample list acak
    a = random.sample(range(n, m), k)
    return a

def list_baru(n):
    newlist = []
    i = 0
    while i < n:
        print("Inputkan isi index ke-", i)
        integer = int(input("input:"))
        newlist.append(integer)
        i += 1
    return newlist