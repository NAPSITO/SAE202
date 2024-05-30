def BellmanFord(M, debut, fin):
    nombreSommets = len(M)
    # Initialisation des distances
    distances = [float('inf')] * nombreSommets
    distances[debut] = 0

    # Initialisation des itinéraires
    predecesseur = [-1] * nombreSommets

    # Itération sur chaque nœud pour mettre à jour les distances
    for i in range(nombreSommets - 1):
        for noeud in range(nombreSommets):
            for voisin in range(nombreSommets):
                if M[noeud][voisin] != 0:
                    if distances[noeud] + M[noeud][voisin] < distances[voisin]:
                        distances[voisin] = distances[noeud] + M[noeud][voisin]
                        predecesseur[voisin] = noeud

    # Vérification de la présence de cycles négatifs
    for noeud in range(nombreSommets):
        for voisin in range(nombreSommets):
            if M[noeud][voisin] != 0:
                if distances[noeud] + M[noeud][voisin] < distances[voisin]:
                    return ("Sommet joignable depuis {} par un chemin dans le graphe, mais pas de plus court chemin ("
                            "présence d'un cycle négatif)").format(debut)

    # Vérification de la connectivité du sommet de départ
    if all(distance == float('inf') for distance in distances):
        return "Sommet non-joignable depuis {} par un chemin dans le graphe".format(debut)

    # Vérification de la connectivité du sommet d'arrivée
    if distances[fin] == float('inf'):
        return "Sommet d'arrivée non-joignable depuis {} par un chemin dans le graphe".format(debut)

    # Reconstruction de l'itinéraire
    chemin = []
    actuel = fin
    while actuel != -1:
        chemin.insert(0, actuel)
        actuel = predecesseur[actuel]

    return distances[fin], chemin
