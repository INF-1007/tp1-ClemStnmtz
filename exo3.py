# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math

# TODO: Lire les 4 valeurs
import math
donnes_valides = True
try :
    distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
    if distance < 0 :
        raise ValueError
    temps_navette = float(input("Entrez le temps d'attente de la navette (en minutes) : "))
    if temps_navette < 0 :
        raise ValueError
    temps_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
    if temps_metro < 0 :
        raise ValueError
    controle = float (input("Entrez le temps de controle a l'entree (en minutes) : "))
    if controle < 0 :
        raise ValueError
except ValueError:
    donnes_valides = False
    print("Erreur - donnees invalides.")
if donnes_valides :
    marche = distance * 60 / 5 + controle
    navette = temps_navette + distance * 60 / 18 + controle
    metro = temps_metro + controle
    options = [math.ceil(marche),math.ceil(navette),math.ceil(metro)]
    noms = ["marcher", "navette", "metro"]
    n = len(options)
for i in range(n):
    for j in range(n-i-1):
        if options[j]>options[j+1] : 
            options[j],options[j+1] = options[j+1],options[j]
            noms[j],noms[j+1] = noms[j+1],noms[j]
meilleur_opt = options[0]
gagnants = []
for i in range(n):
    if options[i]== options[0]:
        gagnants.append(noms[i])
if len(gagnants) == 1:
    print(f"Option la plus rapide : {gagnants[0]}.")
elif len(gagnants) == 2:
    print(f"Egalite : {noms[0]} et {noms[1]}.")
else :
    print(f"Egalite : marcher, navette et metro.")







# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)

# TODO: Afficher la phrase exacte
