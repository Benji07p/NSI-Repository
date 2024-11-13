# Exercice 1
def tri_bulles(tab):
    for i in range(len(tab)-1, 0 , -1):
        for j in range(i):
            if tab[j+1] < tab[j]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

# Exercice 2
def comptage_valeurs(n, tab):
    effectifs = [0 for _ in range(n+1)]
    for valeur in tab:
        effectifs[valeur] = effectifs[valeur] + 1
    return effectifs

def tri_comptage(n, tab):
    effectifs = comptage_valeurs(n , tab)
    return [i for i in range(n+1) for _ in range(effectifs[i])]

#Exercice 3
def tri_01(tab):
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
            
#Exercice 4
def liste_puissances_v1(a, n):
    tab = [1]
    for _ in range(n):
        tab.append(tab[-1]*a)
    return tab

def liste_puissances_v2(a, borne):
    tab = [1]
    while tab[-1] < borne:
        tab.append(tab[-1]*a)
    tab.pop()
    return tab