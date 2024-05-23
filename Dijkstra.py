import numpy as np


def Dijkstra(M, origine, cible):
    # Initialisation des dictionnaires
    taille_graphe = len(M)
    dist = [np.inf] * taille_graphe
    pred = [None] * taille_graphe

    dist[origine] = 0
    noeud_visite = [origine]
    noeud_actuel = origine

    while cible not in noeud_visite:
        distance_min = np.inf
        for i in range(taille_graphe):
            if i not in noeud_visite and dist[i] < distance_min:
                distance_min = dist[i]
                noeud_actuel = i

        noeud_visite.append(noeud_actuel)

        for j in range(taille_graphe):
            if j not in noeud_visite and M[noeud_actuel][j] != np.inf:
                if dist[noeud_actuel] + M[noeud_actuel][j] < dist[j]:
                    dist[j] = dist[noeud_actuel] + M[noeud_actuel][j]
                    pred[j] = noeud_actuel

    nouvelle_cible = cible
    chemin_plus_court = [nouvelle_cible]
    while pred[nouvelle_cible] is not None:
        chemin_plus_court.append(pred[nouvelle_cible])
        nouvelle_cible = pred[nouvelle_cible]

    chemin_plus_court.reverse()

    return dist[-1], chemin_plus_court
