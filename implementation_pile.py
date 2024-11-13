def afficher_pile(pile):
    tab = []
    maxi = 0
    while not pile.est_vide():
        elt = pile.depiler()
        tab.append(elt)
        if len(str(elt)) > maxi:
            maxi = len(str(elt))
    for i in range(len(tab)-1, -1, -1):
        pile.empiler(tab[i])
    largeur = 2 + maxi
    ligne = '|' + largeur*' ' + '|\n|' + largeur*'-' + '|'
    for i in range(len(tab)):
        taille = len(str(tab[i]))
        espace2 = (largeur-taille) // 2
        espace1 = largeur - taille - espace2
        ligne += '\n|' + espace1*' ' + str(tab[i]) \
                + espace2*' ' + '|\n|' + largeur*'-' + '|'
    print(ligne)

## Exercice 2 :

class Pile_tab:
    def __init__(self, taille):
        self.tab = [None] * taille
        self.indice = -1

    def est_vide(self):
        return self.indice == -1

    def empiler(self, element):
        assert self.indice + 1 < len(self.tab), 'La pile est pleine'
        self.indice += 1
        self.tab[self.indice] = element

    def sommet(self):
        return self.tab[self.indice]

    def depiler(self):
        n = self.tab[self.indice]
        self.tab[self.indice] = None
        self.indice -= 1
        return n

## Exercice 3 :

class Maillon:
    def __init__(self, element):
        self.suivant = None
        self.contenu = element

class Pile_chainee:
    def __init__(self):
        self.maillon_sommet = None

    def est_vide(self):
        return self.maillon_sommet == None

    def empiler(self, element):
        maillon = Maillon(element)
        maillon_avant = self.maillon_sommet
        self.maillon_sommet = maillon
        self.maillon_sommet.suivant = maillon_avant

    def sommet(self):
        return self.maillon_sommet.contenu

    def depiler(self):
        n = self.maillon_sommet.contenu
        self.maillon_sommet = self.maillon_sommet.suivant
        return n

ma_pile.empiler(-4)
ma_pile.empiler(3)
ma_pile.empiler(0)
afficher_pile(ma_pile)
ma_pile.empiler(5)
ma_pile.est_vide()
ma_pile.sommet()
ma_pile.depiler()
afficher_pile(ma_pile)