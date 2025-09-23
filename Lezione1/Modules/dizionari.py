dizionario = {"a": 5, "b": 10}
# Un dizionario è una collezione di coppie chiave-valore
# Le chiavi sono uniche e immutabili, i valori possono essere di qualsiasi tipo

x, y = dizionario # unpacking delle chiavi
w, z = dizionario.values() # unpacking dei valori
def main():
    print(x, y)
    print(w, z)

if __name__ == "__main__":
    main()