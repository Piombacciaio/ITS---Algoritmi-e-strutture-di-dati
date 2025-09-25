# Le stringhe in Python sono array di caratteri.
# Non esiste un tipo di dato char, una singola lettera è semplicemente una stringa di lunghezza 1.
# Le stringhe sono immutabili, non possono essere modificate dopo la loro creazione.
# Le stringhe possono essere racchiuse tra virgolette singole o doppie.
# Per includere caratteri speciali in una stringa, si usano le sequenze di escape.
# Le stringhe supportano molte operazioni, come la concatenazione, la ripetizione e l'indicizzazione.
# Le stringhe supportano molti metodi integrati per la manipolazione e l'analisi delle stringhe.

def main():
    # Creazione di stringhe
    stringa1 = "Ciao"
    stringa2 = 'Mondo'
    stringa3 = """Questa è una stringa
    multilinea."""
    print(stringa1, stringa2) # Concatenazione di stringhe
    print(stringa3)

    # Accesso ai caratteri
    print(stringa1[0]) # Primo carattere
    print(stringa2[-1]) # Ultimo carattere
    print(stringa1[1:3]) # Slicing
    print(stringa2[:3]) # Dall'inizio
    print(stringa2[2:]) # Fino alla fine
    print(stringa1[::2]) # Ogni secondo carattere
    print(stringa1[::-1]) # Stringa invertita

    # Metodi delle stringhe
    # Trasformazione del testo
    print(stringa1.lower()) # Tutto minuscolo
    print(stringa2.upper()) # Tutto maiuscolo
    print(stringa1.title()) # Iniziali maiuscole
    print(stringa1.capitalize()) # Prima lettera maiuscola
    print(stringa1.swapcase()) # Inverti maiuscole/minuscole

    # Logi test
    print(stringa1.startswith("C")) # Inizia con (True/False)
    print(stringa2.endswith("o")) # Finisce con (True/False)
    print(stringa1.isalpha()) # Solo lettere (True/False)
    print(stringa1.isdigit()) # Solo numeri (True/False)
    print(stringa1.islower()) # Tutto minuscolo (True/False)
    print(stringa1.isupper()) # Tutto maiuscolo (True/False)
    print(stringa1.isspace()) # Solo spazi (True/False)

    # math
    print(stringa1.find("a")) # Trova indice (-1 se non trovato)
    print(stringa1.count("a")) # Conta occorrenze
    print(stringa1.rfind("a")) # Trova indice da destra (-1 se non trovato)
    print(stringa1 * 3) # Ripetizione della stringa
    print(len(stringa1)) # Lunghezza della stringa

    # Alterazione del contenuto
    print(stringa1.replace("C", "H")) # Sostituzione
    print(stringa1.split("i")) # Divisione in lista
    print(stringa1.rsplit("i")) # Divisione in lista da destra
    print(stringa1.partition("i")) # Partiziona in tupla
    print(stringa1.strip()) # Rimuove spazi bianchi iniziali/finali
    print(stringa1.ljust(10, '-')) # Allinea a sinistra con '-'
    print(stringa1.center(10, '-')) # Centra con carattere di riempimento
    print(stringa1.rjust(10, '-')) # Allinea a destra con '-'
    print(stringa1.zfill(10)) # Riempi con zeri a sinistra
    print(stringa1.expandtabs(4)) # Espande tabulazioni

    # Formattazione
    print(" ".join([stringa1, stringa2])) # Unione di lista in stringa
    print(stringa1 + " " + stringa2) # Concatenazione
    print(f"{stringa1}, {stringa2}!") # Formattazione con f-string
    print("Ciao, {}!".format(stringa2)) # Formattazione con format

    # Altri metodi utili
    print(repr(stringa1)) # Rappresentazione ufficiale, utile per il debug
    print(stringa1.encode()) # Codifica in bytes

if __name__ == "__main__":
    main()