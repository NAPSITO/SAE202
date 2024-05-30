import random

from BellmanFord import BellmanFord
from BellmanFordOrdre import BellmanFordOrder
from Dijkstra import Dijkstra
from TempsBF import TempsBF
from TempsDij import TempsDij
from dessinGrapheChemin import *
from forteConnexité import fc, test_stat_fc
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

print("\n")

# 6.1 Deux fonctions "temps de calcul"
n = 10
p = 0.5
a = 1
b = 10
temps = round(TempsDij(n, p, a, b), 6)
print(f"Temps de calcul pour n={n}, p={p}, a={a}, b={b} : TempsDij = {temps} secondes")

n = 10
p = 0.5
a = 1
b = 10
temps = round(TempsBF(n, p, a, b), 6)
print(f"Temps de calcul pour n={n}, p={p}, a={a}, b={b} : TempsBF = {temps} secondes")

# 6.2 Comparaison et identification des deux fonctions temps
n_values = range(2, 201)
dijkstra_times = [TempsDij(n, p, a, b) for n in n_values]
bellman_ford_times = [TempsBF(n, p, a, b) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, dijkstra_times, label='Dijkstra', color='blue')
plt.plot(n_values, bellman_ford_times, label='Bellman-Ford', color='red')
plt.xlabel('Nombre de sommets (n)')
plt.ylabel('Temps de calcul (s)')
plt.title('Comparaison des temps de calcul : Dijkstra vs Bellman-Ford')
plt.legend()
plt.grid(True)
plt.show()

print("\n")

# 7 Test de forte connexité
print("Fortement connexe : ", fc(exemple))

# 8 Forte connexité pour un graphe avec p=50% de flèches
p = 0.5
a = 0
b = 1
nombreTest = 400

for n in range(10, 100, 10):
    pourcentage = test_stat_fc(n, p, a, b, nombreTest)
    print(f"Pour n={n}, {pourcentage}% des graphes sont fortement connexes.")
    if pourcentage >= 99:
        print(f"L'affirmation est vraie pour n={n}.")
        break
