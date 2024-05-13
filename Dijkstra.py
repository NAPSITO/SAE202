import numpy as np

from dessinGrapheChemin import afficherGraphe, afficherChemin
from generationAleatoire import graphe


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


# Exemple d'utilisation
Infini = np.inf

M = [
    [Infini, Infini, Infini, Infini, 103, Infini, 71],
    [Infini, Infini, Infini, 122, Infini, 98, Infini],
    [Infini, Infini, Infini, 118, 125, Infini, Infini],
    [Infini, 122, 118, Infini, Infini, Infini, Infini],
    [103, Infini, 125, Infini, Infini, 46, Infini],
    [Infini, Infini, Infini, Infini, 46, Infini, 118],
    [71, 98, Infini, Infini, Infini, 118, Infini]
]

# Exécution de l'algorithme de Dijkstra
paths = Dijkstra(M, 0, 5)

# Affichage des résultats
for path in paths:
    print(path)

orientation = afficherGraphe(M)
# afficherChemin(M, d, 4, orientation)
