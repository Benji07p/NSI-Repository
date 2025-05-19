NOM_FICHIER1 = 'Le_tour_du_monde_en_80_jours-Jules_Verne.txt'
NOM_FICHIER2 = 'Voyage_au_centre_de_la_Terre-Jules_Verne.txt'

def recuperer_texte(nom_fichier, encodage='utf-8'):
    with open(nom_fichier, encoding='utf-8') as fichier:
        texte = fichier.read()
    return texte.lower()

def table_de_decalage(motif):
    '''renvoie la liste des dictionnaires permettant de récapituler les décalages'''
    tab = [{'autre': 1}]
    for j in range(1, len(motif)):
        dico = {cle: val+1 for cle, val in tab[j-1].items()}
        dico[motif[j-1]] = 1
        if motif[j] in dico:
            dico.pop(motif[j])
        tab.append(dico)
    return tab

assert table_de_decalage('heureusement') == [{'autre': 1}, {'autre': 2, 'h': 1}, {'autre': 3, 'h': 2, 'e': 1}, {'autre': 4, 'h': 3, 'e': 2, 'u': 1}, {'autre': 5, 'h': 4, 'u': 2, 'r': 1}, {'autre': 6, 'h': 5, 'r': 2, 'e': 1}, {'autre': 7, 'h': 6, 'r': 3, 'e': 2, 'u': 1}, {'autre': 8, 'h': 7, 'r': 4, 'u': 2, 's': 1}, {'autre': 9, 'h': 8, 'r': 5, 'u': 3, 's': 2, 'e': 1}, {'autre': 10, 'h': 9, 'r': 6, 'u': 4, 's': 3, 'm': 1}, {'autre': 11, 'h': 10, 'r': 7, 'u': 5, 's': 4, 'm': 2, 'e': 1}, {'autre': 12, 'h': 11, 'r': 8, 'u': 6, 's': 5, 'm': 3, 'e': 2, 'n': 1}]
assert table_de_decalage('phénomènes') == [{'autre': 1}, {'autre': 2, 'p': 1}, {'autre': 3, 'p': 2, 'h': 1}, {'autre': 4, 'p': 3, 'h': 2, 'é': 1}, {'autre': 5, 'p': 4, 'h': 3, 'é': 2, 'n': 1}, {'autre': 6, 'p': 5, 'h': 4, 'é': 3, 'n': 2, 'o': 1}, {'autre': 7, 'p': 6, 'h': 5, 'é': 4, 'n': 3, 'o': 2, 'm': 1}, {'autre': 8, 'p': 7, 'h': 6, 'é': 5, 'o': 3, 'm': 2, 'è': 1}, {'autre': 9, 'p': 8, 'h': 7, 'é': 6, 'o': 4, 'm': 3, 'è': 2, 'n': 1}, {'autre': 10, 'p': 9, 'h': 8, 'é': 7, 'o': 5, 'm': 4, 'è': 3, 'n': 2, 'e': 1}]

def mauvais_caractere(motif, texte, i):
    '''renvoie l'indice du caractère du motif qui rencontre un mauvais caractère
    dans le texte pour la fenêtre débutant à la position i
    -1 si il n'y a pas de mauvais caractère rencontré
    précondition : 0 <= i <= len(texte)-len(motif)'''
    assert 0 <= i <= len(texte)-len(motif) #i est plus grand que la longueur du texte
    j = len(motif) - 1
    while j >= 0 and motif[j] == texte[i+j]:
        j -= 1
    return j

assert mauvais_caractere('heureusement', recuperer_texte(NOM_FICHIER1), 6115) == 3
assert mauvais_caractere('heureusement', recuperer_texte(NOM_FICHIER1), 48904) == 11
assert mauvais_caractere('heureusement', recuperer_texte(NOM_FICHIER1), 147591) == -1
assert mauvais_caractere('phénomènes', recuperer_texte(NOM_FICHIER2), 48904) == 9
assert mauvais_caractere('phénomènes', recuperer_texte(NOM_FICHIER2), 273573) == 6
assert mauvais_caractere('phénomènes', recuperer_texte(NOM_FICHIER2), 370681) == -1

def recherche(motif, texte):
    '''renvoie la liste des positions où motif apparaît dans texte'''
    tab = table_de_decalage(motif)
    correspondance = []
    i = 0
    while i <= len(texte) - len(motif):
        j = mauvais_caractere(motif, texte, i)
        if j == -1:
            correspondance.append(i)
            i += 1
        elif texte[i+j] in tab[j]:
            i += tab[j][texte[i+j]]
        else:
            i += tab[j]['autre']
    return correspondance

assert recherche('heureusement', recuperer_texte(NOM_FICHIER1)) == [87464, 102774, 103913, 127857, 147591, 176929, 224284, 229328, 232962, 291276, 309873, 310422, 350130, 381700]
assert recherche('phénomènes', recuperer_texte(NOM_FICHIER2)) == [58027, 117708, 131195, 139865, 144985, 146404, 146440, 147169, 266644, 286697, 339332, 370681, 373629, 385506, 392991, 414933]