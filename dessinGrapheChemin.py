import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def afficherGraphe(matrice, titre):
    # Conversion de la matrice en numpy.array
    matrice_np = np.array(matrice)

    # Création du graphe à partir de la matrice
    G = nx.from_numpy_array(matrice_np)

    # Orientation du graphe
    pos = nx.spring_layout(G)

    # Création d'une figure
    fig, ax = plt.subplots()

    # Visualisation du graphe
    nx.draw(G, pos, with_labels=True)

    # Affichage du titre
    ax.set_title(titre)

    plt.show()

    return pos


def afficherChemin(matrice, depart, destination, orientation, titre):
    # Conversion de la matrice en numpy.array
    matrice_np = np.array(matrice)

    # Création du graphe à partir de la matrice
    G = nx.from_numpy_array(matrice_np)

    # Définition du chemin entre deux nœuds spécifiques
    chemin = nx.shortest_path(G, source=depart, target=destination)

    # Orientation du graphe
    pos = orientation

    # Visualisation du chemin
    nx.draw_networkx_nodes(G, pos, nodelist=chemin, node_color='r')
    nx.draw_networkx_edges(G, pos)

    # Ajout des labels
    labels = {node: node for node in chemin}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10)

    # Affichage du titre
    plt.title(titre)

    plt.show(block=False)
