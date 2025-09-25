# While
# Il ciclo while viene utilizzato per eseguire un blocco di codice finché una condizione specificata è vera.

def main():
    count = 0
    while count < 5:
        print(f"Contatore: {count}")
        count += 1  # Incrementa il contatore per evitare un ciclo infinito

    print("Ciclo terminato.")

if __name__ == "__main__":
    main()