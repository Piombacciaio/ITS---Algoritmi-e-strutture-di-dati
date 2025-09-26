# Le Docstring sono stringhe speciali utilizzate per documentare moduli, classi, funzioni e metodi in Python.
# Le Docstring vengono racchiuse tra triple virgolette (""" """) e possono estendersi su più righe.
# Le Docstring dovrebbero descrivere brevemente lo scopo e il comportamento dell'elemento
# Le Docstring possono essere accessibili tramite l'attributo __doc__ dell'oggetto documentato.

def esempio_docstring():
    """Questa è una docstring di esempio.
    
    Questa funzione non fa nulla di particolare, ma serve a mostrare come si scrive una docstring.
    """
    pass

# Esistono varie convenzioni per scrivere docstring, tra cui:
# - La convenzione di Google
# - La convenzione di NumPy/SciPy
# - La convenzione di reStructuredText (reST)

# Esempio di docstring secondo la convenzione di Google
def funzione_con_docstring_google(parametro1, parametro2):
    """Esempio di docstring secondo la convenzione di Google.

    Args:
        parametro1 (int): Descrizione del parametro 1.
        parametro2 (str): Descrizione del parametro 2.

    Returns:
        bool: Descrizione del valore di ritorno.
    """
    return True

# Esempio di docstring secondo la convenzione di NumPy/SciPy
def funzione_con_docstring_numpy(parametro1, parametro2):
    """Esempio di docstring secondo la convenzione di NumPy/SciPy.

    Parameters
    ----------
    parametro1 : int
        Descrizione del parametro 1.
    parametro2 : str
        Descrizione del parametro 2.

    Returns
    -------
    bool
        Descrizione del valore di ritorno.
    """
    return True

# Esempio di docstring secondo la convenzione di reStructuredText (reST)
def funzione_con_docstring_rest(parametro1, parametro2):
    """Esempio di docstring secondo la convenzione di reStructuredText (reST).
    :param parametro1: Descrizione del parametro 1.
    :type parametro1: int
    :param parametro2: Descrizione del parametro 2.
    :type parametro2: str
    :return: Descrizione del valore di ritorno.
    :rtype: bool
    """

    return True


def main():
    esempio_docstring()
    funzione_con_docstring_google(1, "test")
    funzione_con_docstring_numpy(2, "test")
    funzione_con_docstring_rest(3, "test")

if __name__ == "__main__":
    main()