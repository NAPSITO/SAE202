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

