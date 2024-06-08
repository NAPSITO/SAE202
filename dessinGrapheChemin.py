import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def afficherGraphe(matrice_np, titre, chemin=None):
    n = matrice_np.shape[0]
    G = nx.DiGraph()

    for i in range(n):
        for j in range(n):
            if matrice_np[i, j] != float('inf') and matrice_np[i, j] != 0:
                G.add_edge(i, j, weight=matrice_np[i, j])

    # Orientation du graphe
    pos = nx.spring_layout(G)

    # Création d'une figure
    fig, ax = plt.subplots()

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12)

    # Visualisation du graphe
    nx.draw(G, pos, with_labels=True)
    if chemin:
        afficherChemin(G, pos, chemin, titre)

    # Affichage du titre
    ax.set_title(titre)

    plt.show()

    return pos


def afficherChemin(matrice_np, orientation, chemin, titre):
    arretes = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]
    nx.draw_networkx_edges(matrice_np, orientation, edgelist=arretes, edge_color='red', width=2)

    # Affichage du titre
    plt.title(titre)

    plt.show(block=False)
