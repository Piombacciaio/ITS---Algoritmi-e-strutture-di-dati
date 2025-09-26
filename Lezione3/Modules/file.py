# In python è possibile lavorare sui file  per leggere o scrivere dati
# I file possono essere di vari tipi, come testo, binari, CSV, JSON, ecc.
# Le operazioni principali sui file sono apertura, lettura, scrittura e chiusura

def main():

    # il metodo di apertura with permette di omettere il metodo di chiusura lasciando il codice più pulito

    with open("esempio.txt", "w") as f:  # Apro un file in modalità scrittura
        f.write("Ciao, questo è un esempio di scrittura su file.\n")  # Scrivo una stringa nel file
        f.write("Questa è la seconda riga.\n")

    with open("esempio.txt", "r") as f:  # Apro il file in modalità lettura
        content = f.read()  # Leggo il contenuto del file
        print("Contenuto del file:")
        print(content)
        lines = f.readlines()  # Leggo il file riga per riga
        print("Righe del file:")
        for line in lines:
            print(line.strip())

    with open("esempio.txt", "a") as f:  # Apro il file in modalità append (aggiunta)
        f.write("Aggiungo una nuova riga alla fine del file.\n")  # Aggiungo una nuova riga

    # esempi senza with

    file = open("esempio.txt", "r")
    contenuto = file.read()
    file.close()
    print(contenuto)

if __name__ == "__main__":
    main()