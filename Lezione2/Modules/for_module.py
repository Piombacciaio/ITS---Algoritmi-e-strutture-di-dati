# For
# Il ciclo for viene utilizzato per iterare su una sequenza (come una lista, una tupla, un dizionario, un insieme o una stringa).

def main():
    # Esempio con una lista
    frutti = ["mela", "banana", "ciliegia"]
    for frutto in frutti:
        print(frutto)
    
    print()

    # Esempio con una stringa
    parola = "Python"
    for lettera in parola:
        print(lettera)
    
    print()

    # Esempio con range()
    for i in range(5):  # Itera da 0 a 4
        print(i)
    
    print()

    for i in range(2, 10, 2):  # Itera da 2 a 8 con passo di 2
        print(i)
    
    print("Ciclo terminato.")

if __name__ == "__main__":
    main()