import os

def function():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            n = float(input("Inserisci un numero (con virgola o punto) >>> ").replace(',', '.'))
            print(f"Hai inserito il numero: {n}")
            input("Premi Invio per continuare...")
        except ValueError:
            print("Per favore, inserisci un numero valido.")
        except KeyboardInterrupt:
            print("\nFine programma.")
            break

if __name__ == "__main__":
    function()