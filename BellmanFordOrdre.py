from choixListeFlèche import ordreArbitraire, ordreProfondeur, ordreLargeur


def BellmanFordOrder(M, start, end, order_type="arbitraire"):
    num_vertices = len(M)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    predecessors = [-1] * num_vertices
    count = 0

    if order_type == "largeur":
        edges = ordreLargeur(M, start)
    elif order_type == "longueur":
        edges = ordreProfondeur(M, start)
    else:
        edges = ordreArbitraire(M)

    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u
        count += 1

    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            return (
                "Sommet joignable depuis {}, mais pas de plus court chemin").format(
                start), count

    if all(distance == float('inf') for distance in distances):
        return "Sommet non-joignable depuis {}".format(start), count

    if distances[end] == float('inf'):
        return "Sommet d'arrivée non-joignable depuis {}".format(start), count

    path = []
    current = end
    while current != -1:
        path.insert(0, current)
        current = predecessors[current]

    return distances[end], path, count
