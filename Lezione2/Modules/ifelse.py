# if-else
# Gli statement if-else permettono di eseguire blocchi di codice differenti a seconda del valore di una condizione booleana (True o False).
# La sintassi generale è:
# if condizione:
#     blocco_di_codice_se_vero
# elif altra_condizione:
#     blocco_di_codice_se_altra_condizione_vera
# else:
#     blocco_di_codice_se_falso
#
# i blocchi di codice sono indentati (spazi o tabulazioni) per indicare che appartengono alla struttura di controllo.
# i blocchi elif e else sono opzionali, inoltre si possono avere più blocchi elif ma un solo blocco else alla fine.

def main():
    numero = int(input("Inserisci un numero intero: "))
    
    if numero > 0:
        print(f"{numero} è un numero positivo.")
    elif numero < 0:
        print(f"{numero} è un numero negativo.")
    else:
        print("Hai inserito zero.")
    
    # Esempio con più condizioni
    voto = int(input("Inserisci il tuo voto (0-100): "))
    
    if voto >= 90:
        print("Ottimo!")
    elif voto >= 75:
        print("Buono!")
    elif voto >= 60:
        print("Sufficiente!")
    else:
        print("Insufficiente!")

if __name__ == "__main__":
    main()