import random
from search import *


def main():
    List = random.sample(range(1,20),10)
    List.sort()
    print('List= ', List)
    foundinidx = binarySearch(List, 3,0)
    if foundinidx == -1:
        print('Elemen tidak ditemukan')
    else:
        print('Elemen ditemukan di index', foundinidx)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

