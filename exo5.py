# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets

# Lire les données
try:
    n = int(input())
    statut = input()
except ValueError:
    print("Erreur - donnees invalides.")
    exit()

# Validation
if n < 0 or statut not in ['O', 'N']:
    print("Erreur - donnees invalides.")
    exit()

# Prix des forfaits
prix_24 = 66.00
prix_12 = 36.00
prix_5 = 15.75
prix_1 = 3.60

# Réduction étudiant (12% = 0.88)
reduction = 0.88 if statut == 'O' else 1.0

# Variables pour la meilleure solution
meilleur_prix = float('inf')
meilleur_A, meilleur_B, meilleur_C, meilleur_D = 0, 0, 0, 0
meilleur_total = float('inf')

# Bruteforce : tester toutes les combinaisons possibles
max_A = (n // 24) + 1
max_B = (n // 12) + 1
max_C = (n // 5) + 1

for A in range(max_A + 1):
    for B in range(max_B + 1):
        for C in range(max_C + 1):
            billets_forfaits = 24*A + 12*B + 5*C
            
            # Calculer le nombre de billets unitaires nécessaires
            if billets_forfaits >= n:
                D = 0
            else:
                D = n - billets_forfaits
            
            total_billets = billets_forfaits + D
            
            # Calculer le prix total
            prix_forfaits = (prix_24*A + prix_12*B + prix_5*C) * reduction
            prix_total = prix_forfaits + prix_1*D
            
            # Comparer avec la meilleure solution
            # Critères : 1) prix minimal, 2) total billets minimal, 3) D minimal
            if (prix_total < meilleur_prix) or \
               (prix_total == meilleur_prix and total_billets < meilleur_total) or \
               (prix_total == meilleur_prix and total_billets == meilleur_total and D < meilleur_D):
                meilleur_prix = prix_total
                meilleur_A, meilleur_B, meilleur_C, meilleur_D = A, B, C, D
                meilleur_total = total_billets

# Affichage du résultat
print(f"Forfaits de 24 billets - {meilleur_A}")
print(f"Forfaits de 12 billets - {meilleur_B}")
print(f"Forfaits de 5 billets - {meilleur_C}")
print(f"Billets unitaires - {meilleur_D}")
print(f"Total billets - {meilleur_total}")
print(f"Prix total - {meilleur_prix:.2f}$")