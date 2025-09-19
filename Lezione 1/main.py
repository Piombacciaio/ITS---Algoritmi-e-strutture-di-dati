import os

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Scegli un'opzione:")
        print("1. Esegui script sulle liste")
        print("2. Esegui script sui dizionari")
        print("3. Esegui script sull'unpacking")
        print("4. Esci")
        choice = input(">>> ")
        match choice:
            case '1':
                import Algoritmi.liste as liste
                liste.main()
            case '2':
                import Algoritmi.dizionari as dizionari
                dizionari.main()
            case '3':
                import Algoritmi.unpacking as unpacking
                unpacking.main()
            case '4':
                print("Uscita in corso...")
                break
            case _:
                print("Opzione non valida. Riprova.")
