import Lezione1.Modules.liste as liste
import Lezione1.Modules.dizionari as dizionari
import Lezione1.Modules.unpacking as unpacking
import Lezione1.Modules.range_operazioni as range_op
import Lezione1.Modules.delete_items as delete_items
import Lezione1.Modules.is_in as is_in
import Lezione1.Modules.boolean_operators as boolean_operators
import Lezione1.Modules.boolean_values as boolean_values
import Lezione1.Modules.name_variable as name_variable


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

lista_funz = {
    1: liste.main,
    2: dizionari.main,
    3: unpacking.main,
    4: range_op.main,
    5: delete_items.main,
    6: is_in.main,
    7: boolean_operators.main,
    8: boolean_values.main,
    9:  name_variable.main
}
