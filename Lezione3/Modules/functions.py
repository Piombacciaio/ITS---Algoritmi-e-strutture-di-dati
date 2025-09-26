# le funzioni sono blocchi di codice riutilizzabili che eseguono un compito specifico.
# Le funzioni in Python sono definite usando la parola chiave def, seguita dal nome della funzione e dalle parentesi.
# Le funzioni possono accettare parametri, che sono variabili passate alla funzione per influenzarne il comportamento.
# Le funzioni possono restituire valori usando la parola chiave return.

def funzione_senza_parametri():
    print("Ciao dal modulo delle funzioni!")

def funzione_con_parametri(nome, eta):
    print(f"Ciao {nome}, hai {eta} anni.")

# Le variabili possono avere dei valori di default, che vengono usati se non viene passato nessun valore per quel parametro.
def funzione_con_parametri_default(nome="Utente", eta=0):
    print(f"Ciao {nome}, hai {eta} anni.")

def funzione_con_restituzione(valore):
    return valore * 2

def main():
    funzione_senza_parametri()
    funzione_con_parametri("Alice", 30)
    funzione_con_parametri_default()
    funzione_con_parametri_default("Bob", 25)
    risultato = funzione_con_restituzione(10)
    print(f"Il risultato della funzione con restituzione è: {risultato}")

if __name__ == "__main__":
    main()