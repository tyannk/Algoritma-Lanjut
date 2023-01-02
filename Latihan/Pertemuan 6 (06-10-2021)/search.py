def sequentialSearch(List, item):
    idx = 0
    found = False
    while idx < len(List) and not (found):
        if List[idx] == item:
            found = True
        else:
            idx += 1
    if not (found):
        return -1
    else:
        return idx




def binarySearch(List, item, idx0):
    if len(List)==0:
        return -1
    else:
        mid= len(List)//2
        print('Mid=', mid)
        if List[mid]==item:
            #print('idx0', idx0)
            return (idx0+mid)
        elif List[mid]>item:
            print('List Kiri:', List[:mid])
            return binarySearch(List[:mid],item, idx0)
        else: # List[mid] < item
            idx0 = mid+1
            print('idx0', idx0)
            print('List Kanan:',  List[idx0:])
            return binarySearch(List[idx0:], item, idx0)
