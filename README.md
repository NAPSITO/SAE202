# SAE 2.02 : Exploration algorithmique d'un problème

### Introduction

Ce programme montre comment créer et visualiser des graphes en utilisant la bibliothèque Python `networkx`, ainsi
que `matplotlib` pour la visualisation.
Il montre également comment trouver et visualiser le chemin le plus court entre deux nœuds dans un graphe.

### Prérequis

- Bibliothèques Python : `networkx`, `matplotlib`

### Installation

Installez les bibliothèques nécessaires en utilisant pip :

```bash
pip install networkx matplotlib
```

### Utilisation

1. Exécutez le script Python `main.py` :

```bash
python main.py
```

## 2) Dessin d'un graphe et d'un chemin à partir de sa matrice

### Utilisation

Ce script effectue les étapes suivantes :

- Crée un graphe à partir d'une matrice.
- Affiche le graphe initial.
- Trouve le chemin le plus court entre deux nœuds spécifiques.
- Affiche le chemin trouvé dans le graphe.

---

## 3) Génération aléatoire de matrices de graphes pondérés

### Utilisation

Ce programme permet de générer un graphe avec 50% de flèches et avec une proportion variable de flèches :
`graphe(n, a, b)` et `graphe2(n, p, a, b)`.

## 4) Implémentation des algorithmes de Dijkstra et Bellman-Ford

### Algorithme de Dijkstra

1 Définir la taille du graphe et le nœud de départ

```python
taille = 6
depart = 0
```

2 Générer un graphe pondéré aléatoire

```python
M = graphe2(taille, 1, 0, 3)
print(M)
```

3 Appliquer l'algorithme de Dijkstra pour trouver la distance et le chemin le plus court vers le dernier nœud

```python
dist, chemin_plus_court = Dijkstra(M, depart, taille - 1)
print(f"Distance totale : {dist}")
print(f"Chemin le plus court : {chemin_plus_court}")
```

4 Afficher le graphe et le chemin trouvé

```python
orientation = afficherGraphe(M)
afficherChemin(M, depart, taille - 1, orientation)
```

### Algorithme de Bellman-Ford

1 Définir la taille du graphe et le nœud de départ (similaire à Dijkstra)

```python
taille = 6
depart = 0
```

2 Générer un graphe pondéré aléatoire (similaire à Dijkstra)

```python
M = graphe2(taille, 1, 0, 3)
print(M)
```

3 Appliquer l'algorithme de Bellman-Ford pour trouver la distance et le chemin le plus court vers le dernier nœud

```python
result = BellmanFord(M, depart, taille - 1)
```

4 Vérifier et afficher le résultat

```python
if isinstance(result, tuple):
    distance, path = result
    print("Distance totale :", distance)
    print("Chemin le plus court :", path)

    orientation = afficherGraphe(M)
    afficherChemin(M, depart, taille - 1, orientation)
else:
    print(result)
```

## 5) Influence du choix de la liste ordonnées des flèches pour l'algorithme de Bellman-Ford

### Utilisation

Ce programme permet d'explorer l'influence de différents ordres de traitement des arêtes sur l'algorithme de
Bellman-Ford. Trois méthodes sont comparées : arbitraire, par largeur et par longueur.

### Étapes

1. **Générer une matrice de graphes pondérés aléatoires** :
   Utiliser la fonction `genereMatrice` pour créer une matrice de taille définie avec des poids aléatoires pour les
   arêtes.

2. **Définir les paramètres de l'algorithme** :
   Spécifier les nœuds de départ et de fin pour l'exécution de l'algorithme.

3. **Exécuter l'algorithme Bellman-Ford avec différents ordres** :
   Utiliser la fonction `BellmanFordOrder` pour appliquer l'algorithme avec trois ordres de traitement des arêtes :
    - `arbitraire` : Les arêtes sont traitées dans un ordre aléatoire.
    - `largeur` : Les arêtes sont traitées en fonction de leur distance à partir du nœud de départ.
    - `longueur` : Les arêtes sont triées par leur poids.

4. **Comparer les résultats** :
   Comparer le nombre d'itérations nécessaires pour chaque ordre ainsi que les résultats obtenus pour le plus court
   chemin.

### Exemple de sortie

```python
Liste
ordonnée: arbitraire, Résultat: (distance, chemin), Compteur: nombre_iterations
Liste
ordonnée: largeur, Résultat: (distance, chemin), Compteur: nombre_iterations
Liste
ordonnée: longueur, Résultat: (distance, chemin), Compteur: nombre_iterations
```

## 6.1 Deux fonctions "temps de calcul"

### Utilisation

Ce programme compare le temps de calcul des algorithmes de Dijkstra et de Bellman-Ford sur un graphe généré
aléatoirement.

### Étapes

1. **Définir les paramètres du graphe** :
   Spécifiez les paramètres pour la génération du graphe aléatoire, y compris le nombre de nœuds `n`, la probabilité
   d'arête `p`, ainsi que les poids minimum `a` et maximum `b`.

2. **Calculer le temps de l'algorithme de Dijkstra** :
   Utilisez la fonction `TempsDij` pour mesurer le temps nécessaire à l'algorithme de Dijkstra pour trouver les plus
   courts chemins depuis le premier sommet (0).

3. **Calculer le temps de l'algorithme de Bellman-Ford** :
   Utilisez la fonction `TempsBF` pour mesurer le temps nécessaire à l'algorithme de Bellman-Ford pour effectuer la même
   tâche.

4. **Comparer les résultats** :
   Comparez les temps de calcul pour évaluer les performances relatives des deux algorithmes.

### Exemple de sortie

```python
n = 10
p = 0.5
a = 1
b = 10

temps_dijkstra = round(TempsDij(n, p, a, b), 6)
print(f"Temps de calcul pour n={n}, p={p}, a={a}, b={b} : TempsDij = {temps_dijkstra} secondes")

temps_bellman_ford = round(TempsBF(n, p, a, b), 6)
print(f"Temps de calcul pour n={n}, p={p}, a={a}, b={b} : TempsBF = {temps_bellman_ford} secondes")
```

## 6.2 Comparaison et identification des deux fonctions temps

### Utilisation

Ce programme compare graphiquement les temps de calcul des algorithmes de Dijkstra et de Bellman-Ford pour différents
nombres de sommets dans un graphe généré aléatoirement.

### Étapes

1. **Définir les paramètres communs** :
   Spécifiez les paramètres fixes pour la génération du graphe, tels que la probabilité d'arête `p`, ainsi que les poids
   minimum `a` et maximum `b`.

2. **Calculer les temps de calcul pour une gamme de valeurs de n** :
   Pour chaque valeur de `n` dans l'intervalle spécifié, mesurez le temps de calcul des algorithmes de
   Dijkstra (`TempsDij`) et de Bellman-Ford (`TempsBF`).

3. **Tracer les résultats** :
   Utilisez `matplotlib` pour tracer les temps de calcul en fonction du nombre de sommets pour chaque algorithme.

### Exemple de code

```python
import matplotlib.pyplot as plt

valeurs = range(2, 201)
p = 0.5
a = 1
b = 10

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
```

## 7 Test de forte connexité

### Utilisation

Ce programme teste la forte connexité d'un graphe en utilisant la fermeture transitive.

### Étapes

1. **Vérifier la forte connexité** :
   Utilisez la fonction `fc` pour déterminer si un graphe représenté par une matrice d'adjacence est fortement connexe.

2. **Générer et tester un exemple de graphe** :
   Créez une matrice d'adjacence pour un graphe et appliquez la fonction `fc` pour tester sa forte connexité.

### Exemple de sortie

```python
print("Fortement connexe : ", fc(exemple))
print("\n")
```

## 8 Forte connexité pour un graphe avec p = 50% de flèches

### Utilisation

Ce programme teste la proportion de graphes fortement connexes en générant des graphes avec une probabilité de 50%
d'avoir une flèche entre chaque paire de nœuds. Il s'arrête lorsque cette proportion atteint ou dépasse 99% pour un
certain nombre de nœuds.

### Étapes

1. **Tester la forte connexité pour différents nombres de nœuds** :
   Utilisez la fonction `test_stat_fc` pour vérifier la proportion de graphes fortement connexes pour différentes
   valeurs de `n` (nombre de nœuds).

2. **Afficher les résultats** :
   Pour chaque valeur de `n`, affichez le pourcentage de graphes fortement connexes. Si ce pourcentage atteint ou
   dépasse 99%, affichez une affirmation et arrêtez le test.

### Exemple de sortie

```python
for n in range(10, 100, 10):
    pourcentage = test_stat_fc(n, 400)
    print(f"Pour n={n}, {pourcentage}% des graphes sont fortement connexes.")
    if pourcentage >= 99:
        print(f"L'affirmation est vraie pour n={n}.")
        break

print("\n")
```

## 9 Détermination du seuil de forte connexité

### Utilisation

Ce programme détermine le seuil de forte connexité pour un graphe de `n` nœuds. Le seuil est la probabilité minimale `p`
à partir de laquelle au moins 99% des graphes générés sont fortement connexes.

### Étapes

1. **Définir le nombre de nœuds** :
   Spécifiez le nombre de nœuds `n` pour le graphe.

2. **Calculer le seuil de forte connexité** :
   Utilisez la fonction `seuil` pour déterminer la probabilité minimale `p` à laquelle les graphes de `n` nœuds sont
   fortement connexes avec une probabilité d'au moins 99%.

3. **Afficher le résultat** :
   Affichez le seuil de forte connexité calculé.

### Exemple de sortie

```python
n = 10

p_seuil = seuil(n, 400)
print(f"Le seuil de forte connexité pour n={n} est p={p_seuil:.4f}")
```

## 10.1 Représentation graphique de seuil(n)

### Utilisation

Ce programme trace le seuil de forte connexité en fonction de la taille du graphe `n`.

### Étapes

1. **Calculer les seuils pour différentes tailles de graphe** :
   Utilisez la fonction `seuil` pour déterminer le seuil de forte connexité pour chaque valeur de `n` dans l'intervalle
   spécifié.

2. **Tracer les résultats** :
   Utilisez `matplotlib` pour représenter graphiquement la relation entre la taille du graphe et le seuil de forte
   connexité.

### Exemple de code

```python
import matplotlib.pyplot as plt

valeurs = range(10, 41)
seuils = [seuil(n, 20) for n in valeurs]

plt.figure(figsize=(10, 6))
plt.plot(valeurs, seuils, label='Suite seuil(n)', color='pink')
plt.xlabel('Taille du graphe (n)')
plt.ylabel('Seuil')
plt.title('Seuil de forte connexité en fonction de n')
plt.legend()
plt.show()
```

### Conclusion

Le graphique montre comment le seuil de forte connexité varie en fonction de la taille du graphe `n`.

---

## 10.2 Identification de la fonction seuil(n)

### Utilisation

Ce programme identifie la relation fonctionnelle entre `n` et le seuil de forte connexité `p_seuil` en utilisant une
régression linéaire sur les valeurs logarithmiques.

### Étapes

1. **Calculer les valeurs logarithmiques** :
   Calculez les logarithmes naturels des tailles de graphe et des seuils de forte connexité.

2. **Effectuer une régression linéaire** :
   Utilisez la fonction `linregress` pour effectuer une régression linéaire sur les valeurs logarithmiques et obtenir la
   pente et l'intercepte.

3. **Tracer les résultats** :
   Utilisez `matplotlib` pour représenter les données et la ligne de régression.

4. **Afficher la fonction puissance estimée** :
   Convertissez les paramètres de la régression linéaire pour obtenir la forme de la fonction puissance estimée.

### Exemple de code

```python
import numpy as np
from scipy.stats import linregress

log_valeurs = np.log(valeurs)
log_seuils = np.log(seuils)
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
```

## Conclusion
Ce projet démontre de manière exhaustive comment utiliser des algorithmes de graphes pour résoudre des problèmes
complexes tels que la recherche de chemins optimaux et l'analyse de la connexité. Les résultats montrent non seulement
les différences de performance entre les algorithmes de Dijkstra et de Bellman-Ford, mais aussi comment la structure et
la densité des graphes influencent leur forte connexité. L'approche analytique et graphique adoptée offre une
compréhension approfondie des propriétés des graphes et des algorithmes utilisés pour leur analyse.