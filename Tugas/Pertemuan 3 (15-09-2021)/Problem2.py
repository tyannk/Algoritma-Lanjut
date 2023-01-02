# Tyan Nur Khollis
# 41520010057

from Problem1 import *

#Problem 2 nomor 1
List1 = Bil_Bulat(1,100,10)
print("List1 Bilangan Bulat         :",List1)

#Problem 2 nomor 2
List2 = Bil_Bulat(400,500,20)
print("List2 Bilangan Bulat         :",List2)

#Problem 2 nomor 3
List3 = List1+List2
print("List3                        :",List3)

#Problem 2 nomor 4
print("Bilangan Ganjil dari list 3  :",Bil_Ganjil(List3))

#Problem 2 nomor 5
print("Bilangan Genap dari list 3   :",Bil_Genap(List3),"\n")

#Problem 2 nomor 6
string = list_int_to_string(Bil_Ganjil(List3))
print("Konversi list bilangan bulat ganjil menjadi string   :",string)
print("Type data index ke 1                                 :",type(string[1]))


