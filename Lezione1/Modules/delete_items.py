def main():
    list_items = [1, 2, 3, 4, 5]
    print(list_items)  # Output: [1, 2, 3, 4, 5]
    del list_items[1]  # Rimuove l'elemento all'indice 1 (2° valore)
    print(list_items)  # Output: [1, 3, 4, 5]

    list_items = ['a', 'b', 'c', 'd', 'e']
    print(list_items)  # Output: ['a', 'b', 'c', 'd', 'e']
    del list_items[2:4]  # Rimuove gli elementi dall'indice 2 al 3 (4° escluso)
    print(list_items)  # Output: ['a', 'b', 'e']

    dict_items = {'a': 1, 'b': 2, 'c': 3}
    print(dict_items)  # Output: {'a': 1, 'b': 2, 'c': 3}
    del dict_items['b']  # Rimuove l'elemento con chiave 'b'
    print(dict_items)  # Output: {'a': 1, 'c': 3}

if __name__ == "__main__":
    main()