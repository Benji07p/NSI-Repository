from pile import Pile

def affichage_texte(pile):
    '''affiche le texte dont les mots sont contenus dans la pile'''
    pile_temp = Pile()
    while not pile.est_vide():
        pile_temp.empiler(pile.depiler())
    if pile_temp.est_vide():
        texte = ''
    else:
        mot = pile_temp.depiler()
        texte = mot
        pile.empiler(mot)
    while not pile_temp.est_vide():
        mot = pile_temp.depiler()
        texte += ' ' + mot
        pile.empiler(mot)
    print(texte)

def editeur_texte():
    '''simulation de la fonctionnalité d'annulation d'un éditeur de texte'''
    modification = Pile()
    saisie = None
    while saisie != '':
        print('texte : ', end='')
        affichage_texte(modification)
        saisie = input('suite saisie : ')
        if saisie == '<CZ>':
            # simulation du Ctrl-Z d'un éditeur de texte
            print(f'annulation du mot : {modification.depiler()}')
        elif saisie != '':
            # on récupère les mots de la saisie
            lst_mots = saisie.split(' ')
            for mot in lst_mots:
                modification.empiler(mot)