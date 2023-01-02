# Tyan Nur Khollis
# 41520010057

from Problem1 import *

listC = acak(10, 100, 10)

if listC[0] <= listC[len(listC)-1]:
    listC = bubble_asc(listC)
    print("List Bubble Ascending:", listC)
elif listC[0] > listC[len(listC)-1]:
    listC = bubble_desc(listC)
    print("List Bubble Descending:", listC)
