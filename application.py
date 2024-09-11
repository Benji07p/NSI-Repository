from flask import Flask, render_template, request
import folium, requests, urllib.parse
from math import radians, sin, cos, sqrt, asin
from datetime import datetime, timedelta, date

# obtenir l'année actuelle pour définir les dates de changements d'heures
annee_actuelle = date.today().year

# constante ETE pour le changement à l'heure d'été
ETE = datetime.strptime(f'{annee_actuelle}-03-31 02', "%Y-%m-%d %H")
while ETE.strftime('%A') != 'Sunday':
    ETE = ETE + timedelta(days=-1)

# constante HIVER pour le changement à l'heure d'hiver
HIVER = datetime.strptime(f'{annee_actuelle}-10-31 02', "%Y-%m-%d %H")
while HIVER.strftime('%A') != 'Sunday':
    HIVER = HIVER + timedelta(days=-1)

# constante API_KEY pour la clé de l'api de météo
API_KEY = 'f0de38431a3d5a4ed2f7f18d50fcae52'

# constante MOIS pour la correspondance numéro du mois et son nom
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

# récupérations des données via l'API
# source : https://data.nantesmetropole.fr/pages/home/
url = 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_parkings-publics-nantes-disponibilites/records?limit=0'
requete = requests.get(url)
donnees = requete.json()

# constante pour le nombre de parkings dans Nantes
NB_PARKING = donnees['total_count']

def obtenir_meteo(latitude, longitude, decalage):
    '''renvoie les données météo des coordonnées GPS indiquées sous forme d'un dictionnaire
    les clés du dictionnaire sont les chaînes de caractères de la forme 'aaaa mm jj'
    les valeurs associées à ses clés sont des dictionnaires dont les clés sont les heures
    pour chacun des jours et les valeurs sont des tableaux contenant la température, l'icône
    et la description pour l'heure concernée'''
    # récupérations des données via l'API
    # source : https://openweathermap.org/forecast5
    ...
    return {... : {}}

def parking_nantes():
    '''construire une carte en plaçant les parkings de Nantes'''
    # initialisation de la carte
    carte = folium.Map(location=[47.214, -1.552], zoom_start=14)

    # récupérations des données via l'API
    # source : https://data.nantesmetropole.fr/pages/home/
    url = "https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_parkings-publics-nantes-disponibilites/records?limit=29"
    requete = requests.get(url)
    donnees = requete.json()

    # rajout de marqueur sur la carte
    for loop in donnees["results"]:
        if loop["location"] is not None:
            position=[]
            position.append(loop["location"]["lat"])
            position.append(loop["location"]["lon"])
        nom = loop["grp_nom"]
        nb_place = loop["grp_disponible"]
        nb_place_total = loop["grp_exploitation"]
        folium.Marker(location=position, popup=f'{nom} :<br>{nb_place}/{nb_place_total}').add_to(carte)

    # sauvegarde de la carte
    carte.save('static/carte_parking.html')

def obtenir_coordonees(adresse):
    '''renvoie les coordonnées GPS de l'adresse saisie'''
    # récupérations des données via l'API
    # source : https://adresse.data.gouv.fr/api-doc/adresse
    url = f"https://api-adresse.data.gouv.fr/search/?q={adresse}"
    requete = requests.get(url)
    donnees = requete.json()
    for i in range(len(donnees["features"])):
        for j in donnees["features"][i]["geometry"]:
            if donnees["features"][i]["properties"]["context"] == "44, Loire-Atlantique, Pays de la Loire":
                tab = donnees["features"][i]["geometry"]["coordinates"]
                tab1 = []
                tab1.append(tab[1])
                tab1.append(tab[0])
                return tab1

def distance(pos1, pos2):
    '''renvoie la distance entre les deux positions GPS indiquées'''
    latitude1 = radians(pos1[0])
    longitude1 = radians(pos1[1])
    latitude2 = radians(pos2[0])
    longitude2 = radians(pos2[1])
    rayon = 6371
    terme1 = sin((latitude2-latitude1)/2) ** 2
    terme2 = cos(latitude1) * cos(latitude2) * sin((longitude2-longitude1)/2) ** 2
    return 2 * rayon * asin(sqrt(terme1 + terme2))

def parking_proche2(coordonnees):
    '''construire une carte en plaçant les trois parkings de Nantes les plus
    proches des coordonnées GPS indiquées'''
    # initialisation de la carte avec les coordonnées de l'adresse donnée
    carte = folium.Map(location=coordonnees, zoom_start=13)

    # récupérations des données via l'API
    # source : https://data.nantesmetropole.fr/pages/home/
    url = f'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_parkings-publics-nantes-disponibilites/records?limit={NB_PARKING}'
    requete = requests.get(url)
    donnees = requete.json()

    # recherche des trois parkings les plus proches
    tab = []
    dico = {}
    for loop in donnees["results"]:
        if loop["location"] is not None:
            position=[]
            position.append(loop["location"]["lat"])
            position.append(loop["location"]["lon"])
        dico["distance"] = distance(coordonnees, position)
        dico["nom"] = loop["grp_nom"]
        tab.append(dico)
        dico = {}
    tab1 = []
    for _ in range(3):
        minimum = tab[0]["distance"]
        for i in range(len(tab)):
            if tab[i]["distance"] < minimum :
                minimum = tab[i]["distance"]
                j = i
        tab1.append(tab[j])
        tab2 = []
        for k in range(j-1):
            tab2.append(tab[k])
        for k in range(j+1, len(tab)):
            tab2.append(tab[k])
        tab = tab2
    return tab1
    
def parking_proche(coordonnees):
    '''construire une carte en plaçant les trois parkings de Nantes les plus
    proches des coordonnées GPS indiquées'''
    # initialisation de la carte avec les coordonnées de l'adresse donnée
    carte = folium.Map(location=coordonnees, zoom_start=13)

    # récupérations des données via l'API
    # source : https://data.nantesmetropole.fr/pages/home/
    url = f'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_parkings-publics-nantes-disponibilites/records?limit={NB_PARKING}'
    requete = requests.get(url)
    donnees = requete.json()
    # rajout de marqueur sur la carte
    tab = parking_proche2(coordonnees)
    for loopr in range(len(donnees["results"])):
        for loop1 in range(len(tab)):
            if donnees["results"][loopr]["grp_nom"] == tab[loop1]["nom"] :
                if donnees["results"][loopr]["location"] is not None:
                    position = []
                    position.append(donnees["results"][loopr]["location"]["lat"])
                    position.append(donnees["results"][loopr]["location"]["lon"])
                nom = donnees["results"][loopr]["grp_nom"]
                nb_place = donnees["results"][loopr]["grp_disponible"]
                nb_place_total = donnees["results"][loopr]["grp_exploitation"]
                folium.Marker(location=position, popup=f'{nom} :<br>{nb_place}/{nb_place_total}').add_to(carte)

    # sauvegarde de la carte
    carte.save('static/carte_proche.html')

# création de l'application
application = Flask(__name__)

@application.route('/')
def index():
    aujourdhui = date.today()
    if ETE < datetime(aujourdhui.year, aujourdhui.month, aujourdhui.day) < HIVER:
        decalage = 2
    else:
        decalage = 1
    meteo = obtenir_meteo(47.1667, -1.5833, decalage)
    return render_template('index.html', meteo=meteo, horaire=decalage)

@application.route('/parking')
def parking():
    parking_nantes()
    return render_template('parking.html')

@application.route('/adresse')
def adresse():
    return render_template('adresse.html')

@application.route('/proximite')
def proximite():
    get = request.args
    if 'adr' in get:
        coordonnees = obtenir_coordonees(get['adr'])
        parking_proche(coordonnees)
        return render_template('proximite.html')
    else:
        return render_template('adresse.html')

if __name__ == '__main__':
    application.run(debug=True)