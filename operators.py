def add(a,b):
    """Additionne deux nombres.

    Args:
        a (int): premier nombre.
        b (int): deuxieme nombre.

    Returns:
        int: la somme.
    """
    return a + b

def subtract(a,b):
    """Soustrait deux nombres.

    Args:
        a (int): premier nombre dont on soustrait le second.
        b (int): deuxieme nombre.

    Returns:
        int: la différence.
    """
    # BUG: on soustrait a de b et non b de a
    return a - b

def multiply(a,b):
    """Multiplie deux nombres.

    Args:
        a (int): premier nombre.
        b (int): deuxieme nombre.

    Returns:
        int: la multiplication.
    """
    # BUG: ici on ne fait pas a * b, soit la multiplication, on fait a^b donc un exposant.
    return a * b

def divide(a,b):
    """Divise deux nombres.

    Args:
        a (int): premier nombre, le dividende.
        b (int): deuxieme nombre, le diviseur.

    Returns:
        int: le quotient.
    """
    # BUG: ici on fait la division entière entre les nombres et non la division décimale
    return a / b