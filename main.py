import random

from BellmanFord import BellmanFord
from BellmanFordOrder import BellmanFordOrder
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
orientation = afficherGraphe(exemple, "2.1 Dessin d'un graphe")

# 2.2 Dessin d'un chemin
afficherChemin(exemple, 0, 4, orientation, "2.2 Dessin d'un chemin")

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

orientation = afficherGraphe(M, "4.1 Codage de l'algorithme de Dijkstra")
afficherChemin(M, depart, taille - 1, orientation, "4.1 Codage de l'algorithme de Dijkstra")

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

    orientation = afficherGraphe(M, "4.2 Codage de l'algorithme de Bellman-Ford")
    afficherChemin(M, depart, taille - 1, orientation, "4.2 Codage de l'algorithme de Bellman-Ford")
else:
    print(result)

print("\n")


# 5 Influence du choix de la liste ordonnée des flèches pour l'algorithme de Bellman-Ford
def generate_random_matrix(vertices, edge_prob=0.2):
    M = [[0 if i == j or random.random() > edge_prob else random.randint(-10, 10) for j in range(vertices)] for i in
         range(vertices)]
    return M


vertices = 50
M = generate_random_matrix(vertices)
start, end = 0, vertices - 1

for order_type in ["arbitraire", "largeur", "longueur"]:
    result, count = BellmanFordOrder(M, start, end, order_type)
    print(f"Liste ordonnée : {order_type}, Résultat : {result}, Compteur : {count}")
