import time

import networkx as nx

from generationAleatoire import graphe2


def TempsBF(n, p, a, b):
    # Utiliser graphe2 pour générer la matrice d'adjacence
    matrix = graphe2(n, p, a, b)

    # Créer un graphe à partir de la matrice d'adjacence
    G = nx.from_numpy_array(matrix, create_using=nx.DiGraph())

    # Calculer les plus courts chemins depuis le premier sommet (sommet 0) avec Bellman-Ford
    start_time = time.time()
    lengths = nx.single_source_bellman_ford_path_length(G, 0)
    end_time = time.time()

    # Calculer le temps de calcul utilisé
    elapsed_time = end_time - start_time

    return elapsed_time
