from choixListeFlèche import ordreArbitraire, ordreProfondeur, ordreLargeur


def BellmanFordOrder(M, debut, fin, type="arbitraire"):
    nombreSommets = len(M)
    distances = [float('inf')] * nombreSommets
    distances[debut] = 0
    predecesseurs = [-1] * nombreSommets
    compteur = 0

    if type == "largeur":
        arretes = ordreLargeur(M, debut)
    elif type == "longueur":
        arretes = ordreProfondeur(M, debut)
    else:
        arretes = ordreArbitraire(M)

    for i in range(nombreSommets - 1):
        for u, v, w in arretes:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecesseurs[v] = u
        compteur += 1

    for u, v, w in arretes:
        if distances[u] + w < distances[v]:
            return (
                "Sommet joignable depuis {}, mais pas de plus court chemin").format(
                debut), compteur

    if all(distance == float('inf') for distance in distances):
        return "Sommet non-joignable depuis {}".format(debut), compteur

    if distances[fin] == float('inf'):
        return "Sommet d'arrivée non-joignable depuis {}".format(debut), compteur

    chemin = []
    actuel = fin
    while actuel != -1:
        chemin.insert(0, actuel)
        actuel = predecesseurs[actuel]

    return distances[fin], chemin, compteur
