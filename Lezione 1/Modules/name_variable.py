import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


tipi = [
    "Le variabili sono scatole che possono contenere un tipo di dato. \nTipi di dato comuni in Python:",
    "str => Stringhe\n\t\"Questa è una stringa\"\n\t'Questa è una stringa'",
    "int => Interi\n\n\t2\n\t10000\n\t50\n\t-50\n\t-1000\n\t-2\n\n\tP.S. Non tutti i linguaggi accettano come intero\n\tanche i numeri negativi (ricordate questa)",
    "float => Numeri con la virgola\n\n\t3.45\n\t32.5435345\n\t890989020.23423432432",
    "bool => Valori logici\n\n\tTrue\n\tFalse\n\n\tP.S. Attenzione a digitare in upper case \n\taltrimenti non vengono riconosciuti",
    "tuple => Collezione ordinata di elementi\n\n\t(1, 2, 3)\n\t(\"ciao\", 3.14, True)\n\t(255,255,255) => RGB\n\n\tP.S. Sono immutabili quindi non possono essere\n\tmodificate",
    "list => Liste (simili ad array)\n\n\t[1, 2, 3, 4]\n\t[\"Ciao\",\"Cisco\",\"Savastano\"]\n\n\tN.B. Per accedere a un valore si parte da 0\n\tcome posizione\n\n\tP.S. Le liste accettano tutti i tipi di dati:\n\tnon per forza devono essere tutti dello stesso tipo,\n\tma così risulta più disordinato e meno gestibile",
    "dict => Sono dizionari\n\n\t{\"nome\": \"Marco\", \"età\": 29}\n\n\tN.B. Hanno sempre una coppia chiave:valore.\n\tLa chiave deve essere univoca (non può essere duplicata)",
    "None => Valore nullo \n\n\tN.B. È come il null in SQL o in altri linguaggi di programmazione",
]


ruls = [
    "Esistono diversi modi di dare un nome alle variabili",
    "Regola rigida: Devono essere descrittive ma non la Divina Commedia",
    "Se il programma calcola una media => media = (5+10+4)/3",
    "Scritture delle variabili:",
    "camelCase: firstName = 'Mauro' => legibile",
    "PascalCase: FirstName = 'Mauro' => tende ad essere meno leggibile",
    "snake_case: first_name = 'Mauro' => migliore per la leggibilità",
    "SCREAMING_SNAKE_CASE: FIRST_NAME = 'Mauro' => consigliato per le costanti",
    "flatcase: firstname = 'Mauro' => tende ad essere meno leggibile"
]



lesson = [tipi, ruls]

def main():
    choise = int(input("[0] Tipi\n\n[1]Regole di scrittura\n\n"))
    for x in lesson[choise]:
        print(x)
        input("\nPremi invio per continuare")
        clear()



if __name__ == '__main__':
    main()

