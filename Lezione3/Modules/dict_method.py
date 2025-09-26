# I dizionari sono collezioni non ordinate di coppie chiave-valore, dove ogni chiave è unica e viene utilizzata per accedere al valore associato.
# I metodi dei dizionari sono funzioni predefinite che permettono di manipolare i dizionari in vari modi, come aggiungere, rimuovere o modificare elementi, o ottenere informazioni sul dizionario stesso.

def alpha_sort(d):
    
    return dict(sorted(d.items()))

def main():
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Dizionario di esempio:", sample_dict)
    # Estraggo i valori e le chiavi dal dizionario
    print("Chiavi:", sample_dict.keys())
    print("Valori:", sample_dict.values())
    print("Elementi:", sample_dict.items())
    # Aggiungo un nuovo elemento
    sample_dict['d'] = 4
    print("Dizionario dopo l'aggiunta di un elemento:", sample_dict)
    # Metodo get per ottenere un valore con una chiave, con un valore di default se la chiave non esiste
    print("Valore per la chiave 'a':", sample_dict.get('a', 'Non trovato'))
    print("Valore per la chiave 'z':", sample_dict.get('z', 'Non trovato')) # chiave non esistente
    # Verifico se una chiave esiste
    print("La chiave 'a' esiste?", 'a' in sample_dict)
    print("La chiave 'z' esiste?", 'z' in sample_dict)
    # Verifico se un valore esiste
    print("Il valore 3 esiste?", 3 in sample_dict.values())
    # Ottengo il numero di elementi nel dizionario
    print("Numero di elementi nel dizionario:", len(sample_dict))
    # Aggiorno il dizionario con un altro dizionario
    sample_dict.update({'e': 5, 'f': 6})
    print("Dizionario dopo l'aggiornamento:", sample_dict)
    # Copio il dizionario
    copied_dict = sample_dict.copy()
    print("Copia del dizionario:", copied_dict)
    # Rimuovo e restituisco un elemento
    removed_value = sample_dict.pop('c', None)
    print("Valore rimosso:", removed_value)
    print("Dizionario dopo la rimozione di un elemento:", sample_dict)
    # Pulisco il dizionario
    sample_dict.clear()
    print("Dizionario dopo la pulizia:", sample_dict)

if __name__ == "__main__":
    main()