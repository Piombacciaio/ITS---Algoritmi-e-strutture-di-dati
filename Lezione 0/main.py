import os

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Scegli un'opzione:")
        print("1. Verifica se un numero è positivo, negativo o zero")
        print("2. Esci")
        choice = input(">>> ")
        match choice:
            case '1':
                import Algoritmi.PositivoNegativo as Numeri
                Numeri.function()
            case '2':
                print("Uscita in corso...")
                break
            case _:
                print("Opzione non valida. Riprova.")
