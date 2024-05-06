import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Matrice
matrice = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

# Conversion de la matrice en numpy.array
matrice_np = np.array(matrice)

# Création du graphe à partir de la matrice
G = nx.from_numpy_array(matrice_np)

# Visualisation du graphe
nx.draw(G, with_labels=True)
plt.show()

# Définition du chemin entre deux nœuds spécifiques
chemin = nx.shortest_path(G, source=0, target=4)

pos = nx.spring_layout(G)

# Visualisation du chemin
nx.draw_networkx_nodes(G, pos, nodelist=chemin, node_color='r', node_size=500)
nx.draw_networkx_edges(G, pos)

plt.show()
