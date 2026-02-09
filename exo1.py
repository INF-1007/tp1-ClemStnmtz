# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer

- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str)
nom = input("Entrez votre nom complet : ")
donnees_valides = True
# TODO: Lire les 4 valeurs (int)
try :
    NbMtch = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
    DurMoyF = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
    NbMtchFem = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
    DurMoyS = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
    if NbMtch < 0 or NbMtchFem < 0:
        raise ValueError
    if (NbMtch > 0 and DurMoyF <= 0) or (NbMtchFem > 0 and DurMoyS <= 0):
        raise ValueError
except ValueError :
    #donnees_valides = False
    print("Erreur - donnees invalides.")
else:

# TODO: Valider les donnees (matchs >= 0, durees > 0)


# TODO: Calculer les minutes totales (football, soccer, total)
    DurFtot = DurMoyF * NbMtch
    DurStot = DurMoyS * NbMtchFem
    Duree_Globale_Minutes = DurFtot + DurStot 

    # TODO: Convertir en heures/minutes
    # Foot
    hf = DurFtot // 60
    mf = DurFtot % 60
    # Soccer
    hs = DurStot // 60
    ms = DurStot % 60
    # Total
    htot = Duree_Globale_Minutes // 60
    mintot = Duree_Globale_Minutes % 60

    print(f"Bonjour {nom}")
    print(f"Football (Carabins): {NbMtch} match(s), {hf}h{mf:02d} de visionnage")
    print(f"Soccer (Carabins): {NbMtchFem} match(s), {hs}h{ms:02d} de visionnage")
    print(f"Total: {htot}h{mintot:02d}")

