# Biblioteca de funciones para trabajar con cadenas


def longitud(cadena: str) -> int:
    """
    Calcula la longitud de una cadena.

    :param cadena: Cadena a evaluar.

    :return: Longitud de la cadena.
    """
    return len(cadena)



def invertir(cadena: str) -> str:
    """
    Invierte una cadena.

    :param cadena: Cadena a evaluar.

    :return: Cadena invertida.
    """

    for i in range(len(cadena)/2):
        cadena[i], cadena[-i] = cadena[-i], cadena[i]



