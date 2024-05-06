import numpy as np


def graphe(n, a, b):
    # Vérification de la taille de la matrice
    if n <= 0:
        print("La taille de la matrice doit être supérieure à 0.")
        exit()

    # Création d'une matrice de taille n x n avec des valeurs 0 et 1
    matrice = np.random.randint(2, size=(n, n))

    # Conversion de la matrice en float64
    matrice = matrice.astype('float64')

    # Remplacement des 1 par des valeurs aléatoires entre a et b
    indices_1 = np.where(matrice == 1)
    matrice[indices_1] = np.random.uniform(a, b, size=indices_1[0].shape)

    # Remplacement des 0 par float('inf')
    indices_0 = np.where(matrice == 0)
    matrice[indices_0] = float('inf')

    # Conversion des valeurs autres que float('inf') en entiers
    matrice[matrice != float('inf')] = matrice[matrice != float('inf')].astype(np.int64)

    print(matrice)


def graphe2(n, p, a, b):
    if n <= 0 or p < 0 or p > 1:
        print("La taille de la matrice doit être supérieure à 0, et p doit être entre 0 et 1.")
        exit()

    # Création d'une matrice de taille n x n avec des valeurs 0 et 1
    matrice = np.random.binomial(1, p, size=(n, n))

    # Conversion de la matrice en float64
    matrice = matrice.astype('float64')

    # Remplacement des 1 par des valeurs aléatoires entre a et b
    indices_1 = np.where(matrice == 1)
    matrice[indices_1] = np.random.uniform(a, b, size=indices_1[0].shape)

    # Remplacement des 0 par float('inf')
    indices_0 = np.where(matrice == 0)
    matrice[indices_0] = float('inf')

    # Conversion des valeurs autres que float('inf') en entiers
    matrice[matrice != float('inf')] = matrice[matrice != float('inf')].astype(np.int64)

    print(matrice)
