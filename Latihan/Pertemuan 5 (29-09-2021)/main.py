from sorting import *

def main():
    List = [['Pulpen',1500],['Tipe-X',6000],['Pensil',2000],
            ['Map',30000],['Spidol',5500],['Lakban',6500],
            ['Buku',3000],['Gunting',4000],['Jangka',25000],
            ['Buku Gambar',13000],['Pensil Warna',85000]]

    print('Pilih Pengurutan:')
    print('1. Nama barang a ke z')
    print('2. Nama barang z ke a')
    print('3. Harga barang termurah ke termahal')
    print('4. Harga barang termahal ke termurah')
    print('Pilih angka: ', end= ' ' )
    angka = input()

    if angka=='1':
        List = selectionsortA(List,0)
    elif angka=='2':
        List = selectionsortD(List,0)
    elif angka=='3':
        List = selectionsortA(List,1)
    elif angka == '4':
        List = selectionsortD(List, 1)

    print('Nama barang \t \t Harga ')
    for i in range(len(List)):
        print(List[i][0], '\t \t', List[i][1])



if __name__ == '__main__':
    main()



