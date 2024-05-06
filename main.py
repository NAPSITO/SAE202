from generationAleatoire import *
from dessinGrapheChemin import *

# Matrice
exemple = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

# 2.1 Dessin d'un graphe
orientation = afficherGraphe(exemple)

# 2.2 Dessin d'un chemin
afficherChemin(exemple, 0, 4, orientation)

# 3.1 Grahes avec 50% de flèches
graphe(5, 1, 10)
