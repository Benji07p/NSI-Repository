from pile import Pile

# liste non exhaustive de bal ises HTML enregistrées en tant que clé d'un
# dictionnaire dont la valeur associée correspond à préciser si une
# fermeture de balise est attendu
BALISE = {'html': True, 'head': True, 'meta': False, 'title': True, 'body': True, 'h1': True, 'p': True, 'br': False, 'ul': True, 'li': True, 'a': True, 'img': False}

class HTML:
    '''classe pour lire un fichier HTML afin d'en extraire les balises'''
    def __init__(self, nom_fichier, encodage='utf-8'):
        '''lecture du fichier dont le nom est donné et initialisation de l'attribut position qui indique le premier caractère à lire'''
        with open(nom_fichier, encoding=encodage) as fichier:
            self.texte = fichier.read()
        self.position = 0
        self.ligne = 1

    def prochaine_balise(self):
        '''détermine la prochaine balise rencontrée dans le fichier à partir de la dernière position étudiée et renvoie son nom, le type si elle ouvre ou ferme (ouvre toujours pour une balise auto-fermante), et le numéro de ligne où se situe la balise'''
        # on déplace la tête de lecture à la prochaine ouverture de balise
        while self.position < len(self.texte) and self.texte[self.position] !=  '<':
            if self.texte[self.position] == '\n':
                self.ligne = self.ligne + 1
            self.position = self.position + 1
        # on récupère le nom qui est contenu dans la balise qui se situe
        # juste après le caractère <
        balise = ''
        self.position = self.position + 1
        if self.position < len(self.texte) and self.texte[self.position] == '!':
            # ce n'est pas une balise mais un commentaire (ou le DOCTYPE
            # intial), on poursuit jusqu'à la prochaine balise
            return self.prochaine_balise()
        if self.position < len(self.texte) and self.texte[self.position] == '/':
            # juste après le caractère <, on a le caractère /, c'est donc
            # la fermeture d'une balise, et le nom est juste après
            type = 'ferme'
            self.position = self.position + 1
            # on récupère le nom qui correspond à tous les caractères avant
            # le prochain caractère >
            while self.position < len(self.texte) and self.texte[self.position] !=  '>':
                balise = balise + self.texte[self.position]
                self.position = self.position + 1
        else:
            # on n'a pas le caractère /, c'est donc l'ouverture de la balise,
            # qui peut être une balise auto-fermante
            type = 'ouvre'
            # lors de l'ouverture d'une balise il peut y avoir, en plus du nom,
            # des attributs en plus, on récupère que le nom de départ
            ajout = True
            while self.position < len(self.texte) and self.texte[self.position] !=  '>':
                if ajout:
                    if self.texte[self.position] ==  ' ':
                        # on trouve un espace, sans avoir trouvé le caractère
                        # >, le nom de la balise est fini : il n'y a plus
                        # besoin de rajouter de carctères dans le nom de
                        # la balise
                        ajout = False
                    else:
                        balise = balise + self.texte[self.position]
                self.position = self.position + 1
        self.position = self.position + 1
        return (balise, type, self.ligne)

    def fin(self):
        '''renvoie True si le fichier a été lu dans sa globalité et False sinon'''
        # on poursuit la lecture du fichier jusqu'à rencontrer le prochain
        # caractère < ou atteindre la fin du fichier
        while self.position < len(self.texte) and \
                    self.texte[self.position] !=  '<':
            if self.texte[self.position] == '\n':
                self.ligne = self.ligne + 1
            self.position = self.position + 1
        if self.position+1 < len(self.texte) and \
                    self.texte[self.position+1] == '!':
            # c'est une balise de commentaire, on poursuit la lecture
            # du document
            self.position = self.position + 1
            return self.fin()
        else:
            return self.position >= len(self.texte)


def exemple_utilisation_classe_HTML():
    '''affiche la liste des balises contenues dans le fichier HTML d'exemple
    en donnant un exemple d'utilisation de la classe HTML'''
    # création de l'objet lié au fichier 'index.html'
    fichier_html = HTML('index.html')
    # méthode fin permet de renvoyer un booléen pour savoir si on a fini
    # la lecture du fichier
    while not fichier_html.fin():
        # méthode prochaine_balise renvoie 3 informations :
        #     - le nom de la balise
        #     - une chaîne de caractères "ouvre" ou "ferme" pour indiquer si
        # c'est l'ouverture ou la fermeture de la balise (toujours ouvre pour
        # une balise auto-fermante)
        #     - le numéro de ligne où est située cette balise dans le fichier
        balise, type, ligne = fichier_html.prochaine_balise()

        # affichage des informations obtenues
        print(f'balise : {balise} ({type}) à la ligne n°{ligne}')

def verification(nom_fichier, encodage='utf-8'):
    '''renvoie un tuple comprenant un booléen indiquant si les balises sont correctement ouverte et fermée et un message qui indique, lorsqu'il y a une erreur, la balise et la ligne fautive, ce message est 'OK' si il n'y a pas d'erreur'''
    fichier_html = HTML(nom_fichier, encodage)
    balises_ouvertes = Pile()
    while not fichier_html.fin():
        balise, etat, ligne = fichier_html.prochaine_balise()
        if etat == "ouvre" and BALISE[balise]:
            balises_ouvertes.empiler(balise)
        elif etat == "ferme":
            FEUR = balises_ouvertes.depiler()
            if FEUR != balise and BALISE[balise]:
                return (False, f'Ligne {ligne}, attendu {FEUR}, donné {balise}')
    if not balises_ouvertes.est_vide():
        LOL = ''
        while not balises_ouvertes.est_vide():
            LOL += ' ' + balises_ouvertes.depiler()
        return (False, f'Balise non fermée en fin de fichier : {LOL}')
    return (True, 'OK')