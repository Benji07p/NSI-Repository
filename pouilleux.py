from random import shuffle

class Carte:
    '''
    valeur des cartes : As (1), 2 à 10, Valet (11), Dame (13) et Roi (14)
    couleur des cartes : pique (0), coeur (1), carreau (2) et trèfle (3)
    '''

    def __init__(self, val, coul):
        self.valeur = val
        self.couleur = coul

    def carte_visible(self):
        numero = 0x1f0a0 + self.valeur + 16 * self.couleur
        return chr(numero)

    def carte_non_visible(self):
        return chr(0x1f0a0)

    def rouge_noir(self):
        if self.couleur == 0 or self.couleur == 3:
            return 'black'
        else:
            return 'red'

    def paire_avec(self, autre_carte):
        return self.valeur == autre_carte.valeur\
               and self.couleur + autre_carte.couleur == 3

# Question 1 :
# nom = Carte
# attributs = val, coul
# méthodes = __init__, paire_avec, rouge_noir, carte_non_visible, carte_visible

# Question 2 :
huit_coeur = Carte(8, 1)
dame_trefle = Carte(13, 3)
valet_pique = Carte(11, 0)
huit_carreau = Carte(8, 2)

# Question 3 :
#huit_coeur.paire_avec(huit_carreau)
#dame_trefle.rouge_noir()
#huit_carreau.carte_non_visible()
#valet_pique.carte_visible()

# Question 4 :
class Joueur:
    '''La classe Joueur possède 3 attributs :
    - nom (str) : nom du joueur
    - type (str) : type de joueur humain/machine
    - paquet (list[Carte]) : liste des cartes du joueur'''

    def __init__(self, information):
        '''le paramètre information est un couple de str correspondant au nom et type de joueur
        lors de l'initialisation le joueur ne possède pas de cartes'''
        if information[0] == "humain" or information[0] == "machine":
            self.nom = information[1]
            self.type = information[0]
        else :
            self.nom = information[0]
            self.type = information[1]
        self.paquet = []

    def ajouter_carte(self, carte):
        '''ajoute l'objet carte au paquet du joueur renvoie rien'''
        self.paquet.append(carte)

    def obtenir_carte(self, num):
        '''renvoie l'objet carte à l'indice num du paquet du joueur'''
        return self.paquet[num]

    def retirer_carte(self, num):
        '''retire l'objet carte à l'indice num du paquet du joueur
        renvoie l'objet carte retirer'''
        return self.paquet.pop(num)

    def trouver_paire(self):
        '''recherche une paire de carte au sein du paquet lorsqu'une telle paire existe :
        renvoie le couple d'indice de cette paire, l'indice le plus petit en premier
        (il est possible d'avoir plusieurs paire, une seule paire est recherchée et renvoyée)
        lorsqu'il n'y a aucune paire : renvoie rien'''
        for i in range(len(self.paquet)):
            for j in range(len(self.paquet)):
                if self.paquet[i].paire_avec(self.paquet[j]):
                    return (i, j)
        return None

class Pouilleux:
    '''La classe Pouilleux possède 1 attribut :
    - joueurs (list[Joueur]) : la liste des 3 joueurs'''

    def __init__(self, noms):
        '''le paramètres noms est une liste de 3 couples correspondant au (nom du joueur, type du joueur)
        de chacun des 3 joueurs le joueur 1 : est à l'indice 0, le joueur 2 : est à l'indice 1
        le joueur 3 : est à l'indice 2'''
        self.joueurs = [Joueur(noms[0]), Joueur(noms[1]), Joueur(noms[2])]

    def distribuer(self):
        '''permet de distribuer les 51 cartes aléatoirement (paquet de 52 cartes
        sans le valet de trèfle) aux 3 joueurs (17 cartes par joueur) renvoie rien'''
        cartes = []
        for i in range(4):
            for j in range(1, 11):
                cartes.append(Carte(j,i))
            cartes.append(Carte(13,i))
            cartes.append(Carte(14,i))
            if i != 3:
                cartes.append(Carte(11,i))
        shuffle(cartes)
        for j in range(17):
            for i in range(3):
                self.joueurs[i].ajouter_carte(cartes[3*j+i])


    def retirer_paires(self):
        '''permet de retirer toutes les paires de tous les joueurs renvoie rien'''
        for i in range(3):
            while self.joueurs[i].trouver_paire() is not None:
                var = self.joueurs[i].trouver_paire()
                self.joueurs[i].retirer_carte(var[0])
                self.joueurs[i].retirer_carte(var[1]-1)

    def retirer_paire_de(self, joueur):
        '''permet de rechercher une paire dans le paquet du joueur dont l'indice
        est donné et de la retirer si elle existe renvoie rien'''
        condition = self.joueurs[joueur].trouver_paire() is None or self.joueurs[joueur].trouver_paire()[1] is None
        condition = condition or self.joueurs[joueur].trouver_paire()[0] is None
        if condition:
            return None
        pos = self.joueurs[joueur].trouver_paire()
        self.joueurs[joueur].retirer_carte(pos[1])
        self.joueurs[joueur].retirer_carte(pos[0])

    def nom_joueur(self, joueur):
        '''renvoie le nom du joueur dont l'indice est donné'''
        return self.joueurs[joueur].nom

    def ajouter_carte_a(self, joueur, carte):
        '''ajoute l'objet carte à l'indice au paquet du joueur dont
        l'indice est donné'''
        self.joueurs[joueur].ajouter_carte(carte)

    def obtenir_carte_de(self, joueur, num):
        '''renvoie l'objet carte à l'indice num du paquet du joueur dont l'indice
        est donné'''
        return self.joueurs[joueur].obtenir_carte(num)

    def retirer_carte_a(self, joueur, num):
        '''retire l'objet carte à l'indice num du paquet du joueur dont l'indice
        est donné renvoie l'objet carte retirer'''
        return self.joueurs[joueur].retirer_carte(num)

    def nombre_de_cartes_de(self, joueur):
        '''renvoie le nombre de cartes du joueur dont l'indice est donné'''
        return len(self.joueurs[joueur].paquet)

    def est_humain(self, joueur):
        '''renvoie True lorsque le joueur dont l'indice est donné est de type
        humain, et False sinon'''
        return self.joueurs[joueur].type == "humain"
    
    
########################################################################################
def infos_joueur(joueur):
    info = f'Mon nom est : {joueur.nom}\n'
    info += f'Il est un : {joueur.type}\n'
    if len(joueur.paquet) == 0:
        info += 'Il possède aucune carte.\n'
    elif len(joueur.paquet) == 1:
        info += 'Il possède la carte :\n    {joueur.paquet[0].carte_visible()}\n'
    else:
        info += 'Il possède les cartes :\n    '
        for carte in joueur.paquet:
            info += f'{carte.carte_visible()}'
        info += '\n'
    return info

# test création d'un joueur
mon_joueur = Joueur(('Moi', 'humain'))
test = infos_joueur(mon_joueur)
print(test)
assert test == 'Mon nom est : Moi\nIl est un : humain\nIl possède aucune carte.\n'

# test ajouter_carte pour un joueur
mon_joueur.ajouter_carte(Carte(1, 0))
mon_joueur.ajouter_carte(Carte(13, 3))
mon_joueur.ajouter_carte(Carte(14, 0))
mon_joueur.ajouter_carte(Carte(6, 2))
mon_joueur.ajouter_carte(Carte(11, 1))
mon_joueur.ajouter_carte(Carte(14, 3))
mon_joueur.ajouter_carte(Carte(6, 1))
test = infos_joueur(mon_joueur)
print(test)
assert test == 'Mon nom est : Moi\nIl est un : humain\nIl possède les cartes :\n    🂡🃝🂮🃆🂻🃞🂶\n'

# test trouver_paire pour un joueur
i, j = mon_joueur.trouver_paire()
assert i == 2
assert j == 5

# test obtenir_carte pour un joueur
test = f'Une paire : {mon_joueur.obtenir_carte(i).carte_visible()} - {mon_joueur.obtenir_carte(j).carte_visible()}\n'
print(test)
assert test == 'Une paire : 🂮 - 🃞\n'

# test retirer_carte pour un joueur
mon_joueur.retirer_carte(j)
mon_joueur.retirer_carte(i)
test = infos_joueur(mon_joueur)
print(test)
assert test == 'Mon nom est : Moi\nIl est un : humain\nIl possède les cartes :\n    🂡🃝🃆🂻🂶\n'

# fin des tests
i, j = mon_joueur.trouver_paire()
assert i == 2
assert j == 4
test = f'Une paire : {mon_joueur.obtenir_carte(i).carte_visible()} - {mon_joueur.obtenir_carte(j).carte_visible()}\n'
print(test)
assert test == 'Une paire : 🃆 - 🂶\n'
mon_joueur.retirer_carte(j)
mon_joueur.retirer_carte(i)
assert mon_joueur.trouver_paire() == None
test = infos_joueur(mon_joueur)
print(test)
assert test == 'Mon nom est : Moi\nIl est un : humain\nIl possède les cartes :\n    🂡🃝🂻\n'

def infos_jeu(jeu):
    info = ''
    for i in range(3):
        info += f'Joueur {i+1} :\n    '
        info += infos_joueur(jeu.joueurs[i]).replace('\n', '\n    ')
        info += '\n'
    return info

mon_jeu = Pouilleux([('Moi', 'humain'), ('Alice', 'machine'), ('Bob', 'machine')])
test = infos_jeu(mon_jeu)
print(test)
assert test == 'Joueur 1 :\n    Mon nom est : Moi\n    Il est un : humain\n    Il possède aucune carte.\n    \nJoueur 2 :\n    Mon nom est : Alice\n    Il est un : machine\n    Il possède aucune carte.\n    \nJoueur 3 :\n    Mon nom est : Bob\n    Il est un : machine\n    Il possède aucune carte.\n    \n'
mon_jeu.distribuer()
tab = ['Moi', 'Alice', 'Bob']
for i in range(3):
    assert mon_jeu.nom_joueur(i) == tab[i]
tab = [True, False, False]
for i in range(3):
    assert mon_jeu.est_humain(i) == tab[i]
for i in range(3):
    assert mon_jeu.nombre_de_cartes_de(i) == 17
print(infos_jeu(mon_jeu))
mon_jeu.retirer_paires()
print(infos_jeu(mon_jeu))
