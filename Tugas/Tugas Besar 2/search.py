# NIM - Nama Lengkap
# 41520010201 - Tyan Nur Khollis
# 41520010057 - Ganendra Ekapradhana
# 41520010217 - Bulan Suci Rama Dhini

import math
from graph import *


def sequentialSearch(List, item):
    idx = 0
    found = True
    while idx < len(List) and not (found):
        if List[idx][0] == item:
            found = True
        else:
            idx += 1
    if not (found):
        return -1
    else:
        return idx


def dijkstra_terdekat(start, end):
    queue = {v: math.inf for v in graph}
    d = {v: math.inf for v in graph}
    predecessor = {v: None for v in graph}
    d[start] = 0
    queue[start] = 0
    while queue:
        u = min(queue, key=queue.get)
        queue.pop(u)
        for v in graph[u]:
            dtemp = d[u] + graph[u][v]
            if dtemp < d[v]:
                d[v] = dtemp
                predecessor[v] = u
    jalur = jalur_transit(start, end, predecessor)
    return d, jalur


def dijkstra_termurah(start, end):
    queue = {v: math.inf for v in graph_harga}
    d = {v: math.inf for v in graph_harga}
    predecessor = {v: None for v in graph_harga}
    d[start] = 0
    queue[start] = 0
    while queue:
        u = min(queue, key=queue.get)
        queue.pop(u)
        for v in graph_harga[u]:
            dtemp = d[u] + graph_harga[u][v]
            if dtemp < d[v]:
                d[v] = dtemp
                predecessor[v] = u
    jalur = jalur_transit(start, end, predecessor)
    return d, jalur


def jalur_transit(start, end, predecessor):
    jalur_transit = []
    vtemp = end
    while vtemp != start:
        jalur_transit.append(vtemp)
        vtemp = predecessor[vtemp]
    jalur_transit.append(start)
    jalur_transit.reverse()
    return jalur_transit