from generationAleatoire import graphe2


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


def test_stat_fc(n, nombreTest):
    nombreConnectés = 0

    for i in range(nombreTest):
        matrice = graphe2(n, 0.5, 0, 1)
        if fc(matrice):
            nombreConnectés += 1
    return (nombreConnectés / nombreTest) * 100


def test_stat_fc2(n, p, nombreTests):
    nombreConnectés = 0

    for i in range(nombreTests):
        matrice = graphe2(n, p, 0, 1)
        if fc(matrice):
            nombreConnectés += 1
    return (nombreConnectés / nombreTests) * 100


def seuil(n):
    p = 1.0
    while p > 0:
        proportion_connexe = test_stat_fc2(n, p, nombreTests=20)
        if proportion_connexe < 99:
            break
        p -= 0.1
    return p + 0.1
