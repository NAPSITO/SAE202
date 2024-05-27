import networkx as nx
import numpy as np
import time


def TempsDij(n):
    # Générer aléatoirement une matrice d'adjacence pour un graphe pondéré à poids positifs
    np.random.seed(0)  # Pour rendre l'exemple reproductible
    matrix = np.random.randint(1, 10, size=(n, n))
    np.fill_diagonal(matrix, 0)  # Pas de boucle (poids 0 sur la diagonale)

    # Créer un graphe à partir de la matrice d'adjacence
    G = nx.from_numpy_array(matrix, create_using=nx.DiGraph())

    # Calculer les plus courts chemins depuis le premier sommet (sommet 0)
    start_time = time.time()
    lengths = nx.single_source_dijkstra_path_length(G, 0)
    end_time = time.time()

    # Calculer le temps de calcul utilisé
    elapsed_time = end_time - start_time

    return elapsed_time


# Exemple d'utilisation
n = 10
temps = TempsDij(n)
print(f"Temps de calcul pour n={n} : {temps} secondes")
