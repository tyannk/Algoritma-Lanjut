# Tyan Nur Khollis
# 41520010057


import random
def Bil_Bulat(n,m,k):
    return random.sample(range(n,m+1),k)

def Bil_Ganjil(list):
    List = []
    for i in list:
        if( i%2==1 ):
            List.append(i)
    List.sort()
    return List

def Bil_Genap(list):
    List = []
    for i in list:
        if (i % 2 == 0):
            List.append(i)
    List.sort()
    List.reverse()
    return List

def list_int_to_string(list):
    List=[]
    for i in list:
        List.append(str(i))
    return List