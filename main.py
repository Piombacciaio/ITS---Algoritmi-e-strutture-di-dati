import os, sys

import Lezione0.main as L0 
import Lezione1.main as L1
import Lezione2.main as L2
import Dispense.main as DM


lista_opzioni = [
    "Scegli un opzione:\n\n"
    "0. Lezione 0\n",
    "1. Lezione 1\n",
    "2. Lezione 2\n",
    "88. Dispense\n",
    "99. Exit\n"
]

lista_funz = {
    0: [L0.lista_funz, L0.lista_opzioni],
    1: [L1.lista_funz, L1.lista_opzioni],
    2: [L2.lista_funz, L2.lista_opzioni]
}

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:

        clean()

        print(*lista_opzioni)

        try:
            choice = int(input(">> "))
        except (ValueError, KeyError):
            clean()
            continue
        except KeyboardInterrupt:
            sys.exit(0)
        
        if choice == 99:
            clean() 
            sys.exit(0)
        elif choice == 88:
            clean()
            DM.dispensa()
            continue


        while True:

            clean()

            print(*lista_funz[choice][1])

            try:
                choice_lesson = int(input(">> "))
            except (ValueError, KeyError):
                clean()
                continue
            except KeyboardInterrupt:
                sys.exit(0)

            if choice_lesson == 99:
                clean() 
                break
            if choice_lesson in lista_funz[choice][0]: 
                lista_funz[choice][0][choice_lesson]()
                
            input("Premi per continuare...")

    


if __name__ == "__main__":
    main()


