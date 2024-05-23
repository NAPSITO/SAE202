from BellmanFord import BellmanFord
from Dijkstra import Dijkstra
from dessinGrapheChemin import *
from generationAleatoire import *

# Matrice
exemple = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

# 2.1 Dessin d'un graphe
orientation = afficherGraphe(exemple)

# 2.2 Dessin d'un chemin
afficherChemin(exemple, 0, 4, orientation)

# 3.1 Graphes avec 50% de flèches
print(graphe(5, 1, 10))

print("\n")

# 3.2 Graphes avec une proportion variables p de flèches
print(graphe2(5, 0.5, 1, 10))

print("\n")

# 4.1 Codage de l'algorithme de Dijkstra
taille = 6
depart = 0
M = graphe2(taille, 1, 0, 3)
print(M)

dist, chemin_plus_court = Dijkstra(M, depart, taille - 1)

print(f"Distance totale : {dist}")
print(f"Chemin le plus court : {chemin_plus_court}")

orientation = afficherGraphe(M)
afficherChemin(M, depart, taille - 1, orientation)

print("\n")

# 4.2 Codage de l'algorithme de Bellman-Ford
taille = 6
depart = 0
M = graphe2(taille, 1, 0, 3)
print(M)

result = BellmanFord(M, depart, taille - 1)

if isinstance(result, tuple):
    distance, path = result
    print("Distance totale :", distance)
    print("Chemin le plus court :", path)

    orientation = afficherGraphe(M)
    afficherChemin(M, depart, taille - 1, orientation)
else:
    print(result)
