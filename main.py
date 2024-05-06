import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import dessinGrapheChemin

# Matrice
exemple = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

dessinGrapheChemin.afficherGraphe(exemple)

dessinGrapheChemin.afficherChemin(exemple, 0, 3)