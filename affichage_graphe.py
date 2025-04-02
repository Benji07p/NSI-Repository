from graphviz import Digraph, \
                     Graph

def afficher_graphe_matrice(graphe, oriente, sommets):
    '''
    construit le graphe orienté ou non à l'aide de graphviz
      - graphe : défini par une matrice d'adjacence
      - oriente : True pour un graphe orienté, False sinon
      - sommets : liste précisant l'énumération à utiliser pour associer
    les sommets aux indices, None lorsque inconnu
    '''
    if oriente:
        graphique = Digraph('visualisation',
                            filename='visualisation',
                            format='svg',
                            engine='sfdp')
    else:
        graphique = Graph('visualisation',
                          filename='visualisation',
                          format='svg',
                          engine='sfdp')
    ordre = len(graphe)
    for i in range(ordre):
        if sommets == None:
            sommet = str(i)
        else:
            sommet = sommets[i]
        graphique.node(str(i), shape='circle',
                               style='solid',
                               width='0.5',
                               height='0.5',
                               fixedsize='true',
                               label=sommet)
    for i in range(ordre):
        if oriente:
            debut = 0
        else:
            debut = i
        for j in range(debut, ordre):
            if graphe[i][j] == 1:
                graphique.edge(str(i), str(j))
    graphique.view()

def afficher_graphe_listes_successeurs(graphe, oriente, sommets):
    '''
    construit le graphe orienté ou non à l'aide de graphviz
      - graphe : défini par une liste de listes de successeurs
      - oriente : True pour un graphe orienté, False sinon
      - sommets : liste précisant l'énumération à utiliser pour associer
    les sommets aux indices, None lorsque inconnu
    '''
    if oriente:
        graphique = Digraph('visualisation',
                            filename='visualisation',
                            format='svg',
                            engine='sfdp')
    else:
        graphique = Graph('visualisation',
                          filename='visualisation',
                          format='svg',
                          engine='sfdp')
    ordre = len(graphe)
    for i in range(ordre):
        if sommets == None:
            sommet = str(i)
        else:
            sommet = sommets[i]
        graphique.node(str(i), shape='circle',
                               style='solid',
                               width='0.5',
                               height='0.5',
                               fixedsize='true',
                               label=sommet)
    for i in range(ordre):
        if oriente:
            debut = 0
        else:
            debut = i
        for j in graphe[i]:
            if j >= debut:
                graphique.edge(str(i), str(j))
    graphique.view()