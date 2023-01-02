# Tyan Nur Khollis
# 41520010057

import random


def bubble_asc(a):  # fungsi bubble sort ascending
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def bubble_desc(a):     # fungsi bubble sort descending
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def acak(n, m, k):     # fungsi untuk membuat list integer secara acak
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
