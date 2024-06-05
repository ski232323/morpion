def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

def verifier_victoire(plateau, symbole):
    # Vérifier les lignes
    for ligne in plateau:
        if all(case == symbole for case in ligne):
            return True

    # Vérifier les colonnes
    for i in range(3):
        if all(plateau[j][i] == symbole for j in range(3)):
            return True

    # Vérifier les diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or \
            all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False

def jouer():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"

    while True:
        afficher_plateau(plateau)
        ligne = int(input(f"Joueur {joueur_actuel}, choisissez une ligne (0, 1, ou 2) : "))
        colonne = int(input(f"Joueur {joueur_actuel}, choisissez une colonne (0, 1, ou 2) : "))

        if plateau[ligne][colonne] != " ":
            print("Cette case est déjà occupée. Essayez à nouveau.")
            continue

        plateau[ligne][colonne] = joueur_actuel

        if verifier_victoire(plateau, joueur_actuel):
            print(f"Félicitations ! Joueur {joueur_actuel} a gagné !")
            break

        if all(plateau[i][j] != " " for i in range(3) for j in range(3)):
            print("Match nul !")
            break

        joueur_actuel = "O" if joueur_actuel == "X" else "X"

jouer()
