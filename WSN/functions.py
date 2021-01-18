import numpy as np

def min_edge(select, candidate, graph):
    min_weight = np.inf
    v, u = 0, 0
    for i in select:
        for j in candidate:
            if min_weight > graph[i][j]:
                min_weight = graph[i][j]
                v, u = i, j
    return v, u


def prim(graph):
    vertex_num = len(graph)
    select = [0]
    candidate = list(range(1, vertex_num))
    edge = []
    for i in range(1, vertex_num):
        v, u = min_edge(select, candidate, graph)
        edge.append((v, u))
        select.append(u)
        candidate.remove(u)
    return edge


def startwith(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]
    
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis