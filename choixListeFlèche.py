from collections import deque


def ordreArbitraire(M):
    edges = []
    for u in range(len(M)):
        for v in range(len(M)):
            if M[u][v] != 0:
                edges.append((u, v, M[u][v]))
    return edges


def ordreLargeur(M, start):
    num_vertices = len(M)
    visited = [False] * num_vertices
    queue = deque([start])
    visited[start] = True
    bfs_edges = []

    while queue:
        node = queue.popleft()
        for neighbor in range(num_vertices):
            if M[node][neighbor] != 0 and not visited[neighbor]:
                bfs_edges.append((node, neighbor, M[node][neighbor]))
                queue.append(neighbor)
                visited[neighbor] = True

    remaining_edges = [(u, v, M[u][v]) for u in range(num_vertices) for v in range(num_vertices) if
                       M[u][v] != 0 and (u, v, M[u][v]) not in bfs_edges]
    return bfs_edges + remaining_edges


def ordreProfondeur(M, start):
    num_vertices = len(M)
    visited = [False] * num_vertices
    stack = [start]
    dfs_edges = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in range(num_vertices):
                if M[node][neighbor] != 0 and not visited[neighbor]:
                    dfs_edges.append((node, neighbor, M[node][neighbor]))
                    stack.append(neighbor)

    remaining_edges = [(u, v, M[u][v]) for u in range(num_vertices) for v in range(num_vertices) if
                       M[u][v] != 0 and (u, v, M[u][v]) not in dfs_edges]
    return dfs_edges + remaining_edges
