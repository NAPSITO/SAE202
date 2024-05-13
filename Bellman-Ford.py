import numpy as np
from generationAleatoire import *

def BellmanFord(M, d):
    n = len(M)
    # Initialisation des distances
    distances = [float('inf')] * n
    distances[start] = 0

    # Itération sur chaque nœud pour mettre à jour les distances
    for _ in range(n - 1):
        for node in range(n):
            for neighbor in range(n):
                if M[node][neighbor] != 0:
                    if distances[node] + M[node][neighbor] < distances[neighbor]:
                        distances[neighbor] = distances[node] + M[node][neighbor]

    # Vérification de la présence de cycles négatifs
    for node in range(n):
        for neighbor in range(n):
            if M[node][neighbor] != 0:
                if distances[node] + M[node][neighbor] < distances[neighbor]:
                    return "Il existe un cycle négatif dans le graphe"

    return distances

    # Vérification de la connectivité du sommet de départ
    if all(distance == float('inf') for distance in distances):
        return "Sommet non joignable depuis {} par un chemin dans le graphe".format(start)

        # Affichage du graphe avec les distances mises à jour
        G = nx.DiGraph()
        for i in range(num_vertices):
            for j in range(num_vertices):
                if M[i][j] != 0:
                    G.add_edge(i, j, weight=M[i][j])

        pos = nx.spring_layout(G)  # Position des nœuds
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10,
                font_weight="bold")  # Dessine le graphe
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Ajoute les labels pour les poids des arêtes

        plt.title("Graphe avec distances mises à jour")
        plt.show()

        return distances

# Exemple d'utilisation
matrice = [
    [0, 4, 0, 0, 0],
    [-1, 0, 3, 2, 2],
    [0, 0, 0, 2, 0],
    [0, 1, 5, 0, 0],
    [0, 0, -3, 0, 0]
]

start = 0
result = BellmanFord(matrice, start)

if isinstance(result, str):
    print(result)
else:
    print("Plus courts chemins depuis le sommet", start)
    for node, distance in enumerate(result):
        print("Distance de", start, "à", node, ":", distance)

matrice2=graphe2(5,0.5,5,6)

result1 = BellmanFord(matrice2, start)

if isinstance(result1, str):
    print(result1)
else:
    print("Plus courts chemins depuis le sommet", start)
    for node, distance in enumerate(result1):
        print("Distance de", start, "à", node, ":", distance)

# print(paths)
# orientation = afficherGraphe(M)
# afficherChemin(M, d, 4, orientation)
