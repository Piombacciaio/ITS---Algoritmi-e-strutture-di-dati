import os

lista_opzioni = [
    "Scegli un'opzione:\n",
    "1. Esegui script sulle liste\n",
    "2. Esegui script sui dizionari\n",
    "3. Esegui script sull'unpacking\n",
    "4. Esegui script sulle operazioni con range\n",
    "5. Esegui script sulla cancellazione di elementi\n",
    "6. Esegui script sull'operatore in\n",
    "7. Esegui script sugli operatori booleani\n",
    "8. Esegui script sui valori booleani\n",
    "9. Esegui script sulle variabili e tipi\n"
    "99. Esci\n"
]



def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(*lista_opzioni)
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
            case '5':
                import Modules.delete_items as delete_items
                delete_items.main()
            case '6':
                import Modules.is_in as is_in
                is_in.main()
            case '7':
                import Modules.boolean_operators as boolean_operators
                boolean_operators.main()
            case '8':
                import Modules.boolean_values as boolean_values
                boolean_values.main()
            case '9':
                import Modules.name_variable as name_variable
                name_variable.main()

            case '99':
                print("Uscita in corso...")
                break
            case _:
                print("Opzione non valida. Riprova.")
        input("\nPremi Invio per continuare...")



if __name__ == '__main__':
    main()
