# Pass
# la funzione pass non fa nulla
# si usa quando una funzione o un ciclo non ha ancora un corpo
# o quando si vuole creare una funzione vuota
# o quando si vuole creare una struttura di controllo che non ritorni nulla

def funzione_vuota():
    pass

def main():
    print("Esempio di funzione vuota:")
    funzione_vuota()
    print("La funzione non fa nulla, ma non genera errori.")

    if True:
        pass  # Non fa nulla
    else:
        print("Questo non verrà mai eseguito.")

if __name__ == "__main__":
    main()


    