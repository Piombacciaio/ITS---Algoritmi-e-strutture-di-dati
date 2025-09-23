def main():
    test_list = [1, 2, 3, 4, 5]
    test_values = [3, 6]
    for value in test_values: # Controllo se ogni valore della lista valori
        if value in test_list: # è presente nella lista test_list
            print(f"{value} è presente nella lista.")
        else:
            print(f"{value} non è presente nella lista.")

    # Questo controllo si può effettuare anche con le stringhe
    test_string = "Ciao, come va?"
    test_chars = ['a', 'z']
    for char in test_chars:
        if char in test_string:
            print(f"'{char}' è presente nella stringa.")
        else:
            print(f"'{char}' non è presente nella stringa.")

if __name__ == "__main__":
    main()