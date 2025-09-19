import os

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Scegli un'opzione:")
        print("1. Esegui script sulle liste")
        print("2. Esegui script sui dizionari")
        print("3. Esegui script sull'unpacking")
        print("4. Esegui script sulle operazioni con range")
        print("99. Esci")
        choice = input(">>> ")
        match choice:
            case '1':
                import Modules.liste as liste
                liste.main()
            case '2':
                import Modules.dizionari as dizionari
                dizionari.main()
            case '3':
                import Modules.unpacking as unpacking
                unpacking.main()
            case '4':
                import Modules.range_operazioni as range_op
                range_op.main()
            case '99':
                print("Uscita in corso...")
                break
            case _:
                print("Opzione non valida. Riprova.")
