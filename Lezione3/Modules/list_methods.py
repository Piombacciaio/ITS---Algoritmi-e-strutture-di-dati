# Le liste supportano vari metodi integrati che permettono di manipolare e gestire gli elementi al loro interno.

def main():
    lista = [1, 2, 3, 4, 5, "Ciao"]
    print("Lista originale:", lista)
    # Aggiungere un elemento alla fine della lista
    lista.append(6)
    print("Dopo append(6):", lista)
    # Rimuovere un elemento specifico dalla lista
    lista.remove(3)
    print("Dopo remove(3):", lista)
    # Rimuovere e restituire l'ultimo elemento della lista (o un elemento in una posizione specifica)
    ultimo = lista.pop()
    print("Elemento rimosso:", ultimo)
    # Ordinare la lista (funziona solo con elementi comparabili)
    lista_numerica = [5, 2, 9, 1, 5, 6]
    print("Lista numerica originale:", lista_numerica)
    lista_numerica.sort()
    print("Lista numerica ordinata:", lista_numerica)
    # Invertire l'ordine degli elementi nella lista
    lista_numerica.reverse()
    print("Lista numerica invertita:", lista_numerica)
    # Estendere la lista con un'altra lista
    lista.extend([7, 8, 9])
    print("Dopo extend([7, 8, 9]):", lista)
    # Inserire un elemento in una posizione specifica
    lista.insert(2, "Nuovo")
    print("Dopo insert(2, 'Nuovo'):", lista)
    # Contare quante volte un elemento appare nella lista
    happens = lista.count(2)
    print("Il numero 2 appare", happens, "volte nella lista.")
    # Trovare l'indice della prima occorrenza di un elemento
    index_of_ciao = lista.index("Ciao")
    print("L'indice di 'Ciao' è:", index_of_ciao)
    # Copiare la lista
    lista_copiata = lista.copy()
    print("Copia della lista:", lista_copiata)
    # Svuotare la lista
    lista.clear()
    print("Dopo clear():", lista)

if __name__ == "__main__":
    main()
    