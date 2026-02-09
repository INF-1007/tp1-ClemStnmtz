# -*- coding: utf-8 -*-
# Exercice 04 - Verification d'une rampe d'accessibilite (gabarit)
"""
Objectif :
- DEMANDER : hauteur (cm, float) et longueur (m, float)
- Valider : hauteur >= 0 et longueur > 0
- Calculer :
    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle = atan(hauteur_m / longueur_m) en degres
- Verifier la conformite : pente <= 8.00

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT :
    Pente: PP.PP%
    Angle: AA.AA deg
    Conforme: OUI|NON
Si NON, afficher une 4e ligne :
    Depassement: DD.DD%

Prompts EXACTS :
1) "Entrez la hauteur a franchir (en centimetres) : "
2) "Entrez la longueur horizontale (en metres) : "
"""

# TODO: Importer math

import math

# Lire hauteur (cm) et longueur (m)
hauteur_cm = float(input())
longueur_m = float(input())

# Validation
if hauteur_cm < 0 or longueur_m <= 0:
    print("Erreur - donnees invalides.")
    exit()

# Conversion hauteur en mètres
hauteur_m = hauteur_cm / 100

# Calcul de la pente (en %)
pente = (hauteur_m / longueur_m) * 100

# Calcul de l'angle (en radians puis en degrés)
angle_rad = math.atan(hauteur_m / longueur_m)
angle_deg = math.degrees(angle_rad)

# Affichage
print(f"Pente: {pente:.2f}%")
print(f"Angle: {angle_deg:.2f} deg")

# Vérification conformité (pente <= 8%)
if pente <= 8.00:
    print("Conforme: OUI")
else:
    print("Conforme: NON")
    depassement = pente - 8.00
    print(f"Depassement: {depassement:.2f}%")