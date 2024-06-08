import random
from scipy.stats import linregress

from BellmanFord import BellmanFord
from BellmanFordOrdre import BellmanFordOrder
from Dijkstra import Dijkstra
from TempsBF import TempsBF
from TempsDij import TempsDij
from choixListeFlèche import ordreLargeur, ordreProfondeur
from dessinGrapheChemin import *
from forteConnexité import fc, test_stat_fc, seuil
from generationAleatoire import *

# Matrice
exemple = np.array([
    [0, 2, float("inf"), float("inf"), 1],
    [3, float("inf"), 4, 0, float("inf")],
    [float("inf"), 4, 0, 5, float("inf")],
    [3, 0, float("inf"), 0, 2],
    [6, 0, float("inf"), 5, 0]
])

# 2.1 Dessin d'un graphe
print("2.1 Dessin d'un graphe\n")
orientation = afficherGraphe(exemple, "2.1 Dessin d'un graphe")

# 2.2 Dessin d'un chemin
print("2.2 Dessin d'un chemin\n")
distances, predecesseurs = Dijkstra(exemple, 0)

chemin_critique = []
courant = 2
while courant is not None:
    chemin_critique.append(courant)
    courant = predecesseurs[courant]
chemin_critique.reverse()

afficherGraphe(exemple, "2.2 Dessin d'un chemin", chemin_critique)

# 3.1 Graphes avec 50% de flèches
print("3.1 Graphe avec 50% d'infini\n")
print(graphe(5, 1, 10))

print("\n")

# 3.2 Graphes avec une proportion variables p de flèches
print("3.2 Graphe avec une proportion variable p d'infini\n")
print(graphe2(5, 0.3, 1, 10))

print("\n")

# 4.1 Codage de l'algorithme de Dijkstra
print("4.1 Codage de l'algorithme de Dijsktra\n")
taille = 6
depart = 0
M = graphe2(taille, 1, 0, 3)
print(M)

afficherGraphe(M, "4.1 Codage de l'algorithme de Dijsktra", chemin_critique)

if chemin_critique:
    print(f"Plus court chemin pour atteindre {2} depuis {0} :")
    print(f"Chemi : {chemin_critique}")
    print(f"Distance  {distances[2]}")
else:
    print(f"Aucun chemin trouvé de {0} à {2}")

print("\n")

# 4.2 Codage de l'algorithme de Bellman-Ford
print("4.2 Codage de l'algorithme de Bellman-Ford")
taille = 6
depart = 0
M = graphe2(taille, 1, 0, 3)
print(M)

resultat = BellmanFord(M, depart, taille - 1)

if isinstance(resultat, tuple):
    distance, path = resultat
    print("Distance totale :", distance)
    print("Chemin le plus court :", path)

    orientation = afficherGraphe(M, "4.2 Codage de l'algorithme de Bellman-Ford")
else:
    print(resultat)

print("\n")

# 5 Influence du choix de la liste ordonnée des flèches pour l'algorithme de Bellman-Ford
print("5 Influence du choix de la liste ordonnée des flèches pour l'algorithme de Bellman-Ford\n")


def genereMatrice(points, arrete=0.2):
    M = [[0 if i == j or random.random() > arrete else random.randint(-10, 10) for j in range(points)] for i in
         range(points)]
    return M


points = 50
M = genereMatrice(points)
debut, fin = 0, points - 1

for type in ["arbitraire", "largeur", "longueur"]:
    resultat, nombre = BellmanFordOrder(M, debut, fin, type)
    print(f"Liste ordonnée : {type}, Résultat : {resultat}, Compteur : {nombre}")

print("\n")

# 6.1 Deux fonctions "temps de calcul"
print("6.1 Deux fonctions \"temps de calcul")
n = 10
p = 0.5
a = 1
b = 10
M = graphe2(n, p, a, b)
temps = round(TempsDij(n, p, a, b), 6)
print(f"Temps de calcul pour n={n}, p={p}, a={a}, b={b} : TempsDij = {temps} secondes")

temps = round(TempsBF(n, p, a, b), 6)
print(f"Temps de calcul pour n={n}, p={p}, a={a}, b={b} : TempsBF = {temps} secondes")

# 6.2 Comparaison et identification des deux fonctions temps
print("Comparaison du temps de calcul de Dijksta et Bellman-ford pour des sommets allant de 2 a 200")
valeurs = range(2, 201)
tempsDij = [TempsDij(n, p, a, b) for n in valeurs]
tempsBell = [TempsBF(n, p, a, b) for n in valeurs]

plt.figure(figsize=(10, 6))
plt.plot(valeurs, tempsDij, label='Dijkstra', color='blue')
plt.plot(valeurs, tempsBell, label='Bellman-Ford', color='red')
plt.xlabel('Nombre de sommets (n)')
plt.ylabel('Temps de calcul (s)')
plt.title('Comparaison des temps de calcul : Dijkstra vs Bellman-Ford')
plt.legend()
plt.grid(True)
plt.show()

print("\n")

# 7 Test de forte connexité
print("Fortement connexe : ", fc(exemple))

print("\n")

# 8 Forte connexité pour un graphe avec p=50% de flèches
for n in range(20, 50, 1):
    pourcentage = test_stat_fc(n, 400)
    print(f"Pour n={n}, {pourcentage}% des graphes sont fortement connexes.")
    if pourcentage >= 99:
        print(f"L'affirmation est vraie pour n={n}.")
        break

print("\n")

# 9 Détermination du seuil de forte connexité
print("9 Détermination du seuil de forte connexité")
n = 10

p_seuil = seuil(n)
print(f"Le seuil de forte connexité pour n={n} est p={p_seuil}")

# 10.1 Représentation graphique de seuil(n)
values = range(10, 41)
seuil_values = [seuil(n) for n in values]

# Tracer les valeurs
plt.plot(valeurs, seuil_values, marker='o')
plt.xlabel('Taille de la matrice (n)')
plt.ylabel('Seuil de forte connexité')
plt.title('Représentation de seuil')
plt.grid(True)
plt.show()

# 10.2 Identification de la fonction seuil(n)
log_valeurs = np.log(valeurs)
log_seuils = np.log(seuil_values)
pente, intercepte, valeur_r, valeur_p, err = linregress(log_valeurs, log_seuils)

plt.figure(figsize=(10, 6))
plt.plot(log_valeurs, log_seuils, marker='o', linestyle='-', color='b', label='Données')
plt.plot(log_valeurs, pente * log_valeurs + intercepte, color='r', label=f'Régression linéaire (pente={pente:.2f})')
plt.xlabel('log(n)')
plt.ylabel('log(p_seuil)')
plt.title('Log-log du seuil de forte connexité en fonction de n')
plt.legend()
plt.show()

a = np.exp(intercepte)
c = -pente
print(f"La fonction puissance estimée est p_seuil(n) ≈ {a:.4f} * n^({-c:.4f})")
