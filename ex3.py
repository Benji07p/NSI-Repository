from representations import afficher_graphe_matrice,            \
                            afficher_graphe_listes_successeurs, \
                            sommets,                            \
                            matrice_orientee,                   \
                            listes_successeurs,                 \
                            matrice_non_orientee,               \
                            listes_adjacences,                  \
                            mes_sommets,                        \
                            mon_graphe,                         \
                            matrice_vers_listes_successeurs,    \
                            listes_successeurs_vers_matrice,    \
                            transformation_liste_vers_dico,     \
                            transformation_dico_vers_liste
from file import File

def explorer_profondeur_matrice(graphe, sommet, predecesseur, decouverte):
    '''modifie le dictionnaire précisant qui a découvert les sommets explorés
    (None pour le sommet de départ) à partir de la matrice d'adjacence du
    graphe orienté ou non, de l'indice d'un sommet et de l'indice du sommet
    d'où on provient grâce au parcours en profondeur'''
    if not sommet in decouverte:
        tab = graphe[sommet]
        decouverte[sommet] = predecesseur
        for i in range(len(tab)):
            if tab[i] == 1:
                explorer_profondeur_matrice(graphe, i, sommet, decouverte)

decouverte_profondeur = {}
explorer_profondeur_matrice(matrice_orientee, 4, None, decouverte_profondeur)
assert decouverte_profondeur == {4: None, 1: 4, 0: 1, 5: 0, 9: 5, 11: 9, 7: 1}

decouverte_profondeur = {}
explorer_profondeur_matrice(matrice_non_orientee, 5, None, decouverte_profondeur)
assert decouverte_profondeur == {5: None, 0: 5, 1: 0, 4: 1, 7: 4, 9: 1, 11: 9}

def explorer_profondeur_liste(graphe, sommet, predecesseur, decouverte):
    '''modifie le dictionnaire précisant qui a découvert les sommets explorés
    (None pour le sommet de départ) à partir de la liste des listes des
    successeurs du graphe orienté ou non, de l'indice d'un sommet et de
    l'indice du sommet d'où on provient grâce au parcours en profondeur'''
    decouverte[sommet] = predecesseur
    lst = graphe[sommet]
    for i in range(len(lst)):
        if not lst[i] in decouverte:
            explorer_profondeur_liste(graphe, lst[i], sommet, decouverte)

decouverte_profondeur = {}
explorer_profondeur_liste(listes_successeurs, 4, None, decouverte_profondeur)
assert decouverte_profondeur == {4: None, 1: 4, 0: 1, 5: 0, 9: 5, 11: 9, 7: 1}

decouverte_profondeur = {}
explorer_profondeur_liste(listes_adjacences, 5, None, decouverte_profondeur)
assert decouverte_profondeur == {5: None, 0: 5, 1: 0, 4: 1, 7: 4, 9: 1, 11: 9}

def chercher_profondeur(graphe, categorie, oriente, source, destination, ordre_sommet):
    '''renvoie une chaîne de caractères permettant d'aller de l'indice du sommet
    source à l'indice du sommet destination au sein du graphe (categorie = matrice
    liste, et oriente = True ou False) grâce à une exploration en profondeur
    l'association indice du sommet - étiquette du sommet est donnée via la
    liste ordre_sommet'''
    resultat = f'{ordre_sommet[source]}'
    decouverte_profondeur = {}
    tab = []
    if categorie == 'matrice':
        explorer_profondeur_matrice(graphe, source, None, decouverte_profondeur)
    elif categorie == 'listes':
        explorer_profondeur_liste(graphe, source, None, decouverte_profondeur)
    if not destination in decouverte_profondeur:
        return None
    i = destination
    while i != source :
        tab.append(i)
        i = decouverte_profondeur[i]
    for i in range(len(tab)-1, -1, -1):
        if oriente:
            resultat += f' → {ordre_sommet[tab[i]]}'
        else:
            resultat += f' - {ordre_sommet[tab[i]]}'
    return resultat

assert chercher_profondeur(matrice_orientee, 'matrice', True, 4, 11, sommets) == 'E → B → A → F → J → L'
assert chercher_profondeur(matrice_orientee, 'matrice', True, 11, 4, sommets) == None

assert chercher_profondeur(listes_successeurs, 'listes', True, 4, 11, sommets) == 'E → B → A → F → J → L'
assert chercher_profondeur(listes_successeurs, 'listes', True, 11, 4, sommets) == None

assert chercher_profondeur(matrice_non_orientee, 'matrice', False, 11, 7, sommets) == 'L - A - B - E - H'
assert chercher_profondeur(matrice_non_orientee, 'matrice', False, 7, 11, sommets) == 'H - B - A - F - J - L'
assert chercher_profondeur(matrice_non_orientee, 'matrice', False, 3, 2, sommets) == None

assert chercher_profondeur(listes_adjacences, 'listes', False, 11, 7, sommets) == 'L - A - B - E - H'
assert chercher_profondeur(listes_adjacences, 'listes', False, 7, 11, sommets) == 'H - B - A - F - J - L'
assert chercher_profondeur(listes_adjacences, 'listes', False, 3, 2, sommets) == None

def explorer_largeur_matrice(graphe, sommet_depart):
    '''renvoie un dictionnaire précisant qui a découvert les sommets explorés
    (None pour le sommet de départ) à partir de la matrice d'adjacence du
    graphe orienté ou non et de l'indice du sommet de départ grâce au parcours
    en largeur'''
    file = File()
    file.enfiler(sommet_depart)
    decouverte = {}
    decouverte[sommet_depart] = None
    while not file.est_vide():
        sommet = file.defiler()
        for i in range(len(graphe[sommet])):
            if graphe[sommet][i] == 1:
                if not i in decouverte:
                    decouverte[i] = sommet
                    file.enfiler(i)
    return decouverte

assert explorer_largeur_matrice(matrice_orientee, 4) == {4: None, 1: 4, 0: 1, 7: 1, 9: 1, 5: 0, 11: 9}

assert explorer_largeur_matrice(matrice_non_orientee, 5) == {5: None, 0: 5, 9: 5, 11: 5, 1: 0, 4: 1, 7: 1}

def explorer_largeur_liste(graphe, sommet_depart):
    '''renvoie un dictionnaire précisant qui a découvert les sommets explorés
    (None pour le sommet de départ) à partir de la liste des listes des
    successeurs du graphe orienté ou non et de l'indice du sommet de départ
    grâce au parcours en largeur'''
    file = File()
    file.enfiler(sommet_depart)
    decouverte = {}
    decouverte[sommet_depart] = None
    while not file.est_vide():
        sommet = file.defiler()
        for successeur in graphe[sommet]:
            if not successeur in decouverte:
                decouverte[successeur] = sommet
                file.enfiler(successeur)
    return decouverte

assert explorer_largeur_liste(listes_successeurs, 4) == {4: None, 1: 4, 0: 1, 7: 1, 9: 1, 5: 0, 11: 9}

assert explorer_largeur_liste(listes_adjacences, 5) == {5: None, 0: 5, 9: 5, 11: 5, 1: 0, 4: 1, 7: 1}

def chercher_largeur(graphe, categorie, oriente, source, destination, ordre_sommet):
    '''renvoie une chaîne de caractères permettant d'aller de l'indice du sommet
    source à l'indice du sommet destination au sein du graphe (categorie = matrice
    liste, et oriente = True ou False) grâce à une exploration en largeur
    l'association indice du sommet - étiquette du sommet est donnée via la
    liste ordre_sommet'''
    resultat = f'{ordre_sommet[source]}'
    decouverte_largeur = {}
    tab = []
    if categorie == 'matrice':
        decouverte_largeur = explorer_largeur_matrice(graphe, source)
    elif categorie == 'listes':
        decouverte_largeur = explorer_largeur_liste(graphe, source)
    if not destination in decouverte_largeur:
        return None
    i = destination
    while i != source :
        tab.append(i)
        i = decouverte_largeur[i]
    for i in range(len(tab)-1, -1, -1):
        if oriente:
            resultat += f' → {ordre_sommet[tab[i]]}'
        else:
            resultat += f' - {ordre_sommet[tab[i]]}'
    return resultat

assert chercher_largeur(matrice_orientee, 'matrice', True, 4, 11, sommets) == 'E → B → J → L'
assert chercher_largeur(matrice_orientee, 'matrice', True, 11, 4, sommets) == None

assert chercher_largeur(listes_successeurs, 'listes', True, 4, 11, sommets) == 'E → B → J → L'
assert chercher_largeur(listes_successeurs, 'listes', True, 11, 4, sommets) == None

assert chercher_largeur(matrice_non_orientee, 'matrice', False, 11, 7, sommets) == 'L - A - B - H'
assert chercher_largeur(matrice_non_orientee, 'matrice', False, 7, 11, sommets) == 'H - B - A - L'
assert chercher_largeur(matrice_non_orientee, 'matrice', False, 3, 2, sommets) == None

assert chercher_largeur(listes_adjacences, 'listes', False, 11, 7, sommets) == 'L - A - B - H'
assert chercher_largeur(listes_adjacences, 'listes', False, 7, 11, sommets) == 'H - B - A - L'
assert chercher_largeur(listes_adjacences, 'listes', False, 3, 2, sommets) == None