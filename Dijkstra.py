import numpy as np

from dessinGrapheChemin import afficherGraphe, afficherChemin
from generationAleatoire import graphe


def Dijkstra(M, d):
    # Initialisation
    n = len(M)  # Nombre de sommets
    dist = {i: float('inf') for i in range(n)}  # Distance initiale à l'infini
    dist[d] = 0  # Distance du sommet source à lui-même est 0
    pred = {i: None for i in range(n)}  # Prédécesseur initial à None
    dist[d] = 0  # Distance du sommet source à lui-même est 0
    pred[d] = d  # Prédécesseur du sommet source est lui-même
    A = set([d])  # Ensemble des sommets déjà traités

    while len(A) < n:  # Tant que tous les sommets n'ont pas été traités
        # Sélection du sommet avec la distance minimale hors de A
        s = min((s for s in range(n) if s not in A), key=lambda s: dist[s])
        A.add(s)  # Ajout de s dans A

        # Pour tous les successeurs t de s hors de A
        for t, poids in enumerate(M[s]):
            if poids > 0 and t not in A:  # Si le poids est positif et t n'a pas été traité
                # Modification des variables pour t
                if dist[s] + poids < dist[t]:
                    dist[t] = dist[s] + poids
                    pred[t] = s

    # Construction des chemins
    paths = {}
    for v in range(n):
        if v != d:
            if pred[v] is not None:
                # Construction du chemin
                path = [v]
                while pred[v] is not None:
                    path.append(pred[v])
                    v = pred[v]
                path.reverse()
                paths[v] = (dist[v], path)
            else:
                paths[v] = "sommet non joignable à d par un chemin dans le graphe G"

    return paths


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

d = 0  # Sommet source
paths = Dijkstra(M, d)

# Collecte des chemins dans une liste
for v, path in paths.items():
    if isinstance(path, tuple):
        print(f"Chemin de {d} à {v}: Longueur = {path[0]}, Chemin = {path[1]}")
    else:
        print(f"{v}: {path}")

# print(paths)
# orientation = afficherGraphe(M)
# afficherChemin(M, d, 4, orientation)
