from affichage_arbre import creer_arbre_vide,   \
                            creer_arbre,        \
                            est_vide,           \
                            racine,             \
                            gauche,             \
                            droit,              \
                            afficher_arbre,     \
                            arbre_prof
from file import creer_file_vide,   \
                 file_est_vide,     \
                 enfiler,           \
                 defiler

def largeur(arbre):
    '''renvoie la liste des étiquettes via un parcours en largeur'''
    file_au_pif = creer_file_vide()
    lst = []
    val = arbre
    lst.append(racine(val))
    enfiler(file_au_pif, gauche(val))
    enfiler(file_au_pif, droit(val))
    while not file_est_vide(file_au_pif):
        val = defiler(file_au_pif)
        if not est_vide(val):
            lst.append(racine(val))
            enfiler(file_au_pif, gauche(val))
            enfiler(file_au_pif, droit(val))
    return lst

def profondeur(arbre, prefixe, infixe, suffixe):
    '''renvoie un triplet correspondant à la liste des étiquettes via un
    parcours en profondeur en ordre préfixe, infixe et suffixe'''
    if est_vide(arbre):
        return 0
    prefixe.append(racine(arbre))
    profondeur(gauche(arbre), prefixe, infixe, suffixe)
    infixe.append(racine(arbre))
    profondeur(droit(arbre), prefixe, infixe, suffixe)
    suffixe.append(racine(arbre))
    return (prefixe, infixe, suffixe)

def taille(arbre):
    '''renvoie la taille de l'arbre binaire'''
    if est_vide(arbre):
        return 0
    t1 = taille(gauche(arbre))
    t2 = taille(droit(arbre))
    return 1+t2+t1

def hauteur(arbre):
    '''renvoie la hauteur de l'arbre binaire'''
    if est_vide(arbre):
        return -1
    h1 = hauteur(gauche(arbre))
    h2 = hauteur(droit(arbre))
    val = h1
    if h2 > h1:
        val = h2
    return 1+val

def etiquette_presente(arbre, valeur):
    '''renvoie True lorsque valeur correspond à une étiquette de l'arbre binaire, False sinon'''
    if est_vide(arbre):
        return False
    if racine(arbre) == valeur:
        return True
    return etiquette_presente(gauche(arbre), valeur) or etiquette_presente(droit(arbre), valeur)
    
print(largeur(arbre_prof))
print(profondeur(arbre_prof, [],[],[]))
print(taille(arbre_prof))
print(hauteur(arbre_prof))
print(etiquette_presente(arbre_prof, 'G'))
print(etiquette_presente(arbre_prof, 'Z'))