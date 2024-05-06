<<<<<<< HEAD
import networkx as nx
import matplotlib.pyplot as plt

# Matrice d'adjacence
=======
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Matrice
>>>>>>> 248bd6b283c014ab62646ab29591e08b1fcc25c8
matrice = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

<<<<<<< HEAD
# Création du graphe à partir de la matrice d'adjacence
G = nx.from_numpy_array(matrice)
=======
# Conversion de la matrice en numpy.array
matrice_np = np.array(matrice)

# Création du graphe à partir de la matrice
G = nx.from_numpy_array(matrice_np)
>>>>>>> 248bd6b283c014ab62646ab29591e08b1fcc25c8

# Visualisation du graphe
nx.draw(G, with_labels=True)
plt.show()

<<<<<<< HEAD
# Définition du chemin entre deux nœuds spécifiques (par exemple, de 0 à 4)
chemin = nx.shortest_path(G, source=0, target=4)

# Visualisation du chemin
nx.draw_networkx_nodes(G, nodelist=chemin, node_color='r', node_size=500)
nx.draw_networkx_edges(G, edgelist=[(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)], edge_color='r',
                       width=2)
=======
# Définition du chemin entre deux nœuds spécifiques
chemin = nx.shortest_path(G, source=0, target=4)

pos = nx.spring_layout(G)

# Visualisation du chemin
nx.draw_networkx_nodes(G, pos, nodelist=chemin, node_color='r', node_size=500)
nx.draw_networkx_edges(G, pos)

>>>>>>> 248bd6b283c014ab62646ab29591e08b1fcc25c8
plt.show()
