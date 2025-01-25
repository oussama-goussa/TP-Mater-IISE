def add(a, b):
    """
    Additionne deux nombres.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: La somme des deux nombres.
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le deuxième nombre du premier.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: La différence entre les deux nombres.
    """
    return a - b

def multiply(a, b):
    """
    Multiplie deux nombres.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: Le produit des deux nombres.
    """
    return a * b

def divide(a, b):
    """
    Divise le premier nombre par le deuxième.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: Le quotient des deux nombres.

    Raises:
    ValueError: Si le deuxième nombre (b) est égal à zéro.
    """
    if b == 0:
        raise ValueError("Impossible de diviser par zéro")
    return a / b
