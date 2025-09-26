# Le variabili globali sono variabili definite al di fuori di qualsiasi funzione, accessibili da qualsiasi parte del codice
# Le variabili globali possono essere utili per condividere dati tra funzioni, ma il loro uso eccessivo può rendere il codice difficile da leggere e mantenere

def main():
    global global_var
    global_var = "Sono una variabile globale"
    print(global_var)
    
    def inner_function():
        print(global_var)  # Accesso alla variabile globale

    inner_function()

if __name__ == "__main__":
    main()