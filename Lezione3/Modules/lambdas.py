# le lambda sono funzioni anonime, ovvero funzioni senza un nome definito, che possono essere create in modo rapido e conciso.
# Le lambda sono spesso utilizzate per operazioni semplici e brevi, come argomenti di altre funzioni, filtri, mappe e riduzioni.

def main():
    # sintassi: lambda argomenti: espressione

    # esempio 1: funzione lambda che somma due numeri
    somma = lambda x, y: x + y
    print("Somma di 3 e 5:", somma(3, 5))

    # esempio 2: funzione lambda che verifica se un numero è pari
    is_even = lambda x: x % 2 == 0
    print("Il numero 4 è pari?", is_even(4))
    print("Il numero 7 è pari?", is_even(7))

    # esempio 3: utilizzo di lambda con la funzione map per elevare al quadrato una lista di numeri
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print("Numeri al quadrato:", squared)

    # esempio 4: utilizzo di lambda con la funzione filter per filtrare i numeri pari da una lista
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Numeri pari:", even_numbers)

    # esempio 5: utilizzo di lambda con la funzione reduce per calcolare il prodotto di una lista di numeri
    from functools import reduce
    product = reduce(lambda x, y: x * y, numbers)
    print("Prodotto dei numeri:", product)

if __name__ == "__main__":
    main()