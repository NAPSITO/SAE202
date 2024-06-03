from collections import deque


def ordreArbitraire(M):
    arretes = []
    for u in range(len(M)):
        for v in range(len(M)):
            if M[u][v] != 0:
                arretes.append((u, v, M[u][v]))
    return arretes


def ordreLargeur(M, debut):
    nombreSommets = len(M)
    visite = [False] * nombreSommets
    queue = deque([debut])
    visite[debut] = True
    bfs_arretes = []

    while queue:
        noeud = queue.popleft()
        for voisin in range(nombreSommets):
            if M[noeud][voisin] != 0 and not visite[voisin]:
                bfs_arretes.append((noeud, voisin, M[noeud][voisin]))
                queue.append(voisin)
                visite[voisin] = True

    arretes_restantes = [(u, v, M[u][v]) for u in range(nombreSommets) for v in range(nombreSommets) if
                         M[u][v] != 0 and (u, v, M[u][v]) not in bfs_arretes]
    return bfs_arretes + arretes_restantes


def ordreProfondeur(M, debut):
    nombreSommets = len(M)
    visite = [False] * nombreSommets
    pile = [debut]
    dfs_arretes = []

    while pile:
        noeud = pile.pop()
        if not visite[noeud]:
            visite[noeud] = True
            for voisin in range(nombreSommets):
                if M[noeud][voisin] != 0 and not visite[voisin]:
                    dfs_arretes.append((noeud, voisin, M[noeud][voisin]))
                    pile.append(voisin)

    arretes_restantes = [(u, v, M[u][v]) for u in range(nombreSommets) for v in range(nombreSommets) if
                         M[u][v] != 0 and (u, v, M[u][v]) not in dfs_arretes]
    return dfs_arretes + arretes_restantes
