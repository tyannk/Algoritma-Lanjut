# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

Vertex = []
l_id_resi = []
no_id_pnp_dws = []
no_id_pnp_ank = []
temp_no_id_pnp_dws = []
temp_no_id_pnp_ank = []
graph = {}
graph_harga = {}
pnp_dewasa = {}
pnp_anak = {}
temp_pnp_dewasa = []
temp_pnp_anak = []
rekap_pembelian = {}


def add_vertex(v):
    if v in graph:
        print('vertex sudah ada di graph')
    else:
        graph[v] = {}
        graph_harga[v] = {}
        Vertex.append(v)


def add_edge(v1, v2, bobot):
    if v1 not in graph or v2 not in graph:
        print('vertex tidak ada di graph')
    else:
        graph[v1][v2] = bobot
        graph[v2][v1] = bobot

    if graph[v1][v2] <= 150:
        graph_harga[v1][v2] = 30
    elif 150 < graph[v1][v2] <= 250:
        graph_harga[v1][v2] = 45
    else:
        graph_harga[v1][v2] = 55


def add_pnp_dewasa(nama, no_id):
    if no_id in pnp_dewasa:
        print('Data penumpang sudah ada')
    else:
        pnp_dewasa[no_id] = {}
        pnp_dewasa[no_id] = nama
        no_id_pnp_dws.append(no_id)


def add_temp_pnp_dewasa(nama, no_id):
    if no_id in temp_pnp_dewasa:
        print('Data penumpang sudah ada')
    else:
        temp_pnp_dewasa.append(nama)
        temp_no_id_pnp_dws.append(no_id)


def add_pnp_anak(nama, no_id):
    if nama and no_id in pnp_anak:
        print('Data penumpang sudah ada')
    else:
        pnp_anak[no_id] = {}
        pnp_anak[no_id] = nama
        no_id_pnp_ank.append(no_id)


def add_temp_pnp_anak(nama, no_id):
    if nama and no_id in pnp_anak:
        print('Data penumpang sudah ada')
    else:
        temp_pnp_anak.append(nama)
        temp_no_id_pnp_ank.append(no_id)


def catat_pembelian_tiket(id_resi, tgl_brngkt, kota_berangkat, kota_tujuan, total_bayar):
    l_id_resi.append(id_resi)
    rekap_pembelian[id_resi] = {}
    rekap_pembelian[id_resi]["Tanggal Berangkat"] = tgl_brngkt
    rekap_pembelian[id_resi]["Kota Berangkat"] = kota_berangkat
    rekap_pembelian[id_resi]["Kota Tujuan"] = kota_tujuan
    rekap_pembelian[id_resi]["Total Bayar"] = total_bayar


add_vertex('Lille')
add_vertex('Compiegne')
add_vertex('Paris')
add_vertex('Rouen')
add_vertex('Caen')
add_vertex('Rennes')
add_vertex('Nantes')
add_vertex('Angers')
add_vertex('LeMans')
add_vertex('Tours')
add_vertex('Orleans')
add_vertex('Poitiers')
add_vertex('Limoges')
add_vertex('Clermont-Ferrand')
add_vertex('Lyon')
add_vertex('Dijon')
add_vertex('Besancon')
add_vertex('Strasbourg')
add_vertex('Nancy')
add_vertex('Reims')
add_vertex('Bordeaux')
add_vertex('Pau')
add_vertex('Toulouse')
add_vertex('Montpellier')
add_vertex('Marseille')
add_vertex('Nice')
add_vertex('Grenoble')


add_edge('Lille', 'Compiegne', 149)
add_edge('Compiegne', 'Paris', 87)
add_edge('Paris', 'Lille', 225)
add_edge('Paris', 'Rouen', 141)
add_edge('Rouen', 'Caen', 128)
add_edge('Caen', 'Rennes', 185)
add_edge('Rennes', 'Nantes', 113)
add_edge('Nantes', 'Angers', 90)
add_edge('Angers', 'LeMans', 95)
add_edge('LeMans', 'Tours', 101)
add_edge('Tours', 'Orleans', 118)
add_edge('Orleans', 'Paris', 133)
add_edge('Orleans', 'Poitiers', 218)
add_edge('Paris', 'Poitiers', 340)
add_edge('Nantes', 'Poitiers', 219)
add_edge('Poitiers', 'Limoges', 130)
add_edge('Limoges', 'Clermont-Ferrand', 194)
add_edge('Clermont-Ferrand', 'Lyon', 168)
add_edge('Lyon', 'Paris', 466)
add_edge('Lyon', 'Dijon', 195)
add_edge('Dijon', 'Besancon', 97)
add_edge('Besancon', 'Strasbourg', 244)
add_edge('Strasbourg', 'Nancy', 160)
add_edge('Nancy', 'Reims', 245)
add_edge('Reims', 'Paris', 143)
add_edge('Poitiers', 'Bordeaux', 229)
add_edge('Bordeaux', 'Pau', 217)
add_edge('Bordeaux', 'Toulouse', 245)
add_edge('Pau', 'Toulouse', 196)
add_edge('Toulouse', 'Montpellier', 243)
add_edge('Montpellier', 'Marseille', 169)
add_edge('Montpellier', 'Lyon', 304)
add_edge('Marseille', 'Nice', 199)
add_edge('Nice', 'Grenoble', 463)
add_edge('Grenoble', 'Lyon', 111)
