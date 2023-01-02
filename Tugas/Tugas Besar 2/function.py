# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from search import *

pilihan = 0
pilihan_admin = '2'
kota_berangkat = ''
tgl_brkt = ''
kota_tujuan = ''
nama = ''
no_id = 0
jml_pnp = 0
jml_pnp_dewasa = 0
konfirmasi = ''
id_resi = 1


def login():
    global pilihan
    print("=====SILAHKAN LOGIN TERLEBIH DAHULU=====")
    print("INGIN LOGIN SEBAGAI APA?")
    print("1. Pembeli")
    print("2. Admin\n")
    pilihan = input("Inputkan nomor:")
    while pilihan != '1' and pilihan != '2':
        print("\nInputan anda salah, silahkan ulangi!")
        pilihan = input("Inputkan nomor:")
    return pilihan


def pembeli():
    global pilihan, kota_berangkat, kota_tujuan, nama, no_id, jml_pnp_dewasa, jml_pnp, konfirmasi, tgl_brkt, id_resi, l_id_resi
    print("\nNama-Nama Kota :", Vertex)

    kota_berangkat = input("\nInputkan kota keberangkatan:")
    idx = sequentialSearch(Vertex, kota_berangkat)
    while idx == -1:
        print("\nInputan anda salah, silahkan ulangi!")
        kota_berangkat = input('Inputkan kota keberangkatan:')
        idx = sequentialSearch(Vertex, kota_berangkat)

    kota_tujuan = input("\nInputkan kota tujuan:")
    idx = sequentialSearch(Vertex, kota_tujuan)
    while idx == -1:
        print("\nInputan anda salah, silahkan ulangi!")
        kota_tujuan = input('Inputkan kota tujuan:')
        idx = sequentialSearch(Vertex, kota_tujuan)

    tgl_brkt = input("\nInputkan tanggal keberangkatan:")

    jml_pnp = int(input("\nInputkan jumlah penumpang:"))
    while jml_pnp <= 0:
        print("\nInputan anda kurang <= nol/salah, silahkan ulangi!")
        jml_pnp = input('Inputkan jumlah penumpang:')

    distance, jalur = dijkstra_terdekat(kota_berangkat, kota_tujuan)
    harga = total_harga(jalur)
    print("REKOMENDASI MODE TRANSPORTASI\n")
    print("Nomor 1:")
    print("Jarak terdekat:", distance[kota_tujuan])
    print("Jalur terdekat transit di kota:", jalur)
    print("Harga =", harga*jml_pnp, "euro\n")

    price, jalur_termurah = dijkstra_termurah(kota_berangkat, kota_tujuan)
    print("Nomor 2:")
    print("Harga termurah", price[kota_tujuan]*jml_pnp, "euro")
    print("Transit di kota:", jalur_termurah, "\n")

    print("Ingin memilih Mode Transportasi Nomor 1 atau 2?")
    pilihan = input("Jawab:")
    while pilihan != '1' and pilihan != '2':
        print("\nInputan anda salah, silahkan ulangi!")
        pilihan = input("Jawab:")

    jml_pnp_dewasa = int(input("\nBerapa jumlah penumpang dewasa? :"))
    while jml_pnp_dewasa > jml_pnp or jml_pnp_dewasa <= 0:
        print("Jumlah penumpang dewasa yang anda input melebihi total jumlah penumpang/kurang dari sama dengan nol")
        print("Silahkan menginput ulang\n")
        jml_pnp_dewasa = int(input("Berapa jumlah penumpang dewasa? :"))

    print("\nINPUT DATA PENUMPANG")
    while len(temp_pnp_dewasa) < int(jml_pnp_dewasa):
        print("\nPenumpang dewasa")
        nama = input("Nama:")
        no_id = int(input("Nomor Identitas:"))
        add_temp_pnp_dewasa(nama, no_id)

    if jml_pnp_dewasa < jml_pnp:
        while (len(temp_pnp_dewasa) + len(temp_pnp_anak)) < int(jml_pnp):
            print("\nPenumpang anak")
            nama = input("Nama:")
            no_id = int(input("Nomor Identitas:"))
            add_temp_pnp_anak(nama, no_id)

    print("\nPilihan penumpang:")
    if pilihan == '1':
        print("Jalur:", jalur)
    else:
        print("Jalur:", jalur_termurah)
    print("Data penumpang:")
    for i in range(len(temp_pnp_dewasa)):
        print("No Identitas:", temp_no_id_pnp_dws[i])
        print("Nama:", temp_pnp_dewasa[i], "\n")
    for i in range(len(temp_pnp_anak)):
        print("No Identitas:", temp_no_id_pnp_ank[i])
        print("Nama:", temp_pnp_anak[i], "\n")

    print("\nKONFIRMASI PEMBELIAN")
    konfirmasi = input("OK/TIDAK, Jawab:")
    while konfirmasi != 'OK' and konfirmasi != 'TIDAK':
        print("Jawaban anda salah, silahkan ulangi \n")
        konfirmasi = input("OK/TIDAK, Jawab:")

    if konfirmasi == 'OK':
        while len(temp_pnp_dewasa) > 0:
            add_pnp_dewasa(temp_pnp_dewasa[0], temp_no_id_pnp_dws[0])
            temp_pnp_dewasa.pop(0)
            temp_no_id_pnp_dws.pop(0)
        while len(temp_pnp_anak) > 0:
            add_pnp_anak(temp_pnp_anak[0], temp_no_id_pnp_ank[0])
            temp_pnp_anak.pop(0)
            temp_no_id_pnp_ank.pop(0)
        print("\n=====RESI PEMBELIAN=====")
        print("ID_RESI                :", id_resi)
        print("Tanggal Keberangkatan  :", tgl_brkt)
        print("Kota keberangkatan     :", kota_berangkat)
        print("Kota tujuan            :", kota_tujuan)
        print("Data penumpang         :")
        for i in range(len(pnp_dewasa)):
            print("No Identitas :", no_id_pnp_dws[i])
            print("Nama         :", pnp_dewasa[no_id_pnp_dws[i]], "\n")
        for i in range(len(pnp_anak)):
            print("No Identitas :", no_id_pnp_ank[i])
            print("Nama         :", pnp_anak[no_id_pnp_ank[i]], "\n")

        if pilihan == 1:
            print("Jalur Transit:", jalur)
            print("Total Bayar  :", harga*jml_pnp, "euro")
            catat_pembelian_tiket(id_resi, tgl_brkt, kota_berangkat, kota_tujuan, harga*jml_pnp)
        else:
            print("Jalur Transit:", jalur_termurah)
            print("Total Bayar  :", price[kota_tujuan]*jml_pnp, "euro\n")
            catat_pembelian_tiket(id_resi, tgl_brkt, kota_berangkat, kota_tujuan, price[kota_tujuan]*jml_pnp)

        id_resi += 1

        print("Kembali ke menu awal\n")

    return konfirmasi


def admin():
    global pilihan_admin
    print("=====MENU ADMIN=====")
    print("1. Menampilkan rekap semua pembelian tiket")
    print("2. Logout ke menu awal pilihan login")
    pilihan_admin = input("Pilih menu:")
    while pilihan_admin != '1' and pilihan_admin != '2':
        print("Inputan anda salah, Silahkan ulangi!")
        pilihan_admin = input("Pilih menu:")

    if pilihan_admin == '1':
        print("\nMENAMPILKAN SEMUA REKAP PEMBELIAN TIKET:")
        for i in range(len(l_id_resi)):
            i += 1
            print("Id Resi:", i)
            print("Tanggal Keberangkatan:", rekap_pembelian[i]['Tanggal Berangkat'])
            print("Kota Keberangkatan:", rekap_pembelian[i]['Kota Berangkat'])
            print("Kota Tujuan:", rekap_pembelian[i]['Kota Tujuan'])
            print("Total Bayar:", rekap_pembelian[i]['Total Bayar'], "euro", "\n")

        print("===SELESAI===")
        print("KEMBALI KE MENU AWAL PILIHAN LOGIN:\n")
        pilihan_admin = '2'

    return pilihan_admin


def total_harga(jalur):
    harga = 0
    for v in range(len(jalur)):
        if v < len(jalur)-1:
            if graph[jalur[v]][jalur[v+1]] <= 150:
                harga += 30
            elif 150 < graph[jalur[v]][jalur[v+1]] <= 250:
                harga += 45
            else:
                harga += 55
            if v == len(jalur)-1:
                break
    return harga
