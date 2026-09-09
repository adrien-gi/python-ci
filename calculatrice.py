"""
Calculatrice simple - Addition
"""

def main():
    print("=== Calculatrice - Addition ===")
    print("Tape 'q' pour quitter à tout moment.\n")

    while True:
        entree1 = input("Premier nombre : ")
        if entree1.lower() == 'q':
            break

        entree2 = input("Deuxième nombre : ")
        if entree2.lower() == 'q':
            break

        try:
            nombre1 = float(entree1)
            nombre2 = float(entree2)
            resultat = nombre1 + nombre2
            print(f"Résultat : {nombre1} + {nombre2} = {resultat}\n")
        except ValueError:
            print("Erreur : merci d'entrer des nombres valides.\n")

    print("Au revoir !")


if __name__ == "__main__":
    main()
