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
    '''
    renvoie la liste des étiquettes via un parcours en largeur
    '''
    file = creer_file_vide()
    enfiler(file, arbre)
    tab = []
    while not file_est_vide(file) :
        arbre_en_cours = defiler(file)
        if not est_vide(arbre_en_cours):
            tab.append(racine(arbre_en_cours))
            enfiler(file, gauche(arbre_en_cours))
            enfiler(file, droit(arbre_en_cours))
    return tab

def profondeur(arbre, prefixe, infixe, suffixe):
    '''
    renvoie un triplet correspondant à :
      - la liste des étiquettes via un parcours en profondeur en ordre préfixe
      - la liste des étiquettes via un parcours en profondeur en ordre infixe
      - la liste des étiquettes via un parcours en profondeur en ordre suffixe
    '''
    if not est_vide(arbre):
        prefixe.append(racine(arbre))
        profondeur(gauche(arbre), prefixe, infixe, suffixe)
        infixe.append(racine(arbre))
        profondeur(droit(arbre), prefixe, infixe, suffixe)
        suffixe.append(racine(arbre))
    return prefixe, infixe, suffixe

def taille(arbre):
    '''
    renvoie la taille de l'arbre binaire
    '''
    if est_vide(arbre):
        return 0
    else:
        return 1 + taille(gauche(arbre)) + taille(droit(arbre))

def hauteur(arbre):
    '''
    renvoie la hauteur de l'arbre binaire
    '''
    if est_vide(arbre):
        return -1
    else:
        return 1 + max(hauteur(gauche(arbre)), hauteur(droit(arbre)))

def etiquette_presente(arbre, valeur):
    '''
    renvoie True lorsque valeur correspond à une étiquette de l'arbre binaire,
    False sinon
    '''
    if est_vide(arbre):
        return False
    else:
        return racine(arbre) == valeur \
                    or etiquette_presente(gauche(arbre), valeur) \
                    or etiquette_presente(droit(arbre), valeur)

print('largeur : ', largeur(arbre_prof), end='\n\n')
prefixe, infixe, suffixe = profondeur(arbre_prof, [], [], [])
print('profondeur ordre préfixe : ', prefixe, end='\n\n')
print('profondeur ordre infixe : ', infixe, end='\n\n')
print('profondeur ordre suffixe : ', suffixe, end='\n\n')
print('taille = ', taille(arbre_prof), end='\n\n')
print('hauteur = ', hauteur(arbre_prof), end='\n\n')
print('G :', etiquette_presente(arbre_prof, 'G'))
print('Z :', etiquette_presente(arbre_prof, 'Z'))
