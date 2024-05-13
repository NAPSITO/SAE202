def bellman_ford(M, start, end):
    num_vertices = len(M)
    # Initialisation des distances
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    # Initialisation des itinéraires
    predecessors = [-1] * num_vertices

    # Itération sur chaque nœud pour mettre à jour les distances
    for _ in range(num_vertices - 1):
        for node in range(num_vertices):
            for neighbor in range(num_vertices):
                if M[node][neighbor] != 0:
                    if distances[node] + M[node][neighbor] < distances[neighbor]:
                        distances[neighbor] = distances[node] + M[node][neighbor]
                        predecessors[neighbor] = node

    # Vérification de la présence de cycles négatifs
    for node in range(num_vertices):
        for neighbor in range(num_vertices):
            if M[node][neighbor] != 0:
                if distances[node] + M[node][neighbor] < distances[neighbor]:
                    return "Sommet joignable depuis {} par un chemin dans le graphe, mais pas de plus court chemin (présence d'un cycle négatif)".format(start)

    # Vérification de la connectivité du sommet de départ
    if all(distance == float('inf') for distance in distances):
        return "Sommet non-joignable depuis {} par un chemin dans le graphe".format(start)

    # Vérification de la connectivité du sommet d'arrivée
    if distances[end] == float('inf'):
        return "Sommet d'arrivée non-joignable depuis {} par un chemin dans le graphe".format(start)

    # Reconstruction de l'itinéraire
    path = []
    current = end
    while current != -1:
        path.insert(0, current)
        current = predecessors[current]

    return distances[end], path

# Exemple d'utilisation
matrice = [
    [0, 4, 0, 0, 0],
    [-1, 0, 3, 2, 2],
    [0, 0, 0, 0, 0],
    [0, 1, 5, 0, 0],
    [0, 0, -3, 0, 0]
]

start = 0
end = 4
result = bellman_ford(matrice, start, end)

if isinstance(result, tuple):
    distance, path = result
    print("Longueur du plus court chemin de", start, "à", end, ":", distance)
    print("Itinéraire :", path)
else:
    print(result)
