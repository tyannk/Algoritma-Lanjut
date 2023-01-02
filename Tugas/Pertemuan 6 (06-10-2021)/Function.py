# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini


def sequentialSearch(List, item):
    idx = 0
    found = False
    while idx < len(List) and not (found):
        if List[idx][0] == item:
            found = True
        else:
            idx += 1
    if not (found):
        return -1
    else:
        return idx

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

def binarySearch(List, item, idx0,idx):
    if len(List) == 0:
        return -1
    else:
        mid = len(List)//2
        if List[mid][idx]==item:
            #print('idx0', idx0)
            return (idx0+mid)
        elif List[mid][idx]>item:
            return binarySearch(List[:mid],item, idx0,idx)
        else: # List[mid] < item
            idx0 = mid+1
            return binarySearch(List[idx0:], item, idx0,idx)
