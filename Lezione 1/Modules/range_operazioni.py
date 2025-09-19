# Operatori di assegnazione
# += -> operatore di assegnazione incrementale
# -= -> operatore di assegnazione decrementale
# *= -> operatore di assegnazione moltiplicativa
# /= -> operatore di assegnazione divisiva
# //= -> operatore di assegnazione divisiva intera
# %= -> operatore di assegnazione modulo
# **= -> operatore di assegnazione esponenziale

# Altri operatori
# and, or, not
# is, is not -> operatore di identità
# in, not in -> operatore di appartenenza
# == -> operatore di uguaglianza
# != -> operatore di disuguaglianza
# < -> operatore di minore
# > -> operatore di maggiore
# <= -> operatore di minore o uguale
# >= -> operatore di maggiore o uguale
# +, -, *, /, //, %, **

def main():
    x = 0
    y = 0
    print("Incrementiamo x e y di 1, sei volte:\n")
    for _ in range(6):
        x = x + 1 # Aggiorno la variabile x
        y += 1 # Aggiorno la variabile y usando l'operatore di assegnazione incrementale
        print(f"Valore di x: {x}")
        print(f"Valore di y: {y}")
    print(f"Valore finale di x: {x}")
    print(f"Valore finale di y: {y}")
    print("\nOra incrementiamo x e y con i valori di i in range(6):\n")
    x = 0
    y = 0
    for i in range(6):
        x = x + i
        y += i
        print(f"Valore di x: {x}")
        print(f"Valore di y: {y}")
    print(f"Valore finale di x: {x}")
    print(f"Valore finale di y: {y}")

if __name__ == "__main__":
    main()