import numpy as np


def Dijkstra(M, origine):
    # Initialisation des dictionnaires
    n = M.shape[0]
    dist = {}
    pred = {}
    distR = {}

    for sommet in range(n):
        if M[origine, sommet] == 0:
            dist[sommet] = float('inf')
        else:
            dist[sommet] = M[origine, sommet]
        pred[sommet] = None
        distR[sommet] = True

    dist[origine] = 0

    while distR:
        sommet_pp = min(distR, key=dist.get)
        del distR[sommet_pp]

        for sommet in range(n):
            if M[sommet_pp, sommet] != 0 and distR.get(sommet):
                nouvelle_distance = dist[sommet_pp] + M[sommet_pp, sommet]
                if nouvelle_distance <= dist[sommet]:
                    dist[sommet] = nouvelle_distance
                    pred[sommet] = sommet_pp

    return dist, pred
