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
