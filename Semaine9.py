# Exercice 1

def entiers_consecutifs(tab):
    res = []
    for i in range(len(tab)-1):
        if tab[i] + 1 == tab[i+1]:
            res.append((tab[i], tab[i+1]))
    return res

# Exercice 2

def coefficients_binomiaux(n):
    triangle = [[1]]
    for i in range(1, n+1):
        ligne = [1]
        for j in range(1, i):
            ligne.append(triangle[i-1][j-1] + triangle[i-1][j])
        ligne.append(1)
        triangle.append(ligne)
    return triangle

# Exercice 3

def crible_eratosthene(n):
    liste_nombres_premiers = []
    tab = [True for _ in range(n+1)]
    tab[0], tab[1] = False, False
    for i in range(2, n+1):
        if tab[i]:
            liste_nombres_premiers.append(i)
            for multiples in range(2*i, n+1, i):
                tab[multiples] = False
    return liste_nombres_premiers

# Exercice 4

def inserer(lst, indice, element):
    nbre_elts = len(lst)
    lst_res = [None for _ in range(nbre_elts+1)]
    if indice < nbre_elts:
        for i in range(indice):
            lst_res[i] = lst[i]
        lst_res[indice] = element
        for i in range(indice+1, nbre_elts+1):
            lst_res[i] = lst[i-1]
    else:
        for i in range(nbre_elts):
            lst_res[i] = lst[i]
        lst_res[nbre_elts] = element
    return lst_res