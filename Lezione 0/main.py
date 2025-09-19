import os

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Scegli un'opzione:")
        print("1. Verifica se un numero è positivo, negativo o zero")
        print("2. Conversione di tipi di dato")
        print("99. Esci")
        choice = input(">>> ")
        match choice:
            case '1':
                import Modules.PositivoNegativo as Numeri
                Numeri.main()
            case '2':
                import Modules.TypeCasting as TypeCast
                TypeCast.main()
            case '99':
                print("Uscita in corso...")
                break
            case _:
                print("Opzione non valida. Riprova.")
