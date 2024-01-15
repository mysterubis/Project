from script1 import divide

def test_divide():
    # Test de la division de nombres positifs
    result = divide(10, 2)
    assert result == 5.0
    print("Test réussi : division de nombres positifs")

    # Test de la division de nombres négatifs
    result = divide(-10, 2)
    assert result == -5.0
    print("Test réussi : division de nombres négatifs")

    # Test de la division par zéro
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Impossible de diviser par zéro"
        print("Test réussi : division par zéro génère une exception ValueError")
    else:
        assert False, "Une ValueError était attendue, mais aucune exception n'a été levée"