"""Calculatrice simple - Addition."""


def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


def main():
    """Demande deux nombres et affiche leur somme."""
    nombre1 = float(input("Premier nombre : "))
    nombre2 = float(input("Deuxième nombre : "))

    resultat = addition(nombre1, nombre2)

    print(f"Résultat : {nombre1} + {nombre2} = {resultat}")


if __name__ == "__main__":
    main()
\n