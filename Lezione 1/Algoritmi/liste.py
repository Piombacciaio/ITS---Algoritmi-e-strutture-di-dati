import numpy as np

# Le liste sono collezioni ordinate e mutabili di elementi
# Gli array di NumPy sono collezioni ordinate e mutabili di elementi, ottimizzate per operazioni matematiche e scientifiche
# Le liste possono contenere elementi di tipi diversi, mentre gli array di NumPy sono omogenei (tutti dello stesso tipo)

glyc_list = [165, 167, 169, 174, 175, 179] # lista standard di Python
glyc_np = np.array([165, 167, 169, 174, 175, 179]) # array di NumPy

def main():
    print(glyc_list, type(glyc_list))
    print(glyc_np, type(glyc_np))

if __name__ == "__main__":
    main()