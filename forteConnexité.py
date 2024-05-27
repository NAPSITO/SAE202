def fermeture_transitive(M):
    n = len(M)
    fermeture = [row[:] for row in M]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                fermeture[i][j] = fermeture[i][j] or (fermeture[i][k] and fermeture[k][j])

    return fermeture


def fc(M):
    fermeture = fermeture_transitive(M)

    n = len(M)
    for i in range(n):
        for j in range(n):
            if i != j and fermeture[i][j] == 0:
                return False

    return True
