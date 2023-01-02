import random
from bubbleSort import *

L = random.sample(range(1,100),10)
print('List = ', L)
ListA = bubblesortA(L)
print('ListA= ', ListA)
ListD = bubblesortD(L)
print('ListD= ', ListD)


ListM = inputList(ListD, 5)
print('ListM= ', ListM)
ListM = bubblesortD(ListM)
print('ListM= ', ListM)

Li = random.sample(range(10,100),10)
print('Li=', Li)
if Li[0] < Li[len(Li)-1]:
    Li = bubblesortA(Li)
else:
    Li = bubblesortD(Li)
print('Li=', Li)