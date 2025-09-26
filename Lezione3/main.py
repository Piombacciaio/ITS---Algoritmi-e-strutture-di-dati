import Lezione3.Modules.functions as funcs
import Lezione3.Modules.docs as docs
import Lezione3.Modules.list_methods as list_methods
import Lezione3.Modules.dict_method as dict_method
import Lezione3.Modules.file as files
import Lezione3.Modules.globals as glob
import Lezione3.Modules.lambdas as lambdas

lista_opzioni = [
    "Scegli un opzione:\n"
    "1. Funzioni\n",
    "2. Documentazione (docstring)\n",
    "3. Metodi delle liste\n",
    "4. Metodi dei dizionari\n",
    "5. File\n",
    "6. Funzioni globali\n",
    "7. Funzioni lambda\n",
    "99. Exit\n"
]

lista_funz = {
    1: funcs.main,
    2: docs.main,
    3: list_methods.main,
    4: dict_method.main,
    5: files.main,
    6: glob.main,
    7: lambdas.main
}