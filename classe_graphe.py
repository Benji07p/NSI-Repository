from affichage_graphe import afficher_graphe_matrice
class Graphe():
    def __init__(self, oriente, liste_sommet):
        self.matrice = []
        self.oriente = oriente
        self.liste_sommet = liste_sommet
    
    def ajouter_sommet(self):
        tab = [0 for _ in range(len(self.matrice))]
        self.matrice.append(tab)
        for i in range(len(self.matrice)):
            self.matrice[i].append(0)
            
    def ajouter_relation(self, source, destination):
        self.matrice[source][destination] = 1
        if not self.oriente :
            self.matrice[destination][source] = 1
        
    def __str__(self):
        afficher_graphe_matrice(self.matrice, self.oriente, self.liste_sommet)
        return ''
    
class Graphe_Pondere():
    def __init__(self, oriente, liste_sommet):
        self.matrice = []
        self.oriente = oriente
        self.liste_sommet = liste_sommet
    
    def ajouter_sommet(self):
        inf = float("inf")
        tab = [inf for _ in range(len(self.matrice))]
        self.matrice.append(tab)
        for i in range(len(self.matrice)):
            self.matrice[i].append(inf)
            
    def ajouter_relation(self, source, destination, ponderation):
        self.matrice[source][destination] = ponderation
        if not self.oriente :
            self.matrice[destination][source] = ponderation
        
    def __str__(self):
        #Ne fonctionne pas
        #afficher_graphe_matrice(self.matrice, self.oriente, self.liste_sommet)
        return ''
    
graphe = Graphe(False, ['1','2','3','4','5','6'])
for _ in range(6):
    graphe.ajouter_sommet()
graphe.ajouter_relation(0, 1)
graphe.ajouter_relation(0, 2)
graphe.ajouter_relation(0, 5)
graphe.ajouter_relation(1, 2)
graphe.ajouter_relation(1, 3)
graphe.ajouter_relation(2, 3)
graphe.ajouter_relation(4, 3)
graphe.ajouter_relation(4, 5)
graphe.ajouter_relation(2, 5)
print(graphe)