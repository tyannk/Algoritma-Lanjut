# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

from function import *


while pilihan_admin == '2':
    pilihan = login()
    while pilihan == '1':
        konfirmasi = pembeli()
        while konfirmasi == 'TIDAK':
            temp_no_id_pnp_dws = []
            temp_no_id_pnp_ank = []
            temp_pnp_dewasa = {}
            temp_pnp_anak = {}
            print("\n=====KEMBALI KE HALAMAN AWAL SEBAGAI PEMBELI=====")
            konfirmasi = pembeli()
        pilihan = login()

    pilihan_admin = admin()
