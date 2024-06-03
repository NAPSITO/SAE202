import numpy as np


def Dijkstra(M, origine, cible):
    # Initialisation des dictionnaires
    taille_graphe = len(M)
    dist = [np.inf] * taille_graphe
    pred = [None] * taille_graphe

    dist[origine] = 0
    visite = [origine]
    actuel = origine

    while cible not in visite:
        distance_min = np.inf
        for i in range(taille_graphe):
            if i not in visite and dist[i] < distance_min:
                distance_min = dist[i]
                actuel = i

        visite.append(actuel)

        for j in range(taille_graphe):
            if j not in visite and M[actuel][j] != np.inf:
                if dist[actuel] + M[actuel][j] < dist[j]:
                    dist[j] = dist[actuel] + M[actuel][j]
                    pred[j] = actuel

    nouvelle_cible = cible
    chemin = [nouvelle_cible]
    while pred[nouvelle_cible] is not None:
        chemin.append(pred[nouvelle_cible])
        nouvelle_cible = pred[nouvelle_cible]

    chemin.reverse()

    return dist[-1], chemin
