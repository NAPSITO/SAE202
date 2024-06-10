import time
import networkx as nx

from generationAleatoire import graphe2


def TempsBF(n, p, a, b):
    # Utiliser graphe2 pour générer la matrice d'adjacence
    matrice = graphe2(n, p, a, b)

    # Créer un graphe à partir de la matrice d'adjacence
    G = nx.from_numpy_array(matrice, create_using=nx.DiGraph())

    # Calculer les plus courts chemins depuis le premier sommet (sommet 0) avec Bellman-Ford
    tempsDebut = time.time()
    lengths = nx.single_source_bellman_ford_path_length(G, 0)
    tempsFin = time.time()

    # Calculer le temps de calcul utilisé
    temps = tempsFin - tempsDebut

    return max(temps, 1e-10)
