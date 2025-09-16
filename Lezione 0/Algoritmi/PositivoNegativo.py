import os

def function():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            n = int(input("Inserisci un numero >>> "))
            if n == 0:
                print("Il numero 0 non è né positivo né negativo.")
            elif n > 0:
                print("Il numero è positivo.")
            else:
                print("Il numero è negativo.")
            input("Premi Invio per continuare...")
        except ValueError:
            print("Per favore, inserisci un numero valido.")
        except KeyboardInterrupt:
            print("\nFine programma.")
            break

if __name__ == "__main__":
    function()