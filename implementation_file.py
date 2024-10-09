def afficher_file(file):
    if file.est_vide():
        ligne = '<-  '
    else:
        ligne = '<- | '
        tab = []
        while not file.est_vide():
            elt = file.defiler()
            tab.append(elt)
            ligne += str(elt) + ' | '
        for val in tab:
            file.enfiler(val)
    ligne = '  '+(len(ligne)-2)*'-' + '\n' + ligne + '\n  ' + (len(ligne)-2)*'-'
    print(ligne)

## Exercice 4 :

class File_tab:
    def __init__(self, taille):
        self.tab = ...
        self.indice = ...
        self.nb_elts = ...

    def est_vide(self):
        ...

    def enfiler(self, element):
        assert self.nb_elts < len(self.tab), 'La file est pleine'
        ...

    def avant(self):
        ...

    def defiler(self):
        ...

## Exercice 5 :

class Maillon:
    def __init__(self, element):
        self.suivant = None
        self.contenu = element

class File_chainee:
    def __init__(self):
        self.maillon_avant = ...
        self.maillon_arriere = ...

    def est_vide(self):
        ...

    def enfiler(self, element):
        ...

    def avant(self):
        ...

    def defiler(self):
        ...

## Exercice 6 :

class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return len(self.contenu) == 0

    def empiler(self, element):
        self.contenu.append(element)

    def sommet(self):
        return self.contenu[-1]

    def depiler(self):
        return self.contenu.pop()

class File_via_pile:
    def __init__(self):
        self.pile_arriere = ...
        self.pile_avant = ...

    def est_vide(self):
        ...

    def enfiler(self, element):
        ...

    def _transvasement(self):
        assert self.pile_avant.est_vide(), "Le transvasement ne s'effectue que si la pile avant est vide"
        ...

    def avant(self):
        ...

    def defiler(self):
        ...