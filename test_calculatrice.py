"""
Tests automatisés pour la calculatrice.

On importe la fonction 'addition' depuis calculatrice.py.
Comme cette fonction ne contient AUCUN input()/print(), on peut
l'appeler directement avec des valeurs choisies par nous, et vérifier
que le résultat est celui attendu. C'est tout l'intérêt d'avoir séparé
la logique (addition) de l'interaction utilisateur (main).

Pour lancer ces tests en local :
    python3 -m pytest test_calculatrice.py -v
"""

from calculatrice import addition


def test_addition_deux_nombres_positifs():
    """
    Teste le cas 'normal' : deux nombres positifs.
    Ça vérifie que le calcul de base fonctionne, tout simplement.
    """
    resultat = addition(3, 5)
    assert resultat == 8


def test_addition_nombre_negatif():
    """
    Teste l'addition avec un nombre négatif.
    Ça permet de vérifier que la fonction ne suppose pas, à tort,
    que les nombres seront toujours positifs (ex: bug si quelqu'un
    avait écrit une vérification 'if a > 0' par erreur).
    """
    resultat = addition(10, -4)
    assert resultat == 6


def test_addition_deux_nombres_negatifs():
    """
    Teste l'addition de deux nombres négatifs.
    Complète le test précédent pour couvrir aussi ce cas de figure
    (résultat négatif attendu).
    """
    resultat = addition(-3, -7)
    assert resultat == -10


def test_addition_avec_zero():
    """
    Teste l'addition avec zéro.
    Zéro est souvent une valeur 'piège' qui révèle des bugs
    (ex: si le code faisait une division ou une condition dessus).
    Ici on vérifie juste que 0 + n = n, comme attendu.
    """
    resultat = addition(0, 15)
    assert resultat == 15


def test_addition_nombres_decimaux():
    """
    Teste l'addition avec des nombres à virgule (float).
    Important car notre calculatrice utilise float() sur les saisies
    utilisateur : on veut être sûr que 2.5 + 2.5 donne bien 5.0.
    """
    resultat = addition(2.5, 2.5)
    assert resultat == 5.0


def test_addition_est_commutative():
    """
    Teste que l'ordre des nombres ne change pas le résultat
    (a + b doit être égal à b + a). C'est une propriété mathématique
    de l'addition ; ce test vérifie qu'on ne l'a pas cassée par erreur
    dans le code (ex: en utilisant a - b au lieu de a + b).
    """
    assert addition(4, 9) == addition(9, 4)


def test_addition_grands_nombres():
    """
    Teste l'addition avec de grands nombres.
    Permet de repérer d'éventuels problèmes de dépassement ou
    d'arrondi qui n'apparaîtraient pas avec des petits nombres.
    """
    resultat = addition(1_000_000, 2_500_000)
    assert resultat == 3_500_000
