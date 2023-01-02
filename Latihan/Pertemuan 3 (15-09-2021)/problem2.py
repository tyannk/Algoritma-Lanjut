#Jumlah
#rata-rata
#median (nilai tengah)
# nilai terkecil
#nilai terbesar

def jumlah(List):
    sumL = 0
    for i in List:
        sumL += i     # sumL = sumL + i

    return sumL

def ratarata(List):
    rata2L = jumlah(List)/(len(List))
    return rata2L

def median(List):
    List.sort()
    print('List Terurut: ', List)
    if(len(List)%2 == 0):
        medL = (List[int(len(List)/2)] + List[int(len(List)/2)-1])/2
    else:
        medL = (List[int(len(List)/2)])

    return medL

def terkecil(List):
    List.sort()
    minL = List[0]

    return minL

def terbesar(List):
    List.sort()
    maxL = List[len(List)-1]

    return maxL