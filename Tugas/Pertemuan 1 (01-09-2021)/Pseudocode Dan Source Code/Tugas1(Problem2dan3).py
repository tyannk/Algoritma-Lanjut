# Nama : Tyan Nur Khollis
# NIM  : 41520010057

#Pseudocode Problem 1 :
"""
if nilai >= 90
    grade = A
elif nilai >= 70
    grade = B
elif nilai >= 50
    grade = C
elif nilai >= 40
    grade = D
else
    grade = E
"""

# Problem 2 Fungsi dari Problem 1:
def Problem1(nilai):
    if nilai >= 90:
        grade = "A"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 50:
        grade = "C"
    elif nilai >= 40:
        grade = "D"
    else :
        grade = "E"
    return grade

"""
Problem 3, Membuat program Python untuk menentukan grade dari masing" nilai menggunakan 
pengulangan dan fungsi pada problem 2:
"""
nilai = [95,55,90,70,80,40,20,65]
for x in nilai:
    print("nilai=",x," grade=",Problem1(x))

