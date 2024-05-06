import networkx as nx
import matplotlib.pyplot as plt

# Matrice d'adjacence
matrice = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

# Création du graphe à partir de la matrice d'adjacence
G = nx.from_numpy_array(matrice)

# Visualisation du graphe
nx.draw(G, with_labels=True)
plt.show()

# Définition du chemin entre deux nœuds spécifiques (par exemple, de 0 à 4)
chemin = nx.shortest_path(G, source=0, target=4)

# Visualisation du chemin
nx.draw_networkx_nodes(G, nodelist=chemin, node_color='r', node_size=500)
nx.draw_networkx_edges(G, edgelist=[(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)], edge_color='r',
                       width=2)
plt.show()
