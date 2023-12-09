with open('data.txt', 'r') as fichier:
    lignes = fichier.readlines()
    # Convertir les lignes en liste d'entiers
    chiffres = [int(ligne.strip()) for ligne in lignes]

# Trier les chiffres par ordre croissant
chiffres_tries = sorted(chiffres)

# Calculer la médiane
n = len(chiffres_tries)
if n % 2 == 0:
    # Si le nombre de lignes est pair
    mediane = (chiffres_tries[n // 2 - 1] + chiffres_tries[n // 2]) / 2
else:
    # Si le nombre de lignes est impair
    mediane = chiffres_tries[n // 2]

# Calculer la moyenne
moyenne = sum(chiffres_tries) / n

# Calculer la variance
# calcule la différance entre x (une ligne) et la moyenne, la différence est enlevé est au carré, la somme des differences est ensuite divisé par n
variance = sum((x - moyenne) ** 2 for x in chiffres_tries) / n

# Calculer l'écart-type (racine carrée de la variance)
ecart_type = variance ** 0.5

# Afficher les résultats
print("Médiane :", mediane)
print("Moyenne :", moyenne)
print("Variance :", variance)
print("Écart-type :", ecart_type)
